# main.py
from pathlib import Path
import os


# renames all files using the list of filenames, while retaining the file extension
def rename_files(filenames: list[str], files: list[str]) -> None:
    if len(filenames) != len(files):
        raise Exception("Not the same amount of files as filenames")

    for i, file in enumerate(files):
        path = Path(file)
        new_path = os.path.join(path.parent, filenames[i], path.suffix)
        os.rename(file, new_path)


