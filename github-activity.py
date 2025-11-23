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
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        else:
            print(f"Error: Github API returned {e.code}")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    
    if not data:
        print(f"No recent activity found for {username}")
        return
    
    print(f"\n Recent Activity for {username}")

    for event in data:
        event_type = event['type']
        repo_name = event['repo']['name']

        if event_type == 'PushEvent':
            payload = event.get('payload', {})
            commit_count = len(payload.get('commits', []))
            print(f"- Pushed {commit_count} commits to {repo_name}")

        elif event_type == 'IssuesEvent':
            action = event['payload']['action']
            print(f" -{action.capitalize()} an issue in {repo_name}")

        elif event_type == 'WatchEvent':
            print(f"- Starred {repo_name}")

        elif event_type == 'CreateEvent':
            ref_type = event['payload']['ref_type']
            print(f"- Created a new {ref_type} in {repo_name}")
        
        elif event_type == 'ForkEvent':
            print(f"- Forked {repo_name}")

        elif event_type == 'MemberEvent':
            print(f"- A Member event in {repo_name}")

        else:
            print(f" - {event_type.replace('Event', '')} activity in {repo_name}")


if __name__ == "__main__":
    main() 

