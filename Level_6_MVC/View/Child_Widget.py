import tkinter as tk
from Python_TKinter.Level_5_Speichern.SQLite_und_TKinter.DB_Service_Klasse import DBService
from Python_TKinter.Level_5_Speichern.SQLite_und_TKinter.Daten_Klasse import MyData


class DataFrame(tk.Frame):
    def __init__(self, parent, mydata: MyData, db_service: DBService, on_delete):
        super().__init__(parent)
        self.mydata = mydata
        self.db_service = db_service
        self.on_delete = on_delete

        self.data_label = tk.Label(self, text=f"ID: {self.mydata.id}, Data:")
        self.data_label.grid(row=0, column=0, padx=5, pady=5)

        self.data_entry = tk.Entry(self, width=30)
        self.data_entry.insert(0, self.mydata.data)
        self.data_entry.grid(row=0, column=1, padx=5, pady=5)

        self.update_button = tk.Button(self, text="Update", command=self.update_data)
        self.update_button.grid(row=0, column=2, padx=5, pady=5)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_data)
        self.delete_button.grid(row=0, column=3, padx=5, pady=5)

    def update_data(self):
        updated_text = self.data_entry.get()
        if updated_text:
            self.mydata.data = updated_text
            self.db_service.update(self.mydata)
        else:
            messagebox.showwarning("Input Error", "Please enter some data to update.")

    def delete_data(self):
        self.db_service.delete(self.mydata.id)
        self.on_delete(self)
        self.destroy()
