import tkinter as tk
from tkinter import ttk

def show_tab(event):
    selected_tab = notebook.tab(notebook.select(), "text")
    label.config(text=f"Ausgewählte Registerkarte: {selected_tab}")

root = tk.Tk()
root.title("Notebook Demonstration")
root.geometry("400x300")

notebook = ttk.Notebook(root)
notebook.pack(pady=20)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text="Tab 1")
notebook.add(frame2, text="Tab 2")

notebook.bind("<<NotebookTabChanged>>", show_tab)

label = tk.Label(root, text="Wähle eine Registerkarte")
label.pack(pady=10)

root.mainloop()
