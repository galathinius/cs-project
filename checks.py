import tkinter as tk


def make_chek(frame, index, text):
    var = tk.IntVar()
    tk.Checkbutton(frame, text=text, variable=var).grid(row=index + 5, column=0)
    return var

frames = []

def make_check_list(data):
    print('make cek list chemat')
    if frames:
        frames[0].destroy
        frames.pop()
    frame = tk.Frame()
    frames.append(frame)
    frame.grid(row = 3, column = 0, columnspan = 20)

    list_length = min(20, len(data))
    for i in range(0, list_length):
        data[str(i)]['check'] = make_chek(frame, i, data[str(i)]['description'])
        
    return data  

