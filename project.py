import os.path
import json
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain.schema import Document
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
import os
from dotenv import load_dotenv
import sys


# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv('PINECONE_API_KEY')

def authenticate_gmail():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        with open('token.json', 'r') as token:
            creds_info = json.load(token)
            creds = Credentials.from_authorized_user_info(info=creds_info, scopes=SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service

def get_full_message(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    payload = msg['payload']
    headers = payload.get("headers")
    parts = payload.get("parts")
    
    data = ""
    if not parts:
        data = payload['body']['data']
    else:
        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                break
            elif part['mimeType'] == 'text/html':
                data = part['body']['data']
    
    decoded_data = base64.urlsafe_b64decode(data).decode('utf-8')
    
    # Sanitize and clean up the message
    soup = BeautifulSoup(decoded_data, 'html.parser')
    cleaned_text = soup.get_text()

    return cleaned_text

def list_emails_with_label(service, label_name):
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    label_id = None
    for label in labels:
        if label['name'].lower() == label_name.lower():
            label_id = label['id']
            break

    if not label_id:
        print(f"Label '{label_name}' not found.")
        return []

    results = service.users().messages().list(userId='me', labelIds=[label_id]).execute()
    messages = results.get('messages', [])

    email_texts = []

    if not messages:
        print(f"No emails found with label '{label_name}'.")
    else:
        print(f"Emails with label '{label_name}':")
        for message in messages:
            msg_id = message['id']
            full_message = get_full_message(service, msg_id)
            email_texts.append(Document(page_content=full_message))
            # print(f"Full message:\n{full_message}\n{'-'*50}\n")
    
    return email_texts

def query_todo():
    prompt = "Summarize my todo"

    # Note: we must use the same embedding model that we used when uploading the docs
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # Querying the vector database for "relevant" docs
    document_vectorstore = PineconeVectorStore(index_name="todo-email", embedding=embeddings)
    retriever = document_vectorstore.as_retriever()
    context = retriever.get_relevant_documents(prompt)
    #for doc in context:
       # print(f"Content: {doc}\n\n")
   # print("__________________________")

    # Adding context to our prompt
    template = PromptTemplate(template="{query} Context: {context}", input_variables=["query", "context"])
    prompt_with_context = template.invoke({"query": prompt, "context": context})

    # Asking the LLM for a response from our prompt with the provided context
    llm = ChatOpenAI(temperature=0.7)
    results = llm.invoke(prompt_with_context)

    print(results.content)

def main():

    # This section of the code determines the action to be performed based on the command line argument.
    # It supports two actions: 'add' and 'query'.
    # 'add' action will authenticate Gmail, retrieve emails with a specific label, split the email texts,
    # and upload them to a Pinecone vector database using a specified embedding model.
    # 'query' action will perform a search in the vector database to find relevant documents based on a prompt,
    # and then use a language model to generate a summary of these documents.

    action = sys.argv[1] if len(sys.argv) > 1 else 'query'

    if action == 'add':
        service = authenticate_gmail()
        label_name = 'todo'  # Change this to your label name
        email_texts = list_emails_with_label(service, label_name)
        
        # Prepare documents to be uploaded to the vector database (Pinecone)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        documents = text_splitter.split_documents(email_texts)
        print(f"Going to add {len(documents)} to Pinecone")

        # Choose the embedding model and vector store
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        PineconeVectorStore.from_documents(documents=documents, embedding=embeddings, index_name="todo-email")
        print("Loading to vectorstore done")
    elif action == 'query':
        query_todo()
    else:
        print("Invalid action. Please use 'add' or 'query'.")

if __name__ == '__main__':
    main()
