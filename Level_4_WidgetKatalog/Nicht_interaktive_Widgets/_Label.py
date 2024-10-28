import tkinter as tk

root = tk.Tk()
root.title("Label Demonstration")

# Einfaches Label
label1 = tk.Label(root, text="Einfaches Label")
label1.pack()

# Label mit geändertem Hintergrund und Schriftart
label2 = tk.Label(root, text="Label mit Stil", bg="yellow", fg="blue", font=("Helvetica", 16, "bold"))
label2.pack()

root.mainloop()
