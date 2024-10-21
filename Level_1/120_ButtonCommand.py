import tkinter as tk
from functools import partial

# Direkte Zuweisung einer Funktion
def update_label(label):
    label.config(text="update_label ausgeführt")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Erweiterte Button Demo")

# Label erstellen
meinLabel = tk.Label(root, text="Kein Button wurde gedrückt", font=('Arial', 14))
meinLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Button 1 (direkte Zuweisung der Funktion)
button1 = tk.Button(root, text="Funktion benutzen", command=lambda:  update_label(meinLabel))
button1.grid(row=1, column=0, padx=10, pady=10)

# Button mit direkter Lambda-Funktion
button2 = tk.Button(root, text="Lamda benutzen", command=lambda: meinLabel.config(text="Lambda-Funktion direkt genutzt"))
button2.grid(row=1, column=1, padx=10, pady=10)

# Hauptfenster starten
root.mainloop()
