# main.py
from pathlib import Path
import os
import PySimpleGUI as sg
import re

fileList: list[str]
filenameList: list[str]


# renames all files using the list of filenames, while retaining the file extension
def rename_files(filenames: list[str], files: list[str]) -> None:
    if len(filenames) != len(files):
        raise Exception("Not the same amount of files as filenames")

    for i, file in enumerate(files):
        path = Path(file)
        new_path = os.path.join(path.parent, filenames[i] + path.suffix)
        os.rename(file, new_path)


# parse filename list from string
def parse_filenames(filename_string: str) -> list[str]:
    return re.split(", |,", filename_string.replace("\n", ""))


# gui with main functionality
def gui() -> None:
    sg.theme("Dark Blue 3")
    layout = [
        [sg.Text("Welcome to file-renamepy", font="Any 18")],
        [sg.Text("Choose files to be renamed:"), sg.FilesBrowse(key="-SELECTED_FILES-", target=(None, None))],
        [sg.Text("Enter new filenames:"), sg.Multiline(key="-FILENAMES-")],
        [sg.Button("Rename Files")]
    ]
    window = sg.Window("file-renamepy", layout)
    event, values = window.read()

    # Extract values
    global fileList, filenameList
    fileList = values["-SELECTED_FILES-"].split(";")
    print("Selected files: ", fileList)
    filenameList = parse_filenames(values["-FILENAMES-"])
    print("Filenames: ", filenameList)

    # Action
    rename_files(filenameList, fileList)

    window.close()


if __name__ == "__main__":
    gui()
