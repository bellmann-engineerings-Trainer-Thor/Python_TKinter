import tkinter as tk

# Erstelle das Hauptfenster
root = tk.Tk()

# Setze den Titel des Fensters
root.title("Tkinter Fenster")

# Setze die Größe und Position des Fensters
root.geometry("800x600")

# Setze die Mindest- und Maximalgröße
root.minsize(400, 300)
root.maxsize(1024, 768)

# Ändere die Hintergrundfarbe
root.configure(bg='lime')      #mehr farben gibts in der Dokumentation https://www.tcl.tk/man/tcl/TkCmd/colors.html
root.configure(bg='#3adad7')

# Starte die Hauptschleife
root.mainloop()
