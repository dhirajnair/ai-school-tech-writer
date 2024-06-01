# AI for Developer Productivity: Technical Writer Agent

## Overview
In this project, we developed a **Technical Writer Agent** to enhance developer productivity. The core functionality of our agent leverages Retrieval-Augmented Generation (RAG) to dynamically update and refine technical documentation. This innovative approach not only streamlines the documentation process but also ensures that it remains accurate, up-to-date, and contextually relevant.

## Now It's Your Turn!
Embrace your creativity and personalize this project to craft a solution that uniquely addresses the challenges and inefficiencies you face in your own environment. After seeing what our Technical Writer Agent can do, it’s time for you to take the reins. Use the foundation we’ve built and apply it to a challenge you face in your own professional or personal environment. Here’s how you can get started:

### Minimum Requirements
1. **RAG Integration:** Successfully integrate Retrieval-Augmented Generation (RAG) to enable your agent to access and utilize external information when generating responses.
2. **Vector Database Implementation:** Create and implement a vector data store capable of embedding and retrieving documents, ensuring that the system can access necessary information efficiently.

### Stretch Goals
1. **Enhanced UI/UX:** Develop a more advanced and user-friendly interface that includes features such as real-time suggestions, auto-completion of content, and a more interactive documentation process.
2. **Automated Content Updates:** Implement a feature where the agent periodically checks and updates existing documentation based on new information or changes in the relevant field, ensuring that all documentation remains current without manual intervention.
3. **Integration with Existing Tools:** Develop integrations for the agent with commonly used development tools and platforms (e.g., Confluence, Jira, Notion) to streamline workflows and increase accessibility.
4. **Add The Features You Want:** Let your creativity shine by adding a unique feature that significantly simplifies or enhances your daily routines. Innovate with functionalities that solve problems and improve efficiency or satisfaction in meaningful ways.

## Privacy and Submission Guidelines
- **Submission Requirements:** Please submit a link to your public repo with your implementation or a loom video showcasing your work on the [BloomTech AI Platform](app.bloomtech.com). 
- **Sensitive Information:** If your implementation involves sensitive information, you are not required to submit a public repository. Instead, a detailed review of your project through a Loom video is acceptable, where you can demonstrate the functionality and discuss the technologies used without exposing confidential data.

## Updates and Enhancements

### Dependencies
- Added `python-dotenv` version `1.0.1` to manage environment variables securely. Ensure you have `python-dotenv` installed by adding it to your `requirements.txt` file:
  ```plaintext
  python-dotenv==1.0.1
  ```
- Updated `.gitignore` to include `.env` files to prevent sensitive information from being committed to the repository:
  ```plaintext
  venv/
  .env
  ```

### New Features
- Introduced a simple test script (`test.py`) to utilize the `ChatOpenAI` client for language translation. This script demonstrates how to load environment variables using `.env` and interact with the OpenAI API:
  ```python
  from langchain_openai import ChatOpenAI
  from langchain.schema import SystemMessage, HumanMessage, AIMessage
  from langchain_core.output_parsers.string import StrOutputParser
  import os
  from dotenv import load_dotenv
  
  # Load environment variables from .env file
  load_dotenv()
  
  # Retrieve the OpenAI API key from environment variables
  api_key = os.getenv('OPENAI_API_KEY')
  
  client = ChatOpenAI(api_key=api_key, model="gpt-4o")
  
  # Define the messages with roles
  messages = [
      SystemMessage(content="You are a translator. Translate the following English text to French."),
      HumanMessage(content="Hello, how are you?")
  ]
  
  # Generate the response from the model
  response = client.invoke(input=messages)
  parser = StrOutputParser()
  content = parser.invoke(input=response)
  
  # Print the output
  print(content)
  ```

### Utility Function Update
- Minor adjustments in `utility.py` to ensure consistency and correctness in formatting the prompt for the LLM:
  ```python
  def format_data_for_openai(diffs, readme_content, commit_messages):
      readme_content = base64.b64decode(readme_content.content).decode("utf-8")
  
      # Construct the prompt with clear instructions for the LLM.
      prompt = (
          "Please review the following code changes and commit messages from a Github pull request:\n"
          "Code Changes:\n"
          f"{changes}\n"
          "Commit Messages:\n"
          f"{commit_messages}\n"
          "Consider the code changes and commit messages to update the README.md file with the necessary information, ensuring to maintain the style and clarity of the README.md.\n"
          "Ensure the README.md is formatted using markdown syntax.\n"
          "Updated README.md:\n"
      )
  
      return prompt
  ```

By following these updates, you can ensure that your project remains up-to-date with the latest enhancements and security practices.