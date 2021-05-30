import tkinter as tk
import random
import fileWork
import app
import time

players =[]
class Game(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('400x300+550+250')
        self.title('5 Sekund')
        self.configure(bg='bisque')
        self.resizable(False, False)

        self.questions = []
        self.askRounds = tk.Label(self, text="Ile rund?", bg='bisque')
        self.askRounds.place(x=50, y=20)
        self.name_var = tk.StringVar()
        self.roundAsk = tk.Entry(self, textvariable=self.name_var, bg='bisque')
        self.roundAsk.place(x=200, y=20)
        self.startButton = tk.Button(self, text='Rozpocznij', height=1, width=10,
                                command=self.start, bg='goldenrod')
        self.startButton.place(x=160, y=100)
        self.close = tk.Button(self, text='Zamknij', height=1, width=10,
                               command=lambda: [self.destroy(), app.App.ranking(self.parent)], bg='coral1')


    def start(self):
        try:
            self.rounds = int(self.name_var.get()) * len(players) - 1
            self.questions = fileWork.questionsFile()
            self.askRounds.place_forget()
            self.startButton.place_forget()
            self.roundAsk.place_forget()
            self.question = tk.StringVar()
            self.currentPlayer = tk.StringVar()

            # define buttons "right" and "wrong"
            self.right = tk.Button(self, text='OK', height=1, width=10,
                                   command=lambda: [self.correct(), self.printQuestion()],
                                   bg='goldenrod')
            self.wrong = tk.Button(self, text='Źle', height=1, width=10,
                                   command=lambda: [self.printQuestion()], bg='goldenrod')

            self.question.set(self.questions[random.randint(0, len(self.questions)) - 1])
            self.currentPlayer.set(players[app.counter % len(players)])

            tk.Label(self, textvariable=self.currentPlayer, bg='bisque', font=("Arial", 15)).place(relx=0.30, rely=0.2)
            tk.Label(self, textvariable=self.question, bg='bisque', font=("Arial", 15))\
                .place(relx=0.5, rely=0.4, anchor='center')

            self.countdown(5)

        except ValueError:
            tk.messagebox.showinfo("Błąd", "Wpisz liczbę")
            self.roundAsk.delete(0, tk.END)

    def printQuestion(self):
        if self.rounds > 0:
            # hide all buttons
            self.close.place_forget()
            self.right.place_forget()
            self.wrong.place_forget()

            #change player, question and round
            app.counter += 1
            self.question.set(self.questions[random.randint(0, len(self.questions)) - 1])
            self.currentPlayer.set(players[app.counter % len(players)])
            self.rounds -= 1
            self.countdown(5)

        else:
            app.App.ranking(self.parent)
            self.destroy()


    def correct(self):
        players[app.counter % len(players)].addPoints(1)

    def countdown(self, count):
        label = tk.Label(self, bg='bisque', font=("Arial", 15))
        label.place(x=195, y=150)

        while count > -1:
            label['text'] = count
            time.sleep(1)
            count -= 1
            label.update()

        label.destroy()

        self.close.place(x=160, y=240)      #show buttons again
        self.right.place(x=60, y=240)
        self.wrong.place(x=260, y=240)


class Ranking(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x300+550+250')
        self.title('Ranking')
        self.configure(bg='bisque')
        self.resizable(False, False)

        tk.Button(self, text='Zamknij', height= 1, width=10, \
                  command=lambda: [self.destroy(), self.ending()], bg='coral1').place(x=160, y=270)

        scrollbar = tk.Scrollbar(self, orient="vertical")
        ranking = tk.Listbox(self, yscrollcommand=scrollbar.set, bg='bisque', \
                             font=("Arial", 15), justify='center')
        players.sort(key=lambda Player: Player.getPoints, reverse=True)

        for i in range(len(players)):
            ranking.insert(i, str(i + 1) + ". " + str(players[i]))
        ranking.place(relheight=0.9, relwidth=1)

    def ending(self):
        players[:] = []
