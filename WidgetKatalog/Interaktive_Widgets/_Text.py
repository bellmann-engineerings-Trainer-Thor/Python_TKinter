import tkinter as tk

def show_text():
    label.config(text=f"Eingegeben: {text.get('1.0', tk.END).strip()}")

root = tk.Tk()
root.title("Text Demonstration")
root.geometry("400x300")

text = tk.Text(root, height=5, width=30)
text.pack(pady=20)

button = tk.Button(root, text="Anzeigen", command=show_text)
button.pack()

label = tk.Label(root, text="Gib etwas ein und klicke auf 'Anzeigen'")
label.pack(pady=10)

root.mainloop()
