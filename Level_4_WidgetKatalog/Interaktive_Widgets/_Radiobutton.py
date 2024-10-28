import tkinter as tk

def show_choice():
    label.config(text=f"Ausgewählt: {var.get()}")

root = tk.Tk()
root.title("Radiobutton Demonstration")
root.geometry("300x200")

var = tk.StringVar(value="Option 1")

radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1", command=show_choice)
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2", command=show_choice)

radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)

label = tk.Label(root, text="Wähle eine Option")
label.pack(pady=10)

root.mainloop()
