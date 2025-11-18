import urllib.request
import json
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python github-activity.py <username>")
        return
    
    username = sys.argv[1]

    url = f"https://api.github.com/users/{username}/events"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            #print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        return

    for event in data:
        if event['type'] == 'PushEvent':
            repo_name = event['repo']['name']

            payload = event.get('payload', {})

            if 'commits' in payload:
                commit_count = len(payload['commits'])
                print(f"- Pushed {commit_count} commits to {repo_name}")
            else:
                print(f"- Pushed to {repo_name}")


if __name__ == "__main__":
    main() 

# testing
# hello

# still testing