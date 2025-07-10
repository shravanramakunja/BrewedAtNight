import subprocess
import sys

# Default commit message
commit_message = "push"

# If user provides a message as an argument, use that
if len(sys.argv) > 1:
    commit_message = " ".join(sys.argv[1:])

try:
    # Run Git commands
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print(" Changes pushed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error during Git operation: {e}")
