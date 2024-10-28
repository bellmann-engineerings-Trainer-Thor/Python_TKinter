import sqlite3

from Python_TKinter.Level_5_Speichern.SQLite_und_TKinter.Daten_Klasse import MyData


class DBService:
    def __init__(self, db_name='mydata.db'):
        self.db_name = db_name
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS mydata (
                                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                                       data TEXT NOT NULL)''')
            conn.commit()

    def insert(self, mydata: MyData):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO mydata (data) VALUES (?)', (mydata.data,))
            conn.commit()
            mydata.id = cursor.lastrowid
            return mydata

    def update(self, mydata: MyData):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE mydata SET data = ? WHERE id = ?', (mydata.data, mydata.id))
            conn.commit()

    def delete(self, mydata_id: int):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM mydata WHERE id = ?', (mydata_id,))
            conn.commit()

    def fetchall(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM mydata')
            rows = cursor.fetchall()
            return [MyData(id=row[0], data=row[1]) for row in rows]

if __name__ == "__main__":
    # Beispielverwendung
    db_service = DBService()
    print(db_service.fetchall())

    # Einfügen eines Datensatzes
    my_data = db_service.insert(MyData(data="Beispielinhalt"))
    print(db_service.fetchall())

    # Aktualisieren des Datensatzes
    my_data.data = "Aktualisierter Inhalt"
    db_service.update(my_data)
    print(db_service.fetchall())

    # Löschen eines Datensatzes
    db_service.delete(my_data.id)
    print(db_service.fetchall())
