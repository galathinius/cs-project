from func import *
from search_bar import search_button

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
quit()


root.mainloop()
