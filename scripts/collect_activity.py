import os
import requests
import json

TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = "KaPozzi"
REPO = "observability-ci-poc"

if not TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable not set.")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# EVENTS
events_url = f"https://api.github.com/repos/{OWNER}/{REPO}/events"
events = requests.get(events_url, headers=headers).json()

with open("data/raw_events.json", "w") as f:
    json.dump(events, f, indent=2)

# COMMITS
commits_url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
commits = requests.get(commits_url, headers=headers).json()

with open("data/raw_commits.json", "w") as f:
    json.dump(commits, f, indent=2)

# WORKFLOW RUNS (CI)
workflow_url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs"
workflows = requests.get(workflow_url, headers=headers).json()

with open("data/raw_workflows.json", "w") as f:
    json.dump(workflows, f, indent=2)

print("✅ Events, Commits, and Workflows collected!")