import tkinter as tk


root = tk.Tk()
root.title("Place Layout")
root.geometry("400x400")



tk.Button(root, text="Button 1").place(x=50, y=50)
tk.Button(root, text="Button 2").place(x=123, y=321)
tk.Button(root, text="Button 3").place(x=258, y=1)



root.mainloop()