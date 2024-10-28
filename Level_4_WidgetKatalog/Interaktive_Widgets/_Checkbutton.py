import tkinter as tk

def show_choice():
    label.config(text=f"Ausgewählt: {'Ja' if var.get() else 'Nein'}")

root = tk.Tk()
root.title("Checkbutton Demonstration")
root.geometry("300x200")

var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Option auswählen", variable=var, command=show_choice)
checkbutton.pack(pady=20)

label = tk.Label(root, text="Wähle eine Option")
label.pack(pady=10)

root.mainloop()
