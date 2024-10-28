import tkinter as tk

root = tk.Tk()
root.title("Menu Demonstration")

# Menüleiste erstellen
menubar = tk.Menu(root)

# Menü erstellen
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Neu")
filemenu.add_command(label="Öffnen")
filemenu.add_separator()
filemenu.add_command(label="Beenden", command=root.quit)
menubar.add_cascade(label="Datei", menu=filemenu)

# Menüleiste konfigurieren
root.config(menu=menubar)

root.mainloop()
