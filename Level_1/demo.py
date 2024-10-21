import tkinter as tk


def update_label(label):
    label.config(text="update_label ausgeführt")

root = tk.Tk()
root.title("Button Commands")
root.geometry("400x400")

meinLabel = tk.Label(root, text="Kein Button wurde gedrückt", font=('Arial', 14))
meinLabel.grid(row=0, column=0, columnspan=3)

# direkte Zuweisung
button1 = tk.Button(root, text="Funktion benutzen", command=lambda: update_label(meinLabel))
button1.grid(row=1, column=0)

# lamda funktion
button2 = tk.Button(root, text="Lamda benutzen", command=lambda: meinLabel.config(text="Lambda Funktion ausgeführt"))
button2.grid(row=1, column=1)

root.mainloop()