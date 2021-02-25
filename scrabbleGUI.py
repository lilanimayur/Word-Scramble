from tkinter import *
from tkinter.messagebox import _show
import random
import time
import nltk
from nltk.corpus import words
nltk.download('words')



class scrabble:

    def __init__(self):
        self.scr = Tk()
        self.frame = None
        self.can = None
        self.enter = None
        self.exit = None
        self.alphabet = [26]
        self.letterbutton = {}
        self.input = ""
        self.score = 0
        self.forget = []
        self.num = None
        self.dict = words.words()
        self.countxz = 1

    def components(self):

        self.frame=Frame(width=800,height=600)
        self.frame.pack()

        self.can=Canvas(self.frame,width=800,height=600,bg='grey')
        self.can.create_rectangle(20,20,780,420,fill='green')
        self.can.pack()

        self.enter = Button(self.scr,text="Enter",bg='blue', command=lambda: self.checkword())
        self.enter.place(x=425,y=450,width=200,height=100)

        self.exit = Button(self.scr, text="Exit",bg='red', command=lambda: self.quit())
        self.exit.place(x=40,y=450,width=200,height=100)

        self.can.create_rectangle(650,500,750,550,fill='white')
        self.can.pack()

        self.can.create_text(700,475, font="Times 15 italic bold", text="Your score is:")


        self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
                         'Q','R','S','T','U','V','W','X','Y','Z']


        self.num = self.can.create_text(700, 525, font="Times 15 italic bold", text=str(self.score))

    def printbutton(self):
        j = [i for i in range(0,8)]
        for j1 in j:
            i = random.randint(0, 25)
            self.letterbutton[j1] = Button(self.scr, text=self.alphabet[i], command=lambda x=j1: self.getinput(x))
            self.letterbutton[j1].place(x=20+j1*95,y=20,width=95,height=40)
        j = [i for i in range(8, 16)]
        for j1 in j:
            i = random.randint(0, 25)
            self.letterbutton[j1] = Button(self.scr, text=self.alphabet[i], command=lambda x=j1: self.getinput(x))

            self.letterbutton[j1].place(x=20 + (j1-8) * 95, y=60, width=95, height=40)
        j = [i for i in range(16, 24)]
        for j1 in j:
            i = random.randint(0, 25)
            self.letterbutton[j1] = Button(self.scr, text=self.alphabet[i], command=lambda x=j1: self.getinput(x))

            self.letterbutton[j1].place(x=20 + (j1-16) * 95, y=100, width=95, height=40)
        j = [i for i in range(24, 32)]
        for j1 in j:
            i = random.randint(0, 25)
            self.letterbutton[j1] = Button(self.scr, text=self.alphabet[i], command=lambda x=j1: self.getinput(x))

            self.letterbutton[j1].place(x=20 + (j1 - 24) * 95, y=140, width=95, height=40)
        j = [i for i in range(32, 40)]
        for j1 in j:
            i = random.randint(0, 25)
            self.letterbutton[j1] = Button(self.scr, text=self.alphabet[i], command=lambda x=j1: self.getinput(x))

            self.letterbutton[j1].place(x=20 + (j1 - 32) * 95, y=180, width=95, height=40)
        j = [i for i in range(40, 48)]
        for j1 in j:
            i = random.randint(0, 25)
            self.letterbutton[j1] = Button(self.scr, text=self.alphabet[i], command=lambda x=j1: self.getinput(x))

            self.letterbutton[j1].place(x=20 + (j1 - 40) * 95, y=220, width=95, height=40)
        j = [i for i in range(48, 56)]
        for j1 in j:
            i = random.randint(0, 25)
            self.letterbutton[j1] = Button(self.scr, text=self.alphabet[i], command=lambda x=j1: self.getinput(x))

            self.letterbutton[j1].place(x=20 + (j1 - 48) * 95, y=260, width=95, height=40)
        j = [i for i in range(56, 64)]
        for j1 in j:
            i = random.randint(0, 25)
            self.letterbutton[j1] = Button(self.scr, text=self.alphabet[i], command=lambda x=j1: self.getinput(x))

            self.letterbutton[j1].place(x=20 + (j1 - 56) * 95, y=300, width=95, height=40)
        j = [i for i in range(64, 72)]
        for j1 in j:
            i = random.randint(0, 25)
            self.letterbutton[j1] = Button(self.scr, text=self.alphabet[i], command=lambda x=j1: self.getinput(x))

            self.letterbutton[j1].place(x=20 + (j1 - 64) * 95, y=340, width=95, height=40)
        j = [i for i in range(72, 80)]
        for j1 in j:
            i = random.randint(0, 25)
            self.letterbutton[j1] = Button(self.scr, text=self.alphabet[i], command=lambda x=j1: self.getinput(x))

            self.letterbutton[j1].place(x=20 + (j1 - 72) * 95, y=380, width=95, height=40)

    def getinput(self,index):
        self.letterbutton[index].configure(bg='purple')
        self.input+=self.letterbutton[index]['text']
        self.forget.append(index)

    def checkword(self):
        v = self.input
        if v.lower() in self.dict:
            for i in range(len(v)):
                if v[i] == 'Z' or v[i] == 'X':
                    self.countxz = self.countxz + 1
            self.score = self.score + len(v) * self.countxz
            for j in range(len(self.forget)):
                self.letterbutton[self.forget[j]].destroy()
            self.input=""
            self.can.itemconfig(self.num, text=self.score)
        else:
            for j in range(len(self.forget)):
                self.letterbutton[self.forget[j]].configure(bg='red')
            self.input=""
        self.forget = []

    def time(self):
        self.scr.after(60000, lambda: _show('Time Up', 'Your score is '+str(self.score)))
        self.scr.after(70000, self.scr.destroy)


    def quit(self):
        self.scr.destroy()




