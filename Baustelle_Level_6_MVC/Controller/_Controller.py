from tkinter import messagebox

from Python_TKinter.Level_6_MVC.Model._Model import DBService


class MyDataController:
    def __init__(self, db_service: DBService, app):
        self.db_service = db_service
        self.app = app
        self.setup()
        self.load_data()

    def setup(self):
        self.app.data_label = tk.Label(self.app, text="Data:")
        self.app.data_label.grid(row=0, column=0, padx=10, pady=10)

        self.app.data_entry = tk.Entry(self.app, width=40)
        self.app.data_entry.grid(row=0, column=1, padx=10, pady=10)

        self.app.add_button = tk.Button(self.app, text="Add", command=self.add_data)
        self.app.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.app.child_space = tk.Frame(self.app)
        self.app.child_space.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.app.childs = []

    def add_data(self):
        data_text = self.app.data_entry.get()
        if data_text:
            new_data = MyData(data=data_text)
            new_data = self.db_service.insert(new_data)
            self.add_data_frame(new_data)
            self.app.data_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter some data.")

    def load_data(self):
        for frame in self.app.childs:
            frame.destroy()
        self.app.childs.clear()

        all_data = self.db_service.fetchall()
        for data in all_data:
            self.add_data_frame(data)

    def add_data_frame(self, mydata: MyData):
        data_frame = DataFrame(self.app.child_space, mydata, self)
        data_frame.pack(fill="x", padx=5, pady=5)
        self.app.childs.append(data_frame)

    def update_data(self, data_id: int, new_text: str):
        updated_data = MyData(id=data_id, data=new_text)
        self.db_service.update(updated_data)

    def delete_data(self, data_id: int, frame):
        self.db_service.delete(data_id)
        frame.destroy()