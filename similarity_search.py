from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema.document import Document

# Initialize the embeddings class
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Embed a single query
query = "Hello, world!"
vector = embeddings.embed_query(query) # [281, 392, 34993, 23,...]
print(vector[:5])

# Embed multiple documents at once
documents = [
    Document(page_content="Alice works in finance"),
    Document(page_content="Bob is a database administrator"),
    Document(page_content="Carl manages Bob and Alice"),
]
vector_datastore = FAISS.from_documents(documents, embeddings)

# Perform a similarity search with scores
query = "Tell me about Alice"
docs_and_scores = vector_datastore.similarity_search_with_score(query)
print(docs_and_scores)