#this code works

import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

file = open(file_path,"r+b")

#manipulate file here
file_size = os.path.getsize(file_path)
for i in range(file_size):
    print(file.read(1))

file.close()