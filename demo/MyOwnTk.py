

# # Erstelle das Hauptfenster
# root = tk.Tk()
#
# # Setze den Titel des Fensters
# root.title("Tkinter Fenster")
#
# # Setze die Größe des Fensters
# root.geometry("800x600")
#
# # Setze die Mindest- und Maximalgröße
# root.minsize(400, 300)
# root.maxsize(1024, 768)
#
# # Ändere die Hintergrundfarbe
# root.configure(bg='lime')      #mehr farben gibts in der Dokumentation https://www.tcl.tk/man/tcl/TkCmd/colors.html
# root.configure(bg='#3adad7')
#
# # Starte die Hauptschleife
# root.mainloop()

import tkinter as tk
from MyOwnFrame import *
class MyOwnTK(tk.Tk):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None, meintitel="Hallo Welt!"):
        super().__init__(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
        self.title(meintitel)

        # Setze die Größe des Fensters
        self.geometry("800x600")

        # Setze die Mindest- und Maximalgröße
        self.minsize(400, 300)
        self.maxsize(1024, 768)

        # Ändere die Hintergrundfarbe
        self.configure(bg='lime')  # mehr farben gibts in der Dokumentation https://www.tcl.tk/man/tcl/TkCmd/colors.html
        self.configure(bg='#3adad7')


        self.widgetCount = 0
        self.childspace = tk.Frame(self)
        self.childspace.pack()

        self.addButton = tk.Button(self, text="add", command=self.add_widget)
        self.addButton.pack()

    def add_widget(self):
        self.widgetCount += 1
        myWidget = MyOwnFrame(master=self.childspace, text=f"Widget nummer: {self.widgetCount}")
        myWidget.pack()


if __name__ == "__main__":
    objekt = MyOwnTK(meintitel="Hallo Universum!")
    objekt.mainloop()
