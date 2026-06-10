import json
from datetime import datetime

# LOAD DATA
with open("data/normalized_commits.json") as f:
    commits = json.load(f)

with open("data/normalized_workflows.json") as f:
    workflows = json.load(f)

print("\n===== METRICS =====\n")

# COMMITS METRIC
print(f"Total commits: {len(commits)}")

# WORKFLOW METRICS
total_runs = len(workflows)
successful_runs = [w for w in workflows if w.get("conclusion") == "success"]
failed_runs = [w for w in workflows if w.get("conclusion") == "failure"]

print(f"Total workflow runs: {total_runs}")
print(f"Successful runs: {len(successful_runs)}")
print(f"Failed runs: {len(failed_runs)}")

if total_runs > 0:
    success_rate = (len(successful_runs) / total_runs) * 100
    print(f"Success rate: {success_rate:.2f}%")
else:
    print("No workflow runs available for success rate")

# PIPELINE DURATION
durations = []

for w in workflows:
    created = w.get("created_at")
    updated = w.get("updated_at")

    if created and updated:
        start = datetime.fromisoformat(created.replace("Z", "+00:00"))
        end = datetime.fromisoformat(updated.replace("Z", "+00:00"))
        duration = (end - start).total_seconds()
        durations.append(duration)

if durations:
    avg_duration = sum(durations) / len(durations)
    print(f"Average pipeline duration (seconds): {avg_duration:.2f}")
else:
    print("No duration data available")

print("\n✅ Metrics generated\n")