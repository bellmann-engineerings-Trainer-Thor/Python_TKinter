import tkinter as tk

root = tk.Tk()
root.title("Menubutton Demonstration")

# Menubutton erstellen
mb = tk.Menubutton(root, text="Optionen")
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu

# Optionen hinzufügen
mb.menu.add_checkbutton(label="Option 1")
mb.menu.add_checkbutton(label="Option 2")

mb.pack()

root.mainloop()
