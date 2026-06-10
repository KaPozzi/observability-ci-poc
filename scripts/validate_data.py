import json

# LOAD DATA
with open("data/normalized_commits.json") as f:
    commits = json.load(f)

with open("data/normalized_workflows.json") as f:
    workflows = json.load(f)

# VALIDATE
print("\n===== DATA VALIDATION =====\n")

print(f"Total commits collected: {len(commits)}")
print(f"Total workflow runs collected: {len(workflows)}")

# Check if empty
if len(commits) == 0:
    print("⚠️ No commit data found")
else:
    print("✅ Commit data OK")

if len(workflows) == 0:
    print("⚠️ No workflow data found")
else:
    print("✅ Workflow data OK")

# Check conclusions
success_runs = [w for w in workflows if w.get("conclusion") == "success"]
failed_runs = [w for w in workflows if w.get("conclusion") == "failure"]

print(f"\nSuccessful runs: {len(success_runs)}")
print(f"Failed runs: {len(failed_runs)}")

print("\n✅ Validation completed\n")