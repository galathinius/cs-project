import tkinter as tk
from func import update_content, get_chosen
import time
from threading import Event

def enforce_it_button():
    enforce_it = tk.Button()
    enforce_it["command"] = lambda: enforce_them('params')
    enforce_it["text"] = "enforce"
    enforce_it["width"] = "20"
    enforce_it.grid(row=0, column=2)

def enforce_them(params):
    chosen = get_chosen()
    to_pop_up = ''
    for one in chosen:
        to_pop_up = f'{to_pop_up}\n{chosen[one]["description"]}.........Done'
    
    # popupmsg('enforcin')
    popupmsg(to_pop_up)
    

def popupmsg(msg):
    LARGE_FONT= ("Verdana", 12)
    popup = tk.Tk()
    popup.wm_title("!")
    label0 = tk.Label(popup, text='Thanks for waiting\n The following have been enforced:', font=LARGE_FONT, padx=1, pady=1)
    label0.grid(row=1, column=1, columnspan=2, rowspan=4)
    label1 = tk.Label(popup, text=msg, padx=1, pady=1)
    label1.grid(row=7, column=1, columnspan=2, rowspan=4)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.grid()

    time.sleep(3)
    
    popup.mainloop()

# popupmsg('waited......................................')