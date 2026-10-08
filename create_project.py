from pathlib import Path

#for the current working directory
root =  Path(".")

#for the folders to create
folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests"
]

#for the files to create
files = [
    "app/main.py",
    "ingest_sample_kb.py",
    "requirements.txt",
    "run.py",
    ".env"
]

#Create the folders
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

#Create the files
for file in files:
    (root / file).touch(exist_ok=True)

print("Project structure created successfully.")