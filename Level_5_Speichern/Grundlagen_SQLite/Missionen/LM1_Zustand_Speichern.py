import dataclasses
import sqlite3
from dataclasses import dataclass
from typing import List

# Aufgabenbeschreibung
"""
1. Baue die Datenklasse Task{id: INTEGER (PRIMARY KEY AUTOINCREMENT), text: String, done: Boolean}.
2. Mach die DB_Service fertig mit den Methoden: insert(task), update(task), delete(task) und fetchAll() : List[Task].
3. Endkommentiere nach und nach die unten stehenden Tests.
4. Mach das alle Tests funktionieren.
"""

@dataclass
class Task:
    id: int = None
    text: str = ""
    done: bool = False

class DB_Service:

    def __init__(self, db_name='tasks.db'):
        self.db_name = db_name
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    done BOOLEAN NOT NULL
                )
            ''')
            conn.commit()

    def insert(self, task: Task) -> Task:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tasks (text, done) VALUES (?, ?)', (task.text, task.done))
            conn.commit()
            task.id = cursor.lastrowid
        return task

    def update(self, task: Task):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE tasks SET text = ?, done = ? WHERE id = ?', (task.text, task.done, task.id))
            conn.commit()

    def delete(self, task: Task):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE id = ?', (task.id,))
            conn.commit()

    def fetchAll(self) -> List[Task]:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, text, done FROM tasks')
            rows = cursor.fetchall()
            return [Task(id=row[0], text=row[1], done=bool(row[2])) for row in rows]

# Testen aller Methoden
if __name__ == "__main__":

    db_service = DB_Service()

    # Test: Insert
    print("Einfügen von Tasks...")
    task1 = Task(text="Einkaufen gehen", done=False)
    task2 = Task(text="Hausaufgaben machen", done=True)
    db_service.insert(task1)
    db_service.insert(task2)

    # Test: FetchAll
    print("Alle Tasks aus der Datenbank:")
    print(db_service.fetchAll())

    # Test: Update
    print("\nTask aktualisieren (1. Task als erledigt markieren)...")
    task1.done = True
    db_service.update(task1)

    # Nach dem Update alle Tasks abrufen
    print("Aktualisierte Tasks:")
    print(db_service.fetchAll())

    # Test: Delete
    print("\nTask löschen (2. Task löschen)...")
    db_service.delete(task2)

    # Nach dem Löschen alle Tasks abrufen
    print("Übrig gebliebene Tasks nach dem Löschen:")
    print(db_service.fetchAll())
