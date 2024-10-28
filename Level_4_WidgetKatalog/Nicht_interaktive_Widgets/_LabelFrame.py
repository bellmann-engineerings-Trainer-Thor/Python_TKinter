import tkinter as tk

root = tk.Tk()
root.title("LabelFrame Demonstration")

# LabelFrame erstellen
labelframe = tk.LabelFrame(root, text="LabelFrame Beispiel", padx=10, pady=10)
labelframe.pack(padx=10, pady=10)

# Inhalt in LabelFrame
label = tk.Label(labelframe, text="Inhalt innerhalb eines LabelFrames")
label.pack()

root.mainloop()
