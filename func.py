from tkinter import filedialog
import shutil
import tkinter as tk
import json
from checks import make_check_list
from parsing import parse




def file_label():

    global file_label_global

    file_label_global = tk.Label(text="Hello, you haven't chosen a file yet")
    file_label_global.grid(row=2, column=0, padx=10, pady=10,
                        columnspan=2, rowspan=4,)

def update_file_label(text):
    if 'file_label_global' in globals():
        file_label_global.configure(text=text)
    else :
        file_label()

def get_all_data():
    return global_data

def read_from_file(file_name):
    ma_file = open('parsed.json', "r").read()
    global global_data
    global_data = json.loads(ma_file)
    text_to_add = f"You chose:\n{file_name}\n\nThese are the tests:\n\n"
    update_file_label(text_to_add)
    update_content(global_data)

def update_content(data):
    make_check_list(data)

    # text_to_add = ''
    # list_length = len(data) if len(data) < 20 else 20
    # for key in range(0, list_length):
    #     text_to_add += data[str(key)]['description']
    #     text_to_add += '\n'
    # content_label = tk.Label(text=text_to_add)
    # content_label.grid(row=7, column=0, padx=10, pady=10,
    #                        columnspan=2, rowspan=2,)
    
def file_chooser():
    title = "seleeect"
    filetypes = (('Audit files', '*.audit'), ('all files', '*.*'))
    global fname
    fname = filedialog.askopenfilename(initialdir='.',
                                       title=title,
                                       filetypes=filetypes)
    file_name = fname.split('/')[-1]
    parse(fname)
    read_from_file(file_name)

def file_piker_button():
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
