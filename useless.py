import tkinter as tk


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
