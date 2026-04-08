import os

"""
A simple function that creates a project structure with, src, tests, build,
docs as folders.

As files it adds README.md and .gitignore.
"""
def build():
    path = input("Location path: ")
    project_name = input("Project name: ")
    
    folders = ['src', 'tests', 'build', 'docs']
    files = ['README.md', 'LICENSE','.gitignore']

    try:
        os.chdir(f"{path}")
        os.mkdir(project_name)
        os.chdir(f"{path}/{project_name}")
        for folder in folders:
            os.mkdir(folder)
        for file in files:
            #TODO: add header of project on top of README, and build
            #TODO: under # Binary in .gitignore
            open(f"{path}/{project_name}/{file}", "a").close()
        print(f"Project '{project_name}' created successfully")
    except FileExistsError:
        print(f"Project '{project_name}' already exists")
    except PermissionError:
        print(f"Permission to create '{project_name}' denied")
    except Exception as e:
        print(f"An error occured: {e}")
        

build()