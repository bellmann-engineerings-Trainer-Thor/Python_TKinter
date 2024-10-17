import tkinter as tk


class MeineErsteKomponente(tk.Frame):
    def __init__(self, master=None, text="", **kwargs):
        super().__init__(master, **kwargs)

        # Label
        self.label = tk.Label(self, text=text)
        self.label.pack(side="left", padx=10, pady=10)

        # Lösch-Button
        self.delete_button = tk.Button(self, text="Delete", command=self.delete_self)
        self.delete_button.pack(side="right", padx=10, pady=10)

    def delete_self(self):
        self.destroy()