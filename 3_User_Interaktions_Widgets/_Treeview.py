import tkinter as tk
from tkinter import ttk

def show_selection(event):
    selected_item = tree.selection()
    if selected_item:
        label.config(text=f"Ausgewählt: {tree.item(selected_item)['text']}")

root = tk.Tk()
root.title("Treeview Demonstration")
root.geometry("400x300")

tree = ttk.Treeview(root)
tree.pack(pady=20)

tree.insert("", "end", text="Element 1")
tree.insert("", "end", text="Element 2")
tree.insert("", "end", text="Element 3")

tree.bind("<<TreeviewSelect>>", show_selection)

label = tk.Label(root, text="Wähle ein Element aus dem Baum")
label.pack(pady=10)

root.mainloop()
