import tkinter.messagebox
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

        except IOError:
            tkinter.messagebox.showinfo("Error", "Brak pliku")