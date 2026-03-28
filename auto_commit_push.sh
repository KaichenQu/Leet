#!/bin/bash
# Auto commit & push LeetCode solutions if there are changes
# Adds some randomness to the timing (0-8 min delay)

REPO_DIR="/Users/kelsonqu/Desktop/Leet"
cd "$REPO_DIR" || exit 1

# Random delay 0-480 seconds (0-8 min) to avoid exact times
sleep $((RANDOM % 480))

# Check if there are any changes (new/modified files)
if git status --porcelain | grep -q .; then
    # Regenerate README from .py files
    python3 "$REPO_DIR/generate_readme.py"

    # Stage .py files + README
    git add *.py README.md

    # Count new/modified files for commit message
    ADDED=$(git diff --cached --name-only --diff-filter=A -- '*.py' | wc -l | tr -d ' ')
    MODIFIED=$(git diff --cached --name-only --diff-filter=M -- '*.py' | wc -l | tr -d ' ')
    FILES=$(git diff --cached --name-only -- '*.py')

    # Build commit message from changed files
    if [ "$ADDED" -gt 0 ] && [ "$MODIFIED" -gt 0 ]; then
        MSG="add ${ADDED} new solution(s), update ${MODIFIED} file(s)"
    elif [ "$ADDED" -gt 0 ]; then
        NAMES=$(echo "$FILES" | head -3 | sed 's/\.py$//' | sed 's/^[0-9]*\.//' | sed 's/-/ /g' | tr '\n' ', ' | sed 's/,$//')
        MSG="add: ${NAMES}"
    elif [ "$MODIFIED" -gt 0 ]; then
        NAMES=$(echo "$FILES" | head -3 | sed 's/\.py$//' | sed 's/^[0-9]*\.//' | sed 's/-/ /g' | tr '\n' ', ' | sed 's/,$//')
        MSG="update: ${NAMES}"
    else
        MSG="update solutions"
    fi

    git commit -m "$MSG"
    git push origin main 2>/dev/null || git push origin master 2>/dev/null
fi
