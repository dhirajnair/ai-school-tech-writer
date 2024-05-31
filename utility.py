import os
import base64
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers.string import StrOutputParser
from github import Github

def format_data_for_openai(diffs, readme_content, commit_messages):
    prompt = None

    # Combine the changes into a string with clear delineation.
    changes = "\n".join(
        f'File: {file["filename"]}\nDiff:\n{file["patch"]}\n'
        for file in diffs
    )

    # Combine all commit messages
    commit_messages = "\n".join(commit_messages) + "\n\n"

    # Decode the README content
    readme_content = base64.b64decode(readme_content.content).decode("utf-8")

    # Construct the prompt with clear instructions for the LLM.
    prompt = {
        "Please review the following code changes and commit messages from a Github pull request:\n"
        "Code Changes:\n"
        f"{changes}\n"
        "Commit Messages:\n"
        f"{commit_messages}\n"
        "Here is the current README.md:\n"
        f"{readme_content}\n"
        "Consider the code changes and commit messages to update the README.md file with the necessary information, ensuring to maintain the style and clarity of the README.md.\n"
        "Ensure the README.md is formatted using markdown syntax.\n"
        "Updated README.md:\n"
    }

    return prompt

def call_openai(prompt):
    client = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0, model_name="gpt-4o")
    try:
        # Correct the structure of the 'messages' to match the expected format by OpenAI API
        messages = [
            {"role": "system", "content": "You are an AI trained to update README.md files based on the code changes and commit messages from a Github pull request."},
            {"role": "user", "content": prompt}
        ]
        response = client.invoke(input=messages)
        parser = StrOutputParser()
        content = parser.invoke(input=response)
        return content
    except Exception as e:
        print(f"Error making an LLM call: {e}")
        return None

def update_readme_and_create_pr(repo, updated_readme, readme_sha):
    commit_message = "Proposed README.md update"
    commit_sha = os.getenv("COMMIT_SHA")
    main_branch = repo.get_branch("main")
    new_branch_name = f'readme-update-{commit_sha[:7]}'
    new_branch = repo.create_git_ref(ref=f'refs/heads/{new_branch_name}', sha=main_branch.commit.sha)


    repo.update_file("README.md", commit_message, updated_readme, readme_sha, branch=new_branch_name)
    repo.create_pr(commit_sha, commit_message)


    pr_title = "AI PR: Proposed README.md update"
    pr_body = "This is the proposed update to the README.md file."
    pull_request = repo.create_pull(title=pr_title, body=pr_body, head=new_branch_name, base="main")

    return pull_request