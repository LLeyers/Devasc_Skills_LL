from genie.testbed import load
import json
import os
from github import Github

# Function to gather facts
def gather_facts(testbed_file):
    # Load testbed file
    testbed = load(testbed_file)

    # Connect to devices and gather facts
    for device_name, device in testbed.devices.items():
        device.connect()
        facts = device.parse("show version")

        # Save facts to a JSON file
        filename = f"{device_name}_facts.json"
        with open(filename, "w") as f:
            json.dump(facts, f, indent=4)

        # Upload to GitHub
        upload_to_github(filename)

# Function to upload to GitHub
def upload_to_github(filename):
    github_token = "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"
    repo_name = "https://github.com/LLeyers/Devasc_Skills_LL.git"
    branch_name = "master"

    # Connect to GitHub
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    branch = repo.get_branch(branch_name)

    # Upload file to GitHub
    with open(filename, "r") as f:
        content = f.read()

    repo.create_file(filename, f"Add {filename}", content, branch=branch_name)

if __name__ == "__main__":
    testbed_file = "path/to/your/testbed.yaml"
    gather_facts(testbed_file)
