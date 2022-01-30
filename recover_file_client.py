import socket
from open_file_dialogue_test import FileDialogue

# get instruction file
f = FileDialogue()
data = f.get_file_data()
ext = f.get_file_ext()
path = f.get_file_path()
f.close()
