from tkinter import filedialog
import shutil
import tkinter as tk
import json
from parsing import parse


def file_label():

    global file_label_global
    file_label_global = tk.Label(text="Hello, you haven't chosen a file yet")
    file_label_global.grid(row=3, column=0, padx=10, pady=10,
                           columnspan=2, rowspan=2,)


def update_label(file_name):
    ma_file = open('parsed.json', "r").read()
    data = json.loads(ma_file)
    text_to_add = f"You chose:\n{file_name}\n\nThese are the tests:\n\n"
    for key in data:
        text_to_add += data[key]['description']
        text_to_add += '\n'
    # print(text_to_add)
    file_label_global.configure(text=text_to_add)


def say_hi():
    print("hi there, everyone!")


def hello_button():
    # hi there
    hi_there = tk.Button()
    hi_there["text"] = "Hello World\n(click me)"
    hi_there["command"] = say_hi
    hi_there["width"] = "20"
    hi_there.grid(row=0, column=0,
                  padx=10, pady=10, columnspan=2, rowspan=2,)


def file_chooser():
    title = "seleeect"
    filetypes = (('Audit files', '*.audit'), ('all files', '*.*'))
    global fname
    fname = filedialog.askopenfilename(initialdir='.',
                                       title=title,
                                       filetypes=filetypes)

    file_name = fname.split('/')[-1]
    parse(fname)
    update_label(file_name)
    # file_label_global.configure(text=f"You chose:\n{file_name}")
    # print(fname)


def file_piker_button():
    # file piker
    file_pik = tk.Button()
    file_pik["text"] = "Choose a file"
    file_pik["command"] = file_chooser
    file_pik["width"] = "20"
    file_pik.grid(row=0, column=0, padx=10, pady=10)


def file_saver():
    filename = filedialog.asksaveasfilename(
        initialdir=".", title="Select folder", defaultextension=".audit")
    if filename is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return

    shutil.copy2(fname, filename)


def file_saver_button():
    file_save = tk.Button()
    file_save["text"] = "Save as"
    file_save["command"] = file_saver
    file_save["width"] = "20"
    file_save.grid(row=0, column=1, padx=10, pady=10)
