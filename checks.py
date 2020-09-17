import tkinter as tk


def make_chek(frame, index, text):
    var = tk.IntVar()
    tk.Checkbutton(frame, text=text, variable=var).grid(row=index + 6, column=0)
    return var

frames = []

def make_check_list(data):
    print('make cek list chemat')
    if frames:
        frames.pop().grid_forget()
        # .destroy()
    # except:
    #     print('')
        # frames.pop()
    frame = tk.Frame()
    frames.append(frame)
    frame.grid(row = 6, column = 0, columnspan = 20)

    list_length = min(20, len(data))
    print(list_length)
    for i in range(0, list_length):
        data[str(i)]['check'] = make_chek(frame, i, data[str(i)]['description'])
        
    return data  

