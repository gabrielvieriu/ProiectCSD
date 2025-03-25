import sqlite3
import os
con = sqlite3.connect("proiect.db")
cur = con.cursor()
cur.executescript("""
CREATE TABLE IF NOT EXISTS Files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    path TEXT NOT NULL,
    size INTEGER,
    status TEXT CHECK(status IN ('encrypted', 'decrypted'))
);

CREATE TABLE IF NOT EXISTS EncryptionAlgorithms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT CHECK(type IN ('symmetric', 'asymmetric')),
    key_size INTEGER
);

CREATE TABLE IF NOT EXISTS Keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    algorithm_id INTEGER,
    key_data TEXT NOT NULL,
    FOREIGN KEY (algorithm_id) REFERENCES EncryptionAlgorithms(id)
);

CREATE TABLE IF NOT EXISTS FileEncryption (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    algorithm_id INTEGER,
    key_id INTEGER,
    operation TEXT CHECK(operation IN ('encrypt', 'decrypt')),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (file_id) REFERENCES Files(id),
    FOREIGN KEY (algorithm_id) REFERENCES EncryptionAlgorithms(id),
    FOREIGN KEY (key_id) REFERENCES Keys(id)
);

CREATE TABLE IF NOT EXISTS PerformanceMetrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_encryption_id INTEGER,
    execution_time REAL,
    memory_usage REAL,
    FOREIGN KEY (file_encryption_id) REFERENCES FileEncryption(id)
);
""")
path1=r"C:\Users\vieri\OneDrive\Desktop\Facultate\CSD\file1.txt"
size1=os.path.getsize(path1)
cur.execute("""
    INSERT INTO Files (name, path, size, status) VALUES(?,?,?,?)""",
    ('file1.txt',path1,size1,'decrypted')
)
con.commit()

con.close()