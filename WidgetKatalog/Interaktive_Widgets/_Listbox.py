import tkinter as tk

def show_selection(event):
    selected = listbox.curselection()
    if selected:
        label.config(text=f"Ausgewählt: {listbox.get(selected)}")

root = tk.Tk()
root.title("Listbox Demonstration")
root.geometry("300x200")

listbox = tk.Listbox(root)
items = ["Element 1", "Element 2", "Element 3"]
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(pady=20)

listbox.bind("<<ListboxSelect>>", show_selection)

label = tk.Label(root, text="Wähle ein Element aus der Liste")
label.pack(pady=10)

root.mainloop()
