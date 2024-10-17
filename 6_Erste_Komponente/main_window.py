import tkinter as tk
from meine_erste_komponente import MeineErsteKomponente

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Komponenten")

        # Zähler für die Anzahl der hinzugefügten Komponenten
        self.component_count = 0

        # Frame zum Anzeigen der Komponenten
        self.child_space = tk.Frame(self)
        self.child_space.pack(pady=20)

        # Button zum Hinzufügen neuer Custom Frames
        self.add_button = tk.Button(self, text="Komponente hinzufügen", command=self.add_component)
        self.add_button.pack(pady=10)


    def add_component(self):
        self.component_count += 1

        # Erzeuge eine Instanz von MyCustomFrame und füge sie zum Container-Frame hinzu
        custom_frame = MeineErsteKomponente(self.child_space, text=f"Komponente {self.component_count}")
        custom_frame.pack(fill="x", pady=5)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
