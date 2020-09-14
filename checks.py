import tkinter as tk


# root = tk.Tk()
# root.title("Security app")
# root.geometry("800x500")

info = {'0': 
        {'description': 'some info'},
        '1': 
        {'description': 'other info'},
        '2': 
        {'description': 'nothing to see here'}
        }


def make_chek(index, text):
    var = tk.IntVar()
    tk.Checkbutton(text=text, variable=var).grid(row=index + 5, column=0)
    return var

def make_check_list(data):
    list_length = len(data) if len(data) < 20 else 20
    for i in range(0, list_length):
        data[str(i)]['check'] = make_chek(i, data[str(i)]['description'])
    return data  

def show_chosen(items):
    the_chosen = tk.Label()
    the_chosen.grid(row=7, column=0, padx=10, pady=10,
                           columnspan=2, rowspan=2,)
    
    text_to_add = f"You chose:\n"
    for i in range(0, len(items)):
        if items[str(i)]['check'].get():
            text_to_add += items[str(i)]['description']
            text_to_add += '\n'

    the_chosen.configure(text=text_to_add)

def what_did_i_choose_button(my_list):
    
    chosen = tk.Button()
    chosen["text"] = "what did I choose?"
    chosen["command"] = lambda: show_chosen(my_list)
    chosen["width"] = "50"
    chosen.grid(row=0, column=5,
                  padx=10, pady=10, columnspan=2, rowspan=2,)

# the_list = make_check_list(info)
# what_did_i_choose_button(the_list)


# root.mainloop()