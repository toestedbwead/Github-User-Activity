https://roadmap.sh/projects/github-user-activity

# GitHub User Activity CLI

A simple command-line interface tool to fetch and display a GitHub user's recent activity directly in your terminal.

## Features

- Fetch recent GitHub activity for any user
- Clean, formatted output of events
- Robust error handling for common issues
- No external dependencies - uses only Python standard library
- Easy to use command-line interface

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.6+ installed

## Usage

```bash
python github-activity.py <username>
```


# EXAMPLES

1. View your own activity
python github-activity.py your-username

2. View activity of popular developers
python github-activity.py torvalds
python github-activity.py kamranahmedse

3. Handle invalid users gracefully
python github-activity.py invalid-user-123


# Supported Activity Types
1. PushEvent - Commits pushed to repositories
2. IssuesEvent - Issues opened, closed, or reopened
3. WatchEvent - Repositories starred
4. CreateEvent - New repositories, branches, or tags created
5. ForkEvent - Repositories forked
6. MemberEvent - Team member activities
7. Other events - Generic fallback for any unsupported event types

# Requirements Met
1. Runs from command line with username argument
2. Fetches data from GitHub API
3. Displays formatted activity in terminal
4. Handles errors gracefully
5. No external libraries used for API calls

# Based on the roadmap.sh project: https://roadmap.sh/projects/github-user-activity