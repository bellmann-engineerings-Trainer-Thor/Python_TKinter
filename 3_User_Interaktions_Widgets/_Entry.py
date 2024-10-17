import tkinter as tk

def show_text(event):
    label.config(text=f"Eingegeben: {entry.get()}")

root = tk.Tk()
root.title("Entry Demonstration")
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack(pady=20)
entry.bind("<Return>", show_text)

label = tk.Label(root, text="Gib etwas ein und drücke Enter")
label.pack(pady=10)

root.mainloop()
