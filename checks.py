import tkinter as tk
from random import random
import time

def make_chek(frame, index, text, r):
    var = tk.IntVar()
    rate = '________'
    color = ''
    if r:
        time.sleep(.200)
        rate = 'Success_' if random()>0.6 else 'Fail_'
    
    if rate == 'Success_':
        color = 'green'
    elif rate == 'Fail_': 
        color = 'red'
    else: color = 'black'

    tk.Checkbutton(frame, text=f'{rate}{text}', variable=var, fg = color).grid(row=index + 6, column=0)
    return var

frames = []

def make_check_list(data, r):
    print('make cek list chemat')
    if frames:
        frames.pop().grid_forget()
    frame = tk.Frame()
    frames.append(frame)
    frame.grid(row = 6, column = 0, columnspan = 20)

    list_length = min(20, len(data))
    print(list_length)
    for i in range(0, list_length):
        data[str(i)]['check'] = make_chek(frame, i, data[str(i)]['description'], r)
        
    return data  

