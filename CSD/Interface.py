import customtkinter as ctk
import sys
import os
import sqlite3
import openssl as ssl
import criptography as crip
import time

class Interfata:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.conn = sqlite3.connect("proiect.db")
        self.root = ctk.CTk()
        self.root.geometry('700x700')
        self.root.title('Proiect CSD')

        self.frame()
        self.root.mainloop()

    def frame(self):
        # Eticheta comuna
        self.label1 = ctk.CTkLabel(self.root, text='Alege algoritmul si biblioteca', font=('Arial', 20, 'bold'))
        self.label1.place(relx=0.5, rely=0.05, anchor='center')

        # ComboBox pentru algoritm
        self.mode_combobox = ctk.CTkComboBox(self.root,
                                             values=["AES", "RSA"],
                                             state="readonly",
                                             font=('Arial', 16),
                                             width=200)
        self.mode_combobox.set("AES")
        self.mode_combobox.place(relx=0.3, rely=0.12, anchor='center')

        # ComboBox pentru biblioteca
        self.library_combobox = ctk.CTkComboBox(self.root,
                                                values=["OpenSSL", "Cryptography"],
                                                state="readonly",
                                                font=("Arial", 16),
                                                width=200)
        self.library_combobox.set("OpenSSL")
        self.library_combobox.place(relx=0.7, rely=0.12, anchor='center')

        # Selectez cheia AES
        self.label_key = ctk.CTkLabel(self.root, text='Alege cheia AES', font=('Arial', 16))
        self.label_key.place(relx=0.5, rely=0.2, anchor='center')

        self.keys = self.load_keys_from_db()
        key_values = [k['key_data'] for k in self.keys]
        self.key_combobox = ctk.CTkComboBox(self.root,
                                            values=key_values,
                                            font=("Arial", 16),
                                            state="readonly",
                                            width=400)
        self.key_combobox.place(relx=0.5, rely=0.27, anchor='center')

        # Butoane principale
        button_params = {
            'master': self.root,
            'width': 320,
            'height': 50,
            'font': ('Arial', 16, 'bold'),
            'corner_radius': 8
        }


        self.button = ctk.CTkButton(**button_params,
                                    text='Cripteaza Fisier',
                                    fg_color="#3abf5e",
                                    command=self.encrypt_file)
        self.button.place(relx=0.5, rely=0.40, anchor='center')

        self.button2 = ctk.CTkButton(**button_params,
                                     text='Decripteaza Fisier',
                                     command=self.decrypt_file)
        self.button2.place(relx=0.5, rely=0.52, anchor='center')

        self.button3 = ctk.CTkButton(**button_params,
                                     fg_color="#FFA500",
                                     text='Istoric Operatii',
                                     command=self.debug_istoric)
        self.button3.place(relx=0.5, rely=0.64, anchor='center')

        self.button4 = ctk.CTkButton(**button_params,
                                     fg_color="#FF0000",
                                     text='Debug Chei',
                                     command=self.debug_chei)
        self.button4.place(relx=0.5, rely=0.76, anchor='center')

        # Input + buton pentru adaugare cheie
        self.entry_cheie = ctk.CTkEntry(self.root, width=300, font=("Arial", 16))
        self.entry_cheie.place(relx=0.5, rely=0.84, anchor='center')

        self.button_adauga_cheie = ctk.CTkButton(self.root,
                                                 text="Adauga Cheie Noua",
                                                 command=lambda: self.adauga_cheie_noua(self.entry_cheie.get()),
                                                 fg_color="#5555FF",
                                                 width=300)
        self.button_adauga_cheie.place(relx=0.5, rely=0.90, anchor='center')

        self.button_sterge_cheie = ctk.CTkButton(self.root,
                                                 text="Sterge Cheie Selectata",
                                                 command=self.sterge_cheie_selectata,
                                                 fg_color="#AA3333",
                                                 width=300)
        self.button_sterge_cheie.place(relx=0.5, rely=0.96, anchor='center')

    def load_keys_from_db(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, key_data FROM Keys WHERE algorithm_id = 1")
        return [{"id": row[0], "key_data": row[1]} for row in cursor.fetchall()]

    def encrypt_file(self):
        start_time = time.time()

        algorithm = self.mode_combobox.get()
        library = self.library_combobox.get()

        if algorithm == "AES":
            selected = self.key_combobox.get()
            if not selected:
                print("Nu ai selectat o cheie!")
                return
            key_id = next((k["id"] for k in self.keys if k["key_data"] == selected), None)
            key = next((k["key_data"] for k in self.keys if k["id"] == key_id), None)

            if library == "OpenSSL":
                ssl.encrypt_AES("file.txt", "fila2.txt", key)
            elif library == "Cryptography":
                crip.encrypt_file_aes("file.txt", "fila2.txt", key)

        elif algorithm == "RSA":
            if library == "OpenSSL":
                ssl.generate_RSA_key("private.pem", "public.pem")

                ssl.encrypt_RSA("file.txt", "fila2.txt", "public.pem")
            elif library == "Cryptography":
                crip.generate_rsa_keys()
                crip.encrypt_file_rsa("file.txt", "fila2.txt", "public.pem")

        elapsed_time = time.time() - start_time
        print(f"Timp criptare: {elapsed_time:.4f} secunde")

    def decrypt_file(self):
        start_time = time.time()

        algorithm = self.mode_combobox.get()
        library = self.library_combobox.get()

        if algorithm == "AES":
            selected = self.key_combobox.get()
            if not selected:
                print("Nu ai selectat o cheie!")
                return
            key_id = next((k["id"] for k in self.keys if k["key_data"] == selected), None)
            key = next((k["key_data"] for k in self.keys if k["id"] == key_id), None)

            if library == "OpenSSL":
                ssl.decrypt_AES("fila2.txt", "file3.txt", key)
            elif library == "Cryptography":
                crip.decrypt_file_aes("fila2.txt", "file3.txt", key)

        elif algorithm == "RSA":
            if library == "OpenSSL":
                ssl.decrypt_RSA("fila2.txt", "file3.txt", "private.pem")
            elif library == "Cryptography":
                crip.decrypt_file_rsa("fila2.txt", "file3.txt", "private.pem")

        elapsed_time = time.time() - start_time
        print(f"Timp decriptare: {elapsed_time:.4f} secunde")

    def debug_chei(self):
        print("=== Chei AES ===")
        for k in self.keys:
            print(f"Cheie: {k['key_data']}")

    def debug_istoric(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM FileEncryption")
        rows = cursor.fetchall()
        print("=== Istoric Criptare ===")
        for row in rows:
            print(row)

    def adauga_cheie_noua(self, key_text):
        if not key_text:
            print("Cheia este goala.")
            return

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Keys (algorithm_id, key_data) VALUES (?, ?)", (1, key_text))
        self.conn.commit()
        print(f"Cheia '{key_text}' a fost adaugata in baza de date.")

        self.keys = self.load_keys_from_db()
        new_values = [k['key_data'] for k in self.keys]
        self.key_combobox.configure(values=new_values)

    def sterge_cheie_selectata(self):
        selected = self.key_combobox.get()
        if not selected:
            print("Nu ai selectat o cheie pentru stergere!")
            return

        key_id = next((k["id"] for k in self.keys if k["key_data"] == selected), None)
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Keys WHERE id = ?", (key_id,))
        self.conn.commit()
        print("Cheie stearsa.")

        self.keys = self.load_keys_from_db()
        new_values = [k['key_data'] for k in self.keys]
        self.key_combobox.configure(values=new_values)
        self.key_combobox.set("")

if __name__ == "__main__":
    try:

        Interfata()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
