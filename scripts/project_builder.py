#! /usr/bin/python3
import os

"""
A simple function that creates a project structure with, src, tests, build,
docs as folders.

As files it adds README.md and .gitignore.
"""
def build():
    path = input("Location path: ")
    project_name = input("Project name: ")
    license = input("License for project: ")
    
    folders = ['src', 'tests', 'build', 'docs']

    files = {
        "README.md": f"# {project_name}\n",
        "LICENSE": f"{license}\n",
        ".gitignore": "# Binary\n\n*build\n"
    }

    try:
        os.chdir(path)
        os.mkdir(project_name)
        os.chdir(f"{path}/{project_name}")

        for folder in folders:
            os.mkdir(folder)

        for name, content in files.items():
            with open(name, "w") as f:
                f.write(content)

        print(f"Project '{project_name}' created successfully")

    except FileExistsError:
        print(f"Project '{project_name}' already exists")

    except PermissionError:
        print(f"Permission to create '{project_name}' denied")

    except Exception as e:
        print(f"An error occured: {e}")
        

build()