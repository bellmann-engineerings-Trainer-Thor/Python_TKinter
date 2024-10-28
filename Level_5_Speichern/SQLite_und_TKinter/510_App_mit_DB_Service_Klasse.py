import tkinter as tk
from tkinter import messagebox
from Python_TKinter.Level_5_Speichern.SQLite_und_TKinter.DB_Service_Klasse import DBService
from Python_TKinter.Level_5_Speichern.SQLite_und_TKinter.Data_Widget import DataFrame
from Python_TKinter.Level_5_Speichern.SQLite_und_TKinter.Daten_Klasse import MyData


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.db_service = DBService()
        self.title("MyData Manager with Dynamic Frames")

        self.data_label = tk.Label(self, text="Data:")
        self.data_label.grid(row=0, column=0, padx=10, pady=10)

        self.data_entry = tk.Entry(self, width=40)
        self.data_entry.grid(row=0, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self, text="Add", command=self.add_data)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.frames_container = tk.Frame(self)
        self.frames_container.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.data_frames = []
        self.load_data()

    def load_data(self):
        for frame in self.data_frames:
            frame.destroy()
        self.data_frames.clear()

        all_data = self.db_service.fetchall()
        for data in all_data:
            self.add_data_frame(data)

    def add_data(self):
        data_text = self.data_entry.get()
        if data_text:
            new_data = MyData(data=data_text)
            new_data = self.db_service.insert(new_data)
            self.add_data_frame(new_data)
            self.data_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter some data.")

    def add_data_frame(self, mydata: MyData):
        data_frame = DataFrame(self.frames_container, mydata, self.db_service, self.remove_data_frame)
        data_frame.pack(fill="x", padx=5, pady=5)
        self.data_frames.append(data_frame)

    def remove_data_frame(self, frame):
        if frame in self.data_frames:
            self.data_frames.remove(frame)

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
