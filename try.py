from tkinter import filedialog
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # hi there
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        # file piker
        self.file_pik = tk.Button(self)
        self.file_pik["text"] = "Choose a file"
        self.file_pik["command"] = self.file_chooser
        self.file_pik.pack(side="bottom")

        # exit
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def file_chooser(self):
        fname = filedialog.askopenfilename(initialdir='.',
                                            title='Select file', 
                                            filetypes=(('Audit files', '*.audit'), ('all files', '*.*')))
        print(fname)


root = tk.Tk(className='Security app')
root.geometry("1000x500")
# root.filename =  filedialog.askopenfilename( initialdir = "/", title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

app = Application(master=root)
app.mainloop()
