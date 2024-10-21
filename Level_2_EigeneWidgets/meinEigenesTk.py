import tkinter as tk
from meinEigenerFrame import MeinEigenderFrame

class MeinEigensTk(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
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
        custom_frame = MeinEigenderFrame(self.child_space, text=f"Komponente {self.component_count}")
        custom_frame.pack(fill="x", pady=5)


if __name__ == "__main__":
    app = MeinEigensTk()
    app.mainloop()
