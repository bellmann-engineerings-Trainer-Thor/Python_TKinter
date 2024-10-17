import tkinter as tk

root = tk.Tk()
root.title("Scrollbar Demonstration")

# Textfeld erstellen
text = tk.Text(root, wrap="none", width=40, height=10)
text.pack(side="left")

# Scrollbar erstellen
scrollbar = tk.Scrollbar(root, orient="vertical", command=text.yview)
scrollbar.pack(side="right", fill="y")

# Scrollbar mit Textfeld verbinden
text.configure(yscrollcommand=scrollbar.set)

# Beispieltext einfügen
for i in range(50):
    text.insert("end", f"Zeile {i+1}\n")

root.mainloop()
