import tkinter as tk

root = tk.Tk()
root.title("Canvas Demonstration")

# Canvas erstellen
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Formen zeichnen
canvas.create_line(0, 0, 200, 100, fill="blue", width=5)
canvas.create_rectangle(50, 50, 150, 150, fill="red", outline="black", width=3)

root.mainloop()
