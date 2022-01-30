# this code works

import os
import tkinter as tk
from tkinter import filedialog


class FileDialogue:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()

        self.file_path = filedialog.askopenfilename()

        self.file = open(self.file_path, "r+b")

    def get_file_path(self):
        return self.file_path

    def get_file_length(self):
        return os.path.getsize(self.file_path)

    def get_file_data(self):
        result = []
        original = self.file.readlines()
        for bytes in original:
            for byte in list(bytes.decode()):
                result.append(byte.encode())
        return result

    def get_file_ext(self):
        return self.file_path[self.file_path.index(".") :]

    def close(self):
        self.file.close()
