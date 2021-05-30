import data
import game
from tkinter import *
from tkinter import messagebox


import tkinter as tk

counter = 0

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x300+550+250')
        self.title('5 Sekund')
        self.configure(bg='bisque')
        self.resizable(False, False)
        addQuestionButton = tk.Button(self, text='Dodaj pytanie', height= 1, width=10, command=self.addQuestion, bg='goldenrod')
        addPlayerButton = tk.Button(self, text='Dodaj gracza',  height= 1, width=10, command=self.addPlayer, bg='goldenrod')
        deletePlayerButton = tk.Button(self, text='Usuń gracza',  height= 1, width=10, command=self.deletePlayer, bg='goldenrod')
        startButton = tk.Button(self, text='Rozpocznij',  height= 1, width=10, command=self.startGame, bg='goldenrod')
        exit = tk.Button(self, text='Zamknij', height= 1, width=10, command=self.destroy, bg='coral1')

        startButton.place(x=160, y=60)
        addQuestionButton.place(x=50, y=140)
        addPlayerButton.place(x=160, y=140)
        deletePlayerButton.place(x=270, y=140)
        exit.place(x=160, y=240)

        self.mainloop()

    def addPlayer(self):
        window = data.AddPlayer(self)
        window.grab_set()

    def deletePlayer(self):
        if len(game.players) == 0:
            tk.messagebox.showinfo("Błąd", "Nie dodano jeszcze graczy")
        else:
            window = data.DeletePlayers(self)
            window.grab_set()

    def startGame(self):
        if len(game.players) != 0:
            window = game.Game(self)
            window.grab_set()
        else:
            tk.messagebox.showinfo("Bład", "Brak graczy")

    def addQuestion(self):
        window = data.AddQuestion(self)
        window.grab_set()

    def ranking(self):
        window = game.Ranking(self)
        window.grab_set()

if __name__ == "__main__":
    app = App()
    app.mainloop()