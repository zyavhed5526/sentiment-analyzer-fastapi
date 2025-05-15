import os

def list_current_dir():
    entries = os.listdir('.')  # list of files and folders in current dir
    for entry in entries:
        if os.path.isdir(entry):
            print(f"Folder: {entry}")
        else:
            print(f"File: {entry}")

if __name__ == "__main__":
    list_current_dir()
