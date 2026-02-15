---
name: progress
description: Show progress and list next N games to add
user_invocable: true
---

# /progress

Show progress stats and return the next N games to work on.

## Instructions

1. Run `python3 scripts/progress.py <N>` using Bash. Default N is 20; use any number the user provides (e.g. `/progress 50`).
2. Display the progress stats line.
3. Return the list of next games as a structured list the user can act on — each entry should include the name, year, and source.
