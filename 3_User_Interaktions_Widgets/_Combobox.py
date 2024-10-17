import tkinter as tk
from tkinter import ttk

def show_selection(event):
    label.config(text=f"Ausgewählt: {combobox.get()}")

root = tk.Tk()
root.title("Combobox Demonstration")
root.geometry("300x200")

combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.pack(pady=20)
combobox.bind("<<ComboboxSelected>>", show_selection)

label = tk.Label(root, text="Wähle eine Option")
label.pack(pady=10)

root.mainloop()
