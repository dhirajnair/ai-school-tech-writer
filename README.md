# AI for Developer Productivity: Technical Writer Agent

## Overview
In this project, we developed a **Technical Writer Agent** to enhance developer productivity. The core functionality of our agent leverages Retrieval-Augmented Generation (RAG) to dynamically update and refine technical documentation. This innovative approach not only streamlines the documentation process but also ensures that it remains accurate, up-to-date, and contextually relevant.

## New Features

### Gmail Integration for Email Summarization
We have added new functionality to extract emails from Gmail with a specific label, create embeddings for the email contents, and store these embeddings in Pinecone. This allows the system to summarize emails based on stored embeddings.

### Added Scripts
1. **add_rag.py**: 
    - This script uploads documents (PDFs) to a vector database (Pinecone) after splitting them into smaller chunks and embedding them using OpenAI embeddings.
   
2. **project.py**:
    - Authenticates and interacts with the Gmail API to list and retrieve emails with a specific label.
    - Splits email contents into smaller chunks and uploads them to Pinecone.
    - Provides functionality to query these stored email embeddings for summarization.

3. **retrieve_rag.py**:
    - Demonstrates querying the vector database for relevant documents and generating a response using a language model.
   
4. **similarity_search.py**:
    - Shows how to perform a similarity search using FAISS with embedded documents.

### Enhanced .gitignore
- Added entries to ignore `credentials.json` and `token.json` for security reasons.

## Now It's Your Turn!
Embrace your creativity and personalize this project to craft a solution that uniquely addresses the challenges and inefficiencies you face in your own environment. After seeing what our Technical Writer Agent can do, it’s time for you to take the reins. Use the foundation we’ve built and apply it to a challenge you face in your own professional or personal environment. Here’s how you can get started:

### Minimum Requirements
1. **RAG Integration:** Successfully integrate Retrieval-Augmented Generation (RAG) to enable your agent to access and utilize external information when generating responses.
2. **Vector Database Implementation:** Create and implement a vector data store capable of embedding and retrieving documents, ensuring that the system can access necessary information efficiently.

### Stretch Goals
1. **Enhanced UI/UX:** Develop a more advanced and user-friendly interface that includes features such as real-time suggestions, auto-completion of content, and a more interactive documentation process.
2. **Automated Content Updates:** Implement a feature where the agent periodically checks and updates existing documentation based on new information or changes in the relevant field, ensuring that all documentation remains current without manual intervention.
3. **Integration with Existing Tools:** Develop integrations for the agent with commonly used development tools and platforms (e.g., Confluence, Jira, Notion) to streamline workflows and increase accessibility.
4. **Add The Features You Want**: Let your creativity shine by adding a unique feature that significantly simplifies or enhances your daily routines. Innovate with functionalities that solve problems and improve efficiency or satisfaction in meaningful ways.

## Privacy and Submission Guidelines
- **Submission Requirements:** Please submit a link to your public repo with your implementation or a loom video showcasing your work on the [BloomTech AI Platform](app.bloomtech.com). 
- **Sensitive Information:** If your implementation involves sensitive information, you are not required to submit a public repository. Instead, a detailed review of your project through a Loom video is acceptable, where you can demonstrate the functionality and discuss the technologies used without exposing confidential data.

---

### Requirements
To use the new features, ensure you have the following dependencies installed. You can find these in the `requirements.txt` file:

```plaintext
aiosignal==1.3.1
annotated-types==0.6.0
anyio==4.3.0
attrs==23.2.0
beautifulsoup4==4.12.3
cachetools==5.3.3
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
cryptography==42.0.5
Deprecated==1.2.14
distro==1.9.0
frozenlist==1.4.1
google-api-core==2.19.0
google-api-python-client==2.131.0
google-auth==2.29.0
google-auth-httplib2==0.2.0
google-auth-oauthlib==1.2.0
googleapis-common-protos==1.63.0
h11==0.14.0
httpcore==1.0.5
httplib2==0.22.0
httpx==0.27.0
idna==3.7
jsonpatch==1.33
jsonpointer==2.4
langchain==0.2.1
langchain-core==0.2.3
langchain-openai==0.1.8
langchain-pinecone==0.1.1
langchain-text-splitters==0.2.0
langsmith==0.1.65
lxml==5.2.2
numpy==1.26.4
oauthlib==3.2.2
openai==1.30.5
orjson==3.10.3
packaging==23.2
pinecone-client==3.2.2
proto-plus==1.23.0
protobuf==4.25.3
pyasn1==0.6.0
pyasn1_modules==0.4.0
pycparser==2.22
pydantic==2.7.1
pydantic_core==2.18.2
PyGithub==2.3.0
PyJWT==2.8.0
PyNaCl==1.5.0
pyparsing==3.1.2
python-dotenv==1.0.1
PyYAML==6.0.1
regex==2024.5.15
requests==2.31.0
requests-oauthlib==2.0.0
rsa==4.9
sniffio==1.3.1
soupsieve==2.5
SQLAlchemy==2.0.30
tenacity==8.3.0
tiktoken==0.7.0
tqdm==4.66.2
typing_extensions==4.11.0
uritemplate==4.1.1
urllib3==2.2.1
wrapt==1.16.0
yarl==1.9.4
```