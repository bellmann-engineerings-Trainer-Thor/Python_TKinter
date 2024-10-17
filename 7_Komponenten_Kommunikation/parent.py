import tkinter as tk
from child import Child


class Parent(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Komponenten Kommunkation")

        # Liste zur Aufbewahrung der Child-Frames
        self.children_widgets = []
        self.child_counter = 0

        # Frame zum Anzeigen der Komponenten
        self.child_space = tk.Frame(master=self)
        self.child_space.pack(pady=20)

        # Button zum Hinzufügen neuer Komponenten
        self.add_button = tk.Button(self, text="Komponente hinzufügen", command=self.add_child)
        self.add_button.pack(pady=10)

        # Button zum Senden einer Nachricht an alle Kinder
        self.notify_button = tk.Button(self, text="Notify All Children", command=self.notify_all_children)
        self.notify_button.pack(pady=10)

        # Label zum Anzeigen von Nachrichten vom Child
        self.message_label = tk.Label(self, text="")
        self.message_label.pack(pady=10)


    def receive_message_from_child(self, message):
        # Aktualisiere das Label mit der Nachricht vom Child
        self.message_label.config(text=message)

    def add_child(self):
        # pass

        self.child_counter += 1

        # *******************************************************************
        # im Konstruktoraufruf wird die Parent-Methode "receive_message_from_child"
        # als Argument an das Child übergeben
        # *******************************************************************
        child = Child(
            self.child_space,
            text=f"Child {self.child_counter}",
            parent_callback=self.receive_message_from_child     # <- hier wird die Parent-Methode übergeben
        )
        child.pack(fill="x", pady=5)

        self.children_widgets.append(child)

    def notify_all_children(self):
        # Aktualisiere das Label in allen Child-Frames
        for frame in self.children_widgets:
            frame.receive_message_from_parent("Updated by Parent!")



if __name__ == "__main__":
    app = Parent()
    app.mainloop()
