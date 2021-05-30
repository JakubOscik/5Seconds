from tkinter import *
import tkinter as tk
import fileWork
from player import *
import game

class DeletePlayers(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('400x300+550+250')
        self.title('Usuwanie graczy')
        self.configure(bg='bisque')
        self.resizable(False, False)
        self.name_var = tk.StringVar()
        scrollbar = tk.Scrollbar(self, orient="vertical")
        self.names = tk.Listbox(self, width=20, height=10, yscrollcommand=scrollbar.set, bg='bisque')
        for i in range(len(game.players)):
            self.names.insert(i, str(i+1) + " " + str(game.players[i]))

        self.names.place(x=140, y=10)
        tk.Label(self, text="Podaj numer gracza, którego chcesz usunąć", bg='bisque').place(x=80, y=190)

        e1 = tk.Entry(self, textvariable=self.name_var, bg='bisque')
        e1.place(x=140, y=220)
        tk.Button(self, text='Usuń gracza', height= 1, width=10,
                  command=lambda: [self.delete(), e1.delete(0, END)], bg='goldenrod').place(x=20, y=250)
        tk.Button(self, text='Zamknij', height= 1, width=10, command=self.destroy, bg='coral1').place(x=300, y=250)

    def delete(self):
        try:
            if self.name_var.get() != "":
                if int(self.name_var.get()) <= len(game.players):
                    del game.players[int(self.name_var.get()) - 1]
                    self.names.delete(0, len(game.players))
                    self.names.place_forget()
                    for i in range(len(game.players)):
                        self.names.insert(i, str(i+1) + " " + str(game.players[i]))
                    self.names.place(x=140, y=10)
                else:
                    tk.messagebox.showinfo("Usuwanie", "Nie ma takiego gracza")
            else:
                tk.messagebox.showinfo("Błąd", "Nie podano numeru")
        except ValueError:
            tk.messagebox.showinfo("Błąd", "Wpisz numer")

class AddPlayer(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100+600+325')
        self.title('Dodawanie graczy')
        self.configure(bg='bisque')
        self.resizable(False, False)

        self.name_var = tk.StringVar()
        e1 = tk.Entry(self, textvariable=self.name_var, bg='bisque')
        e1.place(x=90, y=30)
        tk.Label(self, text="Wpisz nazwę gracza", bg='bisque').place(x=95, y=5)
        tk.Button(self, text='Dodaj gracza', height= 1, width=10,
                  command=lambda: [self.add(), e1.delete(0, END)], bg='goldenrod').place(x=10, y=60)
        tk.Button(self, text='Zamknij', height= 1, width=10, command=self.destroy, bg='coral1').place(x=210, y=60)

    def add(self):
        if self.name_var.get() != "":
            exists = False
            for i in game.players:
                if i.getName == self.name_var.get():
                    tk.messagebox.showinfo("Błąd", "Gracz o takiej nazie już istnieje")
                    exists = True
            if not exists:
                game.players.append(Player(self.name_var.get()))

        else:
            tk.messagebox.showinfo("Błąd", "Nie podano nazwy")


class AddQuestion(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100+600+325')
        self.title('Dodawanie pytania')
        self.configure(bg='bisque')
        self.resizable(False, False)

        self.name_var = tk.StringVar()
        e1 = tk.Entry(self, textvariable=self.name_var, bg='bisque')
        e1.place(x=90, y=30)
        tk.Label(self, text="Wpisz treść pytania", bg='bisque').place(x=95, y=5)
        tk.Button(self, text='Dodaj pytanie', height= 1, width=10,
                  command=lambda: [self.add(), e1.delete(0, END)], bg='goldenrod').place(x=10, y=60)
        tk.Button(self, text='Zamknij', height= 1, width=10,
                  command=self.destroy, bg='coral1').place(x=210, y=60)

    def add(self):
        if self.name_var.get() != "":
            fileWork.appendQuestion(self.name_var.get())

        else:
            tk.messagebox.showinfo("Błąd", "Treść pytania jest pusta")
