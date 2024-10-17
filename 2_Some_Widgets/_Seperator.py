import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Separator Demonstration")

# Einfache Labels
label1 = tk.Label(root, text="Oben")
label1.pack()

# Horizontaler Separator
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')

# Noch ein Label
label2 = tk.Label(root, text="Unten")
label2.pack()

root.mainloop()
