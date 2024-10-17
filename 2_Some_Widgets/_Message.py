import tkinter as tk

root = tk.Tk()
root.title("Message Demonstration")

# Message erstellen
message = tk.Message(root, text="Dies ist ein längerer Text, der in mehreren Zeilen umgebrochen wird.", width=200)
message.pack()

# Message mit anderem Stil
message2 = tk.Message(root, text="Ein stilisiertes Message-Widget.", width=200, bg="lightblue", font=("Arial", 14))
message2.pack()

root.mainloop()
