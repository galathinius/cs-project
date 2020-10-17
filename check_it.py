import tkinter as tk
from func import update_content, get_chosen


def check_it_button():
    check_it_button = tk.Button()
    check_it_button["command"] = lambda: chek_them('something')
    check_it_button["text"] = "See if used"
    check_it_button["width"] = "20"
    check_it_button.grid(row=1, column=2)

def chek_them(params):
    chosen = get_chosen()
    print('chosen '+ str(len(chosen)))
    updated = update_content(chosen, r=True)

    # pass