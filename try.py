from tkinter import filedialog
import shutil
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # hi there
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there["width"] = "20"
        # self.hi_there.grid(row=0, column=0,
        #                       padx=10, pady=10, columnspan=2, rowspan=2,)

        # exit
        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.grid(row=0, column=10, padx=10, pady=10)
        
        # label
        self.lbl = tk.Label(text="Hello, you haven't chosen a file yet")
        self.lbl.grid(row=1, column=0, padx=10, pady=10)

        # file piker
        self.file_pik = tk.Button(self)
        self.file_pik["text"] = "Choose a file"
        self.file_pik["command"] = self.file_chooser
        self.file_pik["width"] = "20"
        self.file_pik.grid(row=2, column=1, padx=10, pady=10)

        # file saver
        self.file_save = tk.Button(self)
        self.file_save["text"] = "Save as"
        self.file_save["command"] = self.file_saver
        self.file_save["width"] = "20"
        self.file_save.grid(row=3, column=1, padx=10, pady=10)

    def say_hi(self):
        print("hi there, everyone!")

    def file_chooser(self):
        title = "seleeect"
        filetypes = (('Audit files', '*.audit'), ('all files', '*.*'))
        self.fname = filedialog.askopenfilename(initialdir='.',
                                           title=title,
                                           filetypes=filetypes)
        
        file_name = self.fname.split('/')[-1]
        self.lbl.configure(text=f"You chose\n{file_name}")
        print(self.fname)
        

    def file_saver(self):
        filename = filedialog.asksaveasfilename(initialdir = ".", title = "Select folder", defaultextension=".audit")
        if filename is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return

        shutil.copy2(self.fname, filename)
        


root = tk.Tk(className='Security app')
root.geometry("1000x500")

app = Application(master=root)
app.mainloop()
