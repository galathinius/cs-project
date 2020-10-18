import tkinter as tk
from func import file_label, file_piker_button, file_saver_button
from search_bar import search_button
from check_it import check_it_button
from enforce import enforce_it_button

def quit():
    quit = tk.Button(text="QUIT", fg="red",
                     command=root.destroy)
    quit.grid(row=0, column=10, padx=10, pady=10)


root = tk.Tk()
root.title("Security app")
root.geometry("800x500")

file_label()
search_button()
file_piker_button()
file_saver_button()
check_it_button()
enforce_it_button()
quit()


root.mainloop()
