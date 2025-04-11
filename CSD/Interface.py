import customtkinter as ctk
import sys
import os

class Interfata:
    def __init__(self):
        # Appearance settings
        ctk.set_appearance_mode("dark")  # "light", "dark", or "system"
        ctk.set_default_color_theme("blue")  # Other options: "green", "dark-blue"

        """Main Window"""
        self.root = ctk.CTk()
        self.root.geometry('700x530')
        self.root.title('Proiect CSD')

        self.frame()
        self.root.mainloop()

    def frame(self):
        """Algorithm Selection"""
        self.label1 = ctk.CTkLabel(self.root,
                                   text='Alege algoritmul',
                                   font=('Arial', 20, 'bold'))
        self.label1.place(relx=0.5, rely=0.1, anchor='center')

        self.mode_combobox = ctk.CTkComboBox(self.root,
                                             values=["AES", "RSA"],
                                             state="readonly",
                                             font=('Arial', 18),
                                             dropdown_font=('Arial', 18))
        self.mode_combobox.set("AES")  # Set default value
        self.mode_combobox.place(relx=0.5, rely=0.2, anchor='center')

        """Buttons"""
        button_params = {
            'master': self.root,
            'width': 320,
            'height': 50,
            'font': ('Arial', 16, 'bold'),
            'corner_radius': 8
        }

        self.button = ctk.CTkButton(**button_params,
                                    text='Cripteaza Fisier',    fg_color="#3abf5e")
        self.button.place(relx=0.5, rely=0.35, anchor='center')

        self.button2 = ctk.CTkButton(**button_params,
                                     text='Decripteaza Fisier')
        self.button2.place(relx=0.5, rely=0.5, anchor='center')

        self.button3 = ctk.CTkButton(**button_params,           fg_color="#FFA500",
                                     text='Vizualizare Istoric')
        self.button3.place(relx=0.5, rely=0.65, anchor='center')

        self.button4 = ctk.CTkButton(**button_params,           fg_color="#FF0000",
                                     text='Selecteaza Locatia de Salvare')
        self.button4.place(relx=0.5, rely=0.8, anchor='center')


if __name__ == "__main__":
    try:
        Interfata()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
