import tkinter as tk

def show_value():
    label.config(text=f"Ausgewählter Wert: {spinbox.get()}")

root = tk.Tk()
root.title("Spinbox Demonstration")
root.geometry("300x200")

spinbox = tk.Spinbox(root, from_=0, to=10, command=show_value)
spinbox.pack(pady=20)

label = tk.Label(root, text="Wähle einen Wert")
label.pack(pady=10)

root.mainloop()
