import json

# LOAD RAW DATA
with open("data/raw_commits.json") as f:
    commits = json.load(f)

with open("data/raw_workflows.json") as f:
    workflows = json.load(f)

# NORMALIZE COMMITS
normalized_commits = []

for c in commits:
    normalized_commits.append({
        "sha": c.get("sha"),
        "author": c.get("commit", {}).get("author", {}).get("name"),
        "date": c.get("commit", {}).get("author", {}).get("date"),
        "message": c.get("commit", {}).get("message")
    })

# NORMALIZE WORKFLOWS
normalized_workflows = []

for run in workflows.get("workflow_runs", []):
    normalized_workflows.append({
        "id": run.get("id"),
        "name": run.get("name"),
        "status": run.get("status"),
        "conclusion": run.get("conclusion"),
        "created_at": run.get("created_at"),
        "updated_at": run.get("updated_at")
    })

# SAVE NORMALIZED DATA
with open("data/normalized_commits.json", "w") as f:
    json.dump(normalized_commits, f, indent=2)

with open("data/normalized_workflows.json", "w") as f:
    json.dump(normalized_workflows, f, indent=2)

print("✅ Data normalized successfully!")