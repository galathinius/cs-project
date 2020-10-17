from tkinter import filedialog
import shutil
import tkinter as tk
import json
from checks import make_check_list
from parsing import parse

# global_data = {}

def get_chosen():
    data_to_filter = get_all_data()
    data_to_return = {}
    data_len = 0
    for item in data_to_filter:
        if 'check' in data_to_filter[item]:
            if data_to_filter[item]['check'].get():
                data_to_return[str(data_len)] = data_to_filter[item]
                data_len+=1

    return data_to_return

def get_converted_data():
    # print('converting')
    data_to_convert = get_chosen()
    data_to_return = ''
    for item in data_to_convert:
        data_to_return = f'{data_to_return}\n<custom_item>\n'
        for key in data_to_convert[item]:
            data_to_return = f'{data_to_return}{key}:{data_to_convert[item][key]}\n'
        data_to_return = f'{data_to_return}</custom_item>\n'
    return data_to_return

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
    ma_file = open('parsed.json', "r")
    file_data = ma_file.read()
    global_data = json.loads(file_data)
    text_to_add = f"You chose:\n{file_name}\n\nThese are the tests:"
    update_file_label(text_to_add)
    update_content(global_data)
    ma_file.close()

def update_content(data, r = None):
    global global_data
    global_data = make_check_list(data, r)
    return global_data
    
def file_chooser():
    title = "seleeect"
    filetypes = (('Audit files', '*.audit'), ('all files', '*.*'))
    
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

def save_data_to_file(filename):
    data_to_save = get_converted_data()
    f2 = open(filename, "w")
    f2.write(data_to_save)
    f2.close()

def file_saver():
    filename = filedialog.asksaveasfilename(
        initialdir=".", title="Select folder", defaultextension=".audit")
    if filename is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return

    save_data_to_file(filename)

def file_saver_button():
    file_save = tk.Button()
    file_save["text"] = "Save as"
    file_save["command"] = file_saver
    file_save["width"] = "20"
    file_save.grid(row=0, column=1, padx=10, pady=10)


