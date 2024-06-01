from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers.string import StrOutputParser

# Initialize the ChatOpenAI client with your API key
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

client = ChatOpenAI(api_key=api_key,model="gpt-4o")

# Define the messages with roles
messages = [
    SystemMessage(content="You are a translator. Translate the following English text to French."),
    HumanMessage(content="Hello, how are you?")
]

# Generate the response from the model
##response = client(messages)

# Initialize the string output parser
#output_parser = StrOutputParser()

# Parse the response
#content = output_parser.parse(response)


response = client.invoke(input=messages)
parser = StrOutputParser()
content = parser.invoke(input=response)

# Print the output
print(content)
