from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "MoonSyntax"
REPO_NAME = "firstrepo"
PR_NUMBER = 1  # Change to the actual PR number

def get_code_diff():
    """Fetches code differences from a pull request."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{PR_NUMBER}/files"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch PR data:", response.json())
        return []

    files_changed = response.json()
    modified_files = [file["filename"] for file in files_changed]
    
    return modified_files

if __name__ == "__main__":
    changed_files = get_code_diff()
    print("Changed files:", changed_files)
