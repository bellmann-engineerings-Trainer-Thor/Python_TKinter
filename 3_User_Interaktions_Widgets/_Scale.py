import tkinter as tk

def show_value(value):
    label.config(text=f"Wert: {value}")

root = tk.Tk()
root.title("Scale Demonstration")
root.geometry("300x200")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=show_value)
scale.pack(pady=20)

label = tk.Label(root, text="Bewege den Schieberegler")
label.pack(pady=10)

root.mainloop()
