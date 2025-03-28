import sqlite3

def main(db_file='proiect.db'):
    # Conectare la baza de date
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        # 1. Afisare tabele existente initial
        print("\nTabele existente inainte de creare:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print([table[0] for table in cursor.fetchall()])

        # 2. Creare tabel nou
        new_table_name = "tabel_nou"
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {new_table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nume TEXT NOT NULL,
            varsta INTEGER
        );
        """)
        conn.commit()
        print(f"\nTabelul '{new_table_name}' a fost creat cu succes")

        # 3. Afisare tabele dupa creare
        print("\nTabele existente dupa creare:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print([table[0] for table in cursor.fetchall()])

        # 4. Stergere doar a tabelului nou creat
        cursor.execute(f"DROP TABLE IF EXISTS {new_table_name};")
        conn.commit()
        print(f"\nTabelul '{new_table_name}' a fost sters cu succes")

        # 5. Afisare finala a tabelelor
        print("\nTabele existente dupa stergere:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print([table[0] for table in cursor.fetchall()])

    except sqlite3.Error as e:
        print(f"Eroare SQLite: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
