import tkinter as tk
from MyOwnTk import *
# from Python_TKinter.demo import MyOwnTK


class MyOwnFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, text="", **kw):
        super().__init__(master=None, cnf={}, **kw)
        self.label = tk.Label(self, text=text)
        self.label.pack()

        self.button = tk.Button(self, text="delete", command=self.delete_self)
        self.button.pack()
    def delete_self(self):
        self.destroy()


# if __name__ == "__main__":
# root = MyOwnTK()
# myWidget = MyOwnFrame(master=root, text="Hier bin ich")
# myWidget.pack()
# root.mainloop()