import tkinter as tk


root = tk.Tk()
root.title("Pack Layout")
root.geometry("400x400")



tk.Button(root, text="Top1").pack(side="top", pady=5)
tk.Button(root, text="Top2").pack(side="top", pady=5)
tk.Button(root, text="Bottom1").pack(side="bottom", pady=5)
tk.Button(root, text="Bottom2").pack(side="bottom", pady=5)
tk.Button(root, text="Left1").pack(side="left", padx=5)
tk.Button(root, text="Left2").pack(side="left", padx=5)
tk.Button(root, text="Right1").pack(side="right", padx=5)
tk.Button(root, text="Right2").pack(side="right", padx=5)



root.mainloop()