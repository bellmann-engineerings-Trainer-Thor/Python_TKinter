"""
1. Baue die Datenklasse Task{id: INTEGER (PRIMARY KEY) text:String, done:Boolean}.
2. Mach die DB_Service fertig mit den Methoden: insert(task), update(task), delete(task) und fetchAll() : List<Task>.
3. Endkommentiere nach und nach die unten stehenden Tests.
4. Mach das alle Tests funktionieren.
"""
import sqlite3
import dataclasses
from typing import List


@dataclasses.dataclass
class Task:
    pass




class DB_Service:

    def __init__(self):
        # todo baue verbindung zur Datenbank auf
        # todo stelle sicher das auch eine Tabelle vorhanden ist
        # Hinweis: CREATE TABLE IF NOT EXISTS
        pass

    def insert(self, task: Task) -> Task:
        # todo Soll einen Task in der Datenbank hinzufügen und dann den hinzugefügten Task returnieren
        pass

    def update(self, task: Task):
        # todo Soll einen Task in der Datenbank aktualisieren
        pass

    def delete(self, task: Task):
        # todo Soll einen Task aus der Datenbank entfernen
        pass

    def fetchAll(self) -> List[Task]:
        # todo Soll eine Liste von Tasks returnieren
        pass



# Testen aller Methoden
if __name__ == "__main__":
    """
    hier sind die Tests. Mach das sie funktionieren / kommentiere sie nach und nach ein
    """

    db_service = DB_Service()

    # # Test: Insert
    # print("Einfügen von Tasks...")
    # task1 = Task(text="Einkaufen gehen", done=False)
    # task2 = Task(text="Hausaufgaben machen", done=True)
    # db_service.insert(task1)
    # db_service.insert(task2)
    #
    # # Test: FetchAll
    # print("Alle Tasks aus der Datenbank:")
    # print(db_service.fetchAll())
    #
    # # Test: Update
    # print("\nTask aktualisieren (1. Task als erledigt markieren)...")
    # task1.done = True
    # db_service.update(task1)
    #
    # # Nach dem Update alle Tasks abrufen
    # print("Aktualisierte Tasks:")
    # print(db_service.fetchAll())
    #
    # # Test: Delete
    # print("\nTask löschen (2. Task löschen)...")
    # db_service.delete(task2)
    #
    # # Nach dem Löschen alle Tasks abrufen
    # print("Übrig gebliebene Tasks nach dem Löschen:")
    # print(db_service.fetchAll())