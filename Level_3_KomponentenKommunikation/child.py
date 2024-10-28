import tkinter as tk

class Child(tk.Frame):

    # *******************************************************************
    # im Konstruktoraufruf wird die Parent-Methode "receive_message_from_child"
    # als Argument an das Child übergeben
    # *******************************************************************
    def __init__(self, master=None, text="", parent_callback=None, **kwargs):
        super().__init__(master, **kwargs)
        self.text = text
        self.parent_callback = parent_callback

        self.label = tk.Label(self, text=text)
        self.label.pack(side="left", padx=10, pady=10)

        self.notify_button = tk.Button(self, text="Notify Parent", command=self.notify_parent)
        self.notify_button.pack(side="right", padx=10, pady=10)

    def notify_parent(self):
        # Wenn eine Callback-Funktion vorhanden ist, rufe sie auf
        if self.parent_callback:
            self.parent_callback(f"{self.text} sagt: hi!")

    def receive_message_from_parent(self, new_text):
        self.label.config(text=f"{self.text} {new_text}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Child-Test-Applikation")


    def receive_message_from_child(message):
        print(f"Nachricht vom Kind: {message}")


    # Erzeugung eines Child-Widgets
    child = Child(root, text="Child", parent_callback=receive_message_from_child)
    child.pack(pady=20)

    root.mainloop()