import tkinter.messagebox
import datetime
import game
import question
from tkinter import messagebox
from question import *

def questionsFile():
    questions = []
    try:
        file = open("questions", encoding='utf8')
        question = file.readline()
        while question:
            if (len(question) < 7):
                question = file.readline()
            elif (len(question) > 50):
                question = file.readline()
            else:
                questions.append(Question(question))
                question = file.readline()
        file.close()
        return questions

    except IOError:
        tkinter.messagebox.showinfo("Error", "Brak pliku")

def appendQuestion(question):
    if(len(question) < 7):
        tkinter.messagebox.showinfo("Error", "Za krótkie pytanie")
    elif(len(question) > 50):
        tkinter.messagebox.showinfo("Error", "Za długie pytanie")
    else:
        try:
            file = open("questions", 'a', encoding='utf8')
            file.write("\n" + str(question))
            file.close()
        except IOError:
            tkinter.messagebox.showinfo("Error", "Brak pliku")

def saveRanking():
    try:
        file = open("ranking", 'a', encoding='utf8')
        file.write("\n"+str(datetime.datetime.now()))
        for i in game.players:
            file.write("\n"+str(i))
        file.close()
    except IOError:
        tkinter.messagebox.showinfo("Error", "Brak pliku")