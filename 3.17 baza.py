import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza danych zostalą podłączona")
except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danch", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
