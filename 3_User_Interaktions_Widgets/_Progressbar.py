import tkinter as tk
from tkinter import ttk

def start_progress():
    progressbar.start(10)
    label.config(text="Fortschritt läuft...")

def stop_progress():
    progressbar.stop()
    label.config(text="Fortschritt gestoppt")

root = tk.Tk()
root.title("Progressbar Demonstration")
root.geometry("400x200")

progressbar = ttk.Progressbar(root, length=200, mode="indeterminate")
progressbar.pack(pady=20)

start_button = ttk.Button(root, text="Start", command=start_progress)
start_button.pack(pady=5)

stop_button = ttk.Button(root, text="Stop", command=stop_progress)
stop_button.pack(pady=5)

label = tk.Label(root, text="Klicke auf Start, um den Fortschritt zu sehen")
label.pack(pady=10)

root.mainloop()
