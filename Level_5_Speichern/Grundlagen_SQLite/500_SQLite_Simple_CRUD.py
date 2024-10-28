import sqlite3

#**************************************************************************************
# Erzeuge ggf. eine neue Datenbank andernfalls öffne die Datenbank.
#**************************************************************************************
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS example_table (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')
    conn.commit()

#**************************************************************************************
# CREATE Daten
#**************************************************************************************
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO example_table (name, age) VALUES ('John', 25)")
    cursor.execute("INSERT INTO example_table (name, age) VALUES ('Jane', 30)")
    cursor.execute("INSERT INTO example_table (name, age) VALUES ('Bob', 35)")
    conn.commit()

#**************************************************************************************
# READ Daten
#**************************************************************************************
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM example_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#**************************************************************************************
# UPDATE Daten
#**************************************************************************************
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("UPDATE example_table SET age = 28 WHERE name = 'Jane'")
    conn.commit()

#**************************************************************************************
# DELETE Daten
#**************************************************************************************
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM example_table WHERE name = 'Bob'")
    conn.commit()

#**************************************************************************************
# READ Daten nach UPDATE und DELETE
#**************************************************************************************
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM example_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#**************************************************************************************
# Randbemerkung
#**************************************************************************************
print("\nmit welchen Datentypen haben wir es zu tun?")
print("der Returnwert von cursor.fetchall() ist: ", type(rows))
print("ein einzelnes Element dieser List ist ein: ", type(rows[0]))
