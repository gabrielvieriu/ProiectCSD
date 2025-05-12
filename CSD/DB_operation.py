import sqlite3

def store_operation(file_id, algorithm_id, key_id, operation, exec_time, mem_usage):
    con = sqlite3.connect("proiect.db")
    cur = con.cursor()

    cur.execute("""
        INSERT INTO FileEncryption (file_id, algorithm_id, key_id, operation)
        VALUES (?, ?, ?, ?)
    """, (file_id, algorithm_id, key_id, operation))
    file_encryption_id = cur.lastrowid

    cur.execute("""
        INSERT INTO PerformanceMetrics (file_encryption_id, execution_time, memory_usage)
        VALUES (?, ?, ?)
    """, (file_encryption_id, exec_time, mem_usage))

    con.commit()
    con.close()

def update_file_status(file_id, status):
    con = sqlite3.connect("proiect.db")
    cur = con.cursor()
    cur.execute("UPDATE Files SET status=? WHERE id=?", (status, file_id))
    con.commit()
    con.close()
