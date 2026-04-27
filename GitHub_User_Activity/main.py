import sys
import urllib.request
import json

BASE_URL = "https://api.github.com/users/"


def fetch_activity(username):
    url = BASE_URL + username + "/events"

    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                print("Error: Unable to fetch data")
                return None

            data = response.read()
            return json.loads(data)

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("User not found")
        else:
            print("HTTP Error:", e.code)
    except urllib.error.URLError:
        print("Network error")
    
    return None


def display_events(events):
    if not events:
        print("No activity found")
        return

    for event in events[:10]:
        event_type = event.get("type")
        repo = event.get("repo", {}).get("name", "unknown repo")

        if event_type == "PushEvent":
            commits = len(event.get("payload", {}).get("commits", []))
            print(f"- Pushed {commits} commits to {repo}")

        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action")
            print(f"- {action.capitalize()} an issue in {repo}")

        elif event_type == "WatchEvent":
            print(f"- Starred {repo}")

        elif event_type == "ForkEvent":
            print(f"- Forked {repo}")

        elif event_type == "CreateEvent":
            ref_type = event.get("payload", {}).get("ref_type")
            print(f"- Created a {ref_type} in {repo}")

        else:
            print(f"- {event_type} in {repo}")


def main():
    if len(sys.argv) < 2:
        print("Usage: github-activity <username>")
        return

    username = sys.argv[1]

    events = fetch_activity(username)

    if events:
        display_events(events)


if __name__ == "__main__":
    main()