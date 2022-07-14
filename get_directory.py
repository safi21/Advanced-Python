"""   Write a code to find all files of a given path.   """

import os

def get_files_and_dirs(path):
    files = []
    dirs = []

    with os.scandir(path) as it:
        for entry in it:
            if entry.name.startswith("."):
                continue
            if entry.is_dir():
                dirs.append(entry.path)
            elif entry.is_file():
                files.append(entry.path)
    return files, dirs

def traverse_dir(path):
    all_files = []
    all_dirs = [path]
    while len(all_dirs) > 0:
        current_dir = all_dirs.pop(0)
        try:
            files, dirs = get_files_and_dirs(current_dir)
            all_files.extend(files)
            all_dirs.extend(dirs)
        except PermissionError:
            print('Access is denied')
    return all_files

if __name__ == "__main__":
    path = input("Enter a path: ")
    files = traverse_dir(path)
    python_files = [file for file in files if file.endswith(".py")]
    #print(files)
    print(python_files)
    print(len(python_files))
    print(len(files))