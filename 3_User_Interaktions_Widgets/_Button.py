import tkinter as tk

def on_click():
    label.config(text="Button wurde geklickt!")

root = tk.Tk()
root.title("Button Demonstration")
root.geometry("300x200")

button = tk.Button(root, text="Klick mich", command=on_click)
button.pack(pady=20)

label = tk.Label(root, text="Wähle eine Aktion")
label.pack(pady=10)

root.mainloop()
