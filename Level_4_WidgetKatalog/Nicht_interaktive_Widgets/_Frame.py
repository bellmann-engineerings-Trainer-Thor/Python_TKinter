import tkinter as tk

root = tk.Tk()
root.title("Frame Demonstration")

# Einfaches Frame
frame1 = tk.Frame(root, width=200, height=100, bg="red")
frame1.pack()

# Frame mit einem anderen Hintergrund und einer Border
frame2 = tk.Frame(root, width=200, height=100, bg="blue", bd=5, relief="sunken")
frame2.pack()

root.mainloop()
