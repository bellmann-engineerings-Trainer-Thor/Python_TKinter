import tkinter as tk
from tkinter import messagebox
from Python_TKinter.Level_6_MVC.Model._Model import DBService
from Python_TKinter.Level_5_Speichern.SQLite_und_TKinter.Daten_Klasse import MyData


class DataFrame(tk.Frame):
    def __init__(self, parent, mydata: MyData, delete_button_clicked):
        super().__init__(master=parent)
        self.mydata = mydata                             # Datenobjekt speichern
        self.db_service = DBService()                    # DB-Service instanzieren
        self.delete_button_clicked = delete_button_clicked  # Callback speichern

        # Label für Daten-ID und -Text
        self.data_label = tk.Label(self, text=f"ID: {self.mydata.id}, Data:")
        self.data_label.grid(row=0, column=0, padx=5, pady=5)

        # Eingabefeld für Daten-Text
        self.data_entry = tk.Entry(self, width=30)
        self.data_entry.insert(0, self.mydata.data)
        self.data_entry.grid(row=0, column=1, padx=5, pady=5)

        # Update-Button hinzufügen
        self.update_button = tk.Button(self, text="Update", command=self.__update_button_clicked)
        self.update_button.grid(row=0, column=2, padx=5, pady=5)

        # Delete-Button hinzufügen
        self.delete_button = tk.Button(self, text="Delete", command=self.__delete_button_clicked)
        self.delete_button.grid(row=0, column=3, padx=5, pady=5)

    # Daten aktualisieren
    def __update_button_clicked(self):
        updated_text = self.data_entry.get()                     # Eingabewert holen
        if updated_text:                                         # Prüfen, ob Eingabe vorhanden
            self.mydata.data = updated_text                      # Datenobjekt aktualisieren
            self.db_service.update(self.mydata)                  # Datenbank aktualisieren

    # Daten löschen
    def __delete_button_clicked(self):
        self.db_service.delete(self.mydata.id)                   # Datenbankeintrag löschen
        self.delete_button_clicked(self)                         # Callback ausführen
        self.destroy()                                           # Widget zerstören
