import tkinter as tk


root = tk.Tk()
root.title("Security app")
root.geometry("800x500")

info = [['apple', 'oramge', 'pear'],[]*3]


def make_chek(index, text):
    var = tk.IntVar()
    tk.Checkbutton(text=text, variable=var).grid(row=index, column=1)
    return var

def make_check_list(data):
    for i in range(0, len(data[0])):
        data[1].append(make_chek(i, data[0][i])) 
    return data  

def show_chosen(cheks):
    the_chosen = tk.Label()
    the_chosen.grid(row=7, column=0, padx=10, pady=10,
                           columnspan=2, rowspan=2,)
    
    text_to_add = f"You chose:\n"
    for i in range(0, len(cheks[0])):
        if cheks[1][i].get():
            text_to_add += cheks[0][i]
            text_to_add += '\n'

    the_chosen.configure(text=text_to_add)

def what_did_i_choose_button(my_list):
    
    chosen = tk.Button()
    chosen["text"] = "what did I choose?"
    chosen["command"] = lambda: show_chosen(my_list)
    chosen["width"] = "50"
    chosen.grid(row=0, column=5,
                  padx=10, pady=10, columnspan=2, rowspan=2,)

the_list = make_check_list(info)
what_did_i_choose_button(the_list)


root.mainloop()