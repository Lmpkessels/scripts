#!/usr/bin/env python3

import subprocess
from pathlib import Path


def run(*cmd):
    subprocess.run(cmd, check=True)


def git_push():
    if not (Path(".git")).exists():
        print("Initializing Git repository...")
        run("git", "init")

    print("\n=== Git Status ===")
    run("git", "status")

    files = input("\nFiles to commit (. for all): ").strip()
    if not files:
        return

    message = input("Commit message: ").strip()
    if not message:
        return

    run("git", "add", *files.split())
    run("git", "commit", "-m", message)
    run("git", "push")

    print("\nPush complete.")


if __name__ == "__main__":
    git_push()
