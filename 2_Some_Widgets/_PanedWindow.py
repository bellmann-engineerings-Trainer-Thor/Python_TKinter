import tkinter as tk

root = tk.Tk()
root.title("PanedWindow Demonstration")

# PanedWindow erstellen
pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=1)

# Frames hinzufügen
left = tk.Frame(pw, bg="red", width=100, height=300)
pw.add(left)

right = tk.Frame(pw, bg="blue", width=100, height=300)
pw.add(right)

root.mainloop()
