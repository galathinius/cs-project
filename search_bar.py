import tkinter as tk
import json
import re
from func import get_all_data, update_content
# from daniela import make_check_list

#------------------------- SEARCH
def search_entry():
    entry = tk.Entry () 
    entry.grid(row=1, column=0)
    return entry

def getSearch(entry):
    entry_data = entry.get()
    all_data = get_all_data()
    search_result = {}
    search_len = 0
    for key in all_data:
        if re.search(entry_data, all_data[key]['description']):
            search_result[str(search_len)] = all_data[key]
            search_len+=1
    update_content(search_result)

def search_button():
    entry = search_entry()
    search_button = tk.Button()
    search_button["command"] = lambda: getSearch(entry)
    search_button["text"] = "Search"
    search_button["width"] = "20"
    search_button.grid(row=1, column=1)
