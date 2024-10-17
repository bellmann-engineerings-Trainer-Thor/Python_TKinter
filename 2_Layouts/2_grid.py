import tkinter as tk


root = tk.Tk()
root.title("Grid Layout")
root.geometry("400x400")



tk.Button(root, text="Row 0, Col 0").grid(row=0, column=0)
tk.Button(root, text="Row 0, Col 2").grid(row=0, column=1)
tk.Button(root, text="Row 0, Col 3").grid(row=0, column=2)
tk.Button(root, text="Row 2, Col 1").grid(row=1, column=0)
tk.Button(root, text="Row 2, Col 2").grid(row=1, column=1)
tk.Button(root, text="Row 2, Col 3").grid(row=1, column=2)

tk.Button(root, text="columnspan=2", width=20).grid(row=2, column=0,columnspan=2)
tk.Button(root, text="columnspan=3", width=30).grid(row=3, column=0, columnspan=3)



root.mainloop()