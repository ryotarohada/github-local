import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USER = os.getenv("GITHUB_USER")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

repos = [
    # Write the name of the repository you want to delete.
]
url = f"https://api.github.com/repos/{GITHUB_USER}/"
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

for repo in repos:
    r = requests.delete(url+repo, headers=headers)
    if r.status_code == 204:
        print(f"delete succeeded! {repo}")