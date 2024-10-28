import tkinter as tk
from tkinter import messagebox
from Python_TKinter.Level_5_Speichern.SQLite_und_TKinter.DB_Service_Klasse import DBService
from Python_TKinter.Level_5_Speichern.SQLite_und_TKinter.Data_Widget import DataFrame
from Python_TKinter.Level_5_Speichern.SQLite_und_TKinter.Daten_Klasse import MyData

# GUI-Anwendung: MyApp, Verwaltung von Daten-Widgets
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Titel setzen
        self.title("MyData Manager with Dynamic Frames")

        # Label für Dateneingabe
        self.data_label = tk.Label(self, text="Data:")
        self.data_label.grid(row=0, column=0, padx=10, pady=10)

        # Eingabefeld für Daten
        self.data_entry = tk.Entry(self, width=40)
        self.data_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button zum Hinzufügen von Daten
        self.add_button = tk.Button(self, text="Add", command=self.__add_button_clicked)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        # Frame für die Daten-Widgets
        self.child_space = tk.Frame(self)
        self.child_space.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Liste der vorhandenen Daten-Widgets
        self.childs = []
        for data in DBService().fetchall():
            self.__add_child(data)

    # Hinzufügen-Button geklickt
    def __add_button_clicked(self):
        user_input = self.data_entry.get()                          # Eingabe holen
        if user_input:                                              # Eingabe prüfen
            new_data = DBService().insert(MyData(data=user_input))  # Neues MyData-Objekt erstellen
            self.__add_child(new_data)                              # Neues Widget hinzufügen
            self.data_entry.delete(0, tk.END)                  # Eingabefeld leeren

        # Neues Daten-Widget hinzufügen
    def __add_child(self, mydata: MyData):
        data_frame = ((
            DataFrame(
                master=self.child_space,
                mydata=mydata,
                delete_button_clicked=self.__childDeleted
            )
        )
        .pack(fill="x", padx=5, pady=5))                        # DataFrame im UI platzieren
        self.childs.append(data_frame)                          # DataFrame zur Liste der Widgets hinzufügen

        # Daten-Widget gelöscht
    def __childDeleted(self, child: DataFrame):
        if child in self.childs:                                # Prüfen, ob das Widget in der Liste ist
            self.childs.remove(child)                           # Widget aus der Liste entfernen


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
