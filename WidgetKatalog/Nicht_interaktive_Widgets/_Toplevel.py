import tkinter as tk

def create_toplevel():
    toplevel = tk.Toplevel()
    toplevel.title("Neues Fenster")
    label = tk.Label(toplevel, text="Dies ist ein neues Toplevel-Fenster.")
    label.pack()

root = tk.Tk()
root.title("Toplevel Demonstration")

button = tk.Button(root, text="Neues Fenster öffnen", command=create_toplevel)
button.pack()

root.mainloop()
