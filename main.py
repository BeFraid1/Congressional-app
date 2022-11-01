
import random
import os
import sys
from time import time
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as customtkinter
from winsound import *

call = None



def login():
    global entry1, entry2,log_screen
    
    log_screen = customtkinter.CTkToplevel(main_screen)
    log_screen.geometry('400x400')
    log_screen.title("Login")
    
    frame = customtkinter.CTkFrame(master=log_screen,width=200,height=300,corner_radius=10)
    frame.pack(padx=50, pady=50)
    
    customtkinter.CTkLabel(master=frame, text="Login",text_font = ('Calibri',15)).pack(padx=10,pady=5)
    
    entry1 = customtkinter.CTkEntry(master=frame,placeholder_text="Username",width=120,height=25,border_width=2,corner_radius=10)
    entry1.pack(padx=10)
    
    entry2 = customtkinter.CTkEntry(master=frame,placeholder_text="Password",width=120,height=25,border_width=2,corner_radius=10,show = '*')
    entry2.pack(padx=10,pady = 10)
    

    
    customtkinter.CTkButton(frame,width=5,height =1, text='Login',text_font = ('Calibri',12),command=log_user).pack(padx=10, pady=5)
    
    log_screen.bind("<Return>", log_user)

def log_user(fake = 0):
    global a,b,c
    user=entry1.get()
    pswd=entry2.get()
    
    success = False
    with open('user_details', 'r') as file:
        for i in file:
            a, b, c = i.split("|")
            c = c.strip()
            if(a == user and pswd == b):
                success = True
                break
        if(success == True):

            store(c)
            log_screen.destroy()
            
        else:
            wronglog = customtkinter.CTkLabel(log_screen,text="Username or password were incorrect\nPlease try again", text_font = ('Calibri',15))
            wronglog.pack(padx=10, pady=5)
            log_screen.after(3000, lambda: wronglog.destroy())


def reg():
    global entry1, entry2,reg_screen
    
    reg_screen = customtkinter.CTkToplevel(main_screen)
    reg_screen.geometry('400x400')
    reg_screen.title("Login")
    
    frame = customtkinter.CTkFrame(master=reg_screen,width=200,height=300,corner_radius=10)
    frame.pack(padx=50, pady=50)
    
    customtkinter.CTkLabel(master=frame, text="Register",text_font = ('Calibri',15)).pack(padx=10,pady=5)
    
    entry1 = customtkinter.CTkEntry(master=frame,placeholder_text="Username",width=120,height=25,border_width=2,corner_radius=10)
    entry1.pack(padx=10)
    
    entry2 = customtkinter.CTkEntry(master=frame,placeholder_text="Password",width=120,height=25,border_width=2,corner_radius=10,show = '*')
    entry2.pack(padx=10,pady = 10)
    
    user=entry1.get()
    pswd=entry2.get()
    
    
    customtkinter.CTkButton(frame,width=5,height =1, text='Register',text_font = ('Calibri',12),command=reg_user).pack(padx=10, pady=5)
    
    reg_screen.bind("<Return>", reg_user)
    
def reg_user(fake = 0):
    global num
    user=entry1.get()
    pswd=entry2.get()
    
    with open('user_details', 'r') as file:
        for i in file:
            a, b, c = i.split("|")
            c = c.strip()
            if(a == user):
                wrongreg = customtkinter.CTkLabel(reg_screen,text="Please use a different username", text_font = ('Calibri',15))
                wrongreg.pack(padx=10, pady=5)
                reg_screen.after(3000, lambda: wrongreg.destroy())
                return
    
    with open("numo", 'r') as f:
        num = int(f.readlines()[-1])
    with open('user_details', 'a') as f:
        f.write(user + '|' + pswd + '|' + str(num) + '\n')
        
        entry1.delete(0, END)
        entry2.delete(0, END)
        
        num += 1
        
    with open("numo", 'a') as f:
        num = f.write('\n' + str(num))
        
    
    
    with open('user_details', 'r') as file:
        for i in file:
            a, b, c = i.split("|")
            c = c.strip()
            if(a == user and pswd == b):
                success = True
                break
        if(success == True):
            store(c)
            reg_screen.destroy()
            



def main():
    global main_screen
    
    main_screen = customtkinter.CTk()
    main_screen.geometry('900x500')
    main_screen.title('Main menu')
    
    image1 = Image.open("bank.png")
    reimage = image1.resize((300, 300))
    test = ImageTk.PhotoImage(reimage)
    
    label1 = customtkinter.CTkLabel(image = test)
    label1.place(x=100,y=50)
    
    
    log_button = customtkinter.CTkButton(master=main_screen,text = "Login",text_font = ('Calibri',15),width = 200, border_width = 0,height=40, command=login)
    log_button.place(x = 500, y = 150)
    
    reg_button = customtkinter.CTkButton(master=main_screen,text = "Register",text_font = ('Calibri',15),width = 200, border_width = 0,height=40, command=reg)
    reg_button.place(x = 500, y = 225)
    
    main_screen.mainloop()
    
def store(c):
    global balance, score, right, expoval, moneyamnt, cFile
    cFile = c + '.txt'
        
        
    try:
        with open(cFile,'r')as f:
            for i in f:
                balance,score = i.split("|")
    except:
        with open(cFile, "a")as f:
            f.write('0|0')
        with open(cFile,'r')as f:
            for i in f:
                balance,score = i.split("|")
    
    balance = int(balance)
    score = int(score)
    


    right =[]
    expoval = 1

    moneyamnt = ''
    atmscreen()
    
def atmscreen():
    global showbal
    atm_screen = customtkinter.CTkToplevel(main_screen)
    atm_screen.geometry('400x600')
    atm_screen.title("ATM")
    
    frame = customtkinter.CTkFrame(master=atm_screen,width=200,height=300,corner_radius=10)
    frame.pack(padx=20, pady=40)
    
    customtkinter.CTkLabel(master=frame,width=150, text="ATM",text_font = ('Calibri',35)).pack(padx=10,pady=5)
    
    showbal = customtkinter.CTkLabel(master=frame, text='Balance: ' + str(balance) + '$',text_font = ('Calibri',20))
    showbal.pack(padx=10,pady=10)
    
    depButton = customtkinter.CTkButton(master = frame,width = 30, text='Deposit',text_font=('Calibri',12), command=showdep)
    depButton.pack(padx=15, pady=10)
    
    withButton = customtkinter.CTkButton(master = frame,width = 30, text='Withdraw',text_font=('Calibri',12), command=showWith)
    withButton.pack(padx=15)

    gameButton = customtkinter.CTkButton(master = frame,width = 30, text='Games',text_font=('Calibri',12), command=games)
    gameButton.pack(padx=15,pady=10)
    
    logoutButton = customtkinter.CTkButton(master = frame,width = 30, text='Logout',text_font=('Calibri',12), command= lambda : atm_screen.destroy())
    logoutButton.pack(padx=15)
    
    fakeLabel = customtkinter.CTkLabel(frame, text='').pack(padx=15,pady=10)
    
def games():
    try:
        score += int(scorenum)
    except:
        pass
    
    game_screen = customtkinter.CTkToplevel(main_screen)
    game_screen.geometry('400x400')
    game_screen.title("Games")
    
    math_button =  customtkinter.CTkButton(game_screen, text="Math game",text_font = ('Calibri',20),command=mathGame)
    math_button.pack(pady=50)
    
    mem_button = customtkinter.CTkButton(game_screen, text="Memory game",text_font = ('Calibri',20),command=memGame)
    mem_button.pack()
    
    word_button = customtkinter.CTkButton(game_screen, text="Word game",text_font = ('Calibri',20),command= wordGame)
    word_button.pack(pady=50)
 
def check(select):
    global score, balance, scorenum
    if len(correct) < len(lst):
        if correct == lst:
            score += 1
            scorenum+=1
            with open(cFile,'a')as f:
                f.write('\n' + str(balance) + '|' + str(score))
            with open(cFile,'r')as f:
                for i in f:
                    balance,score = i.split("|")
    elif len(correct) == len(lst):
        if correct == lst:
            randnum(select)
            score = int(score)
            score +=1
            scorenum +=1 
            with open(cFile,'a')as f:
                f.write('\n' + str(balance) + '|' + str(score))
            with open(cFile,'r')as f:
                for i in f:
                    balance,score = i.split("|")
                
    elif len(correct) > len(lst):
            select.destroy()
            correct.clear()
            lst.clear()
            urs = 0
            nums = 0
            select.destroy()
        
     
def memGame():
    global lst,correct,memscreen,scorenum
    scorenum = 0
    lst = []
    correct = []

    
    memscreen = customtkinter.CTkToplevel(main_screen)
    memscreen.geometry('500x500')
    
    customtkinter.CTkLabel(memscreen,text='Please enter the numbers in\nthe order provided',text_font=('Calibri',20),width = 100).place(x=100,y=350)
    
    randnum(memscreen)
    for i in lst:
        buttons(memscreen)

def memButton(numButton, select):
    global urs,scorenum
    try:
        urs = numButton
        correct.append(urs)
        
    except:
        urs = numButton
        correct.append(urs)
        
    check(select)

def buttons(select):
    global button_four, button_one, button_two, button_three
    
    
    button_one = customtkinter.CTkButton(select, text="1",height=70,width=117, command = lambda: memButton(1, select),border_width=1).place(x=195,y=50)
    
    button_two = customtkinter.CTkButton(select, text="2",height=70,width=117, command = lambda: memButton(2, select),border_width=1).place(x=80, y = 120)
    
    button_three = customtkinter.CTkButton(select, text="3",height=70,width=117, command = lambda: memButton(3, select),border_width=1).place(x = 195,y=  190)
    
    button_four = customtkinter.CTkButton(select, text="4",height=70,width=117, command = lambda: memButton(4, select),border_width=1).place(x=310, y = 120)


def randnum(select):
    global rand, nums, urs, score,scorenum
    rand = random.randint(1,4)
    lst.append(rand)
    
    for i in lst:
        
        try:
            nums += i
        except:
            nums = i
    scorenum = len(lst)
    
    randomnum = customtkinter.CTkLabel(select, text=rand,width = 1, height = 1,text_font= ('Calibri', 30))
    randomnum.place(x=240,y=300)
    
    scoreword = customtkinter.CTkLabel(select, text='Score: ' + str(scorenum),text_font= ('Calibri', 15),width = 50)
    scoreword.place(x=220,y=0)
    

    
    select.after(500, lambda: randomnum.destroy())
    
    correct.clear()

def mathrandnums():
    global ans, rand1, rand2
    
    rand1 = random.randint(1,100)
    rand2 = random.randint(1,100)
    ans = rand1 + rand2
    




def expo():
    global right, expoval, score
    global balance, score, right, expoval, moneyamnt
    for i in right:
        if score <= 0:
            score += 1
            
        score = int(score + expoval)
        expoval+= 0.0625      
        
        
def timeup():
    customtkinter.CTkLabel(mathscreen, text= "TIME IS UP",text_font= ('Calibri', 15)).pack()
    mathscreen.after(0, lambda: mathscreen.destroy())
    
def givetime():
    global call
    if call is not None:

        mathscreen.after_cancel(call)
        
        call = None

def checkcall():
    global call
    if call is None:
        call = mathscreen.after(5000, timeup )
        
def checkmath(fake = 0):
    global mathentry, mathans, equation,right, cFile
    global balance, score, right, expoval, moneyamnt,call
    
    givetime()
    
    call = 1
    
    
    if int(mathentry.get()) == ans:
        correctans = customtkinter.CTkLabel(mathscreen, text = "CORRECT")
        correctans.pack()
        correctans.after(1000, lambda: correctans.destroy())
        mathentry.delete(0, END)
        mathrandnums()
        equation.configure( text = str(rand1) + "+" + str(rand2))
        right.append(1)
        expo()
        
        call = None
        checkcall()
        
        with open(cFile,'a')as f:
            f.write('\n' + str(balance) + '|' + str(score))
            
        equation.configure(text = str(rand1) + "+" + str(rand2))
        
        mathentry.delete(0, 'end')
        
        mathscreen.destroy()
        main_screen.after_cancel(countdown)
        mathGame()
        
        
        
        
    else:
        customtkinter.CTkLabel(mathscreen, text= 'WRONG', text_font= ('Calibri', 15)).pack()
        mathscreen.after(2000, lambda: mathscreen.destroy())
    

def mathGame():
    global timer
    global mathscreen, mathentry, mathans, equation
    

    mathscreen = customtkinter.CTkToplevel(main_screen)
    mathscreen.title('Math game')
    mathscreen.geometry('400x400')

    mathans = StringVar

    checkcall()
    mathrandnums()

    
    equation = customtkinter.CTkLabel(mathscreen,text = str(rand1) + "+" + str(rand2),text_font=("Calibri", 40))
    equation.pack(pady = 15)

    mathentry = customtkinter.CTkEntry(mathscreen,textvariable= mathans)
    mathentry.pack()

    checBut = customtkinter.CTkButton(mathscreen,text = "Check", command = checkmath)
    checBut.pack(pady=15)
    
    mathscreen.bind("<Return>", checkmath)
    
    timer = customtkinter.CTkLabel(mathscreen, text='5.00' + " seconds left",text_font=("Calibri", 35))
    timer.pack(pady=15)
    
    countdown(5000)
    
def countdown(count):
    try:
        if count > 0:
            mathscreen.after(1, countdown, count-1)
            timer.configure(text=str(count)[0] + '.'+ str(count)[1] + " seconds left")
        if count == 1:
            mathscreen.after(1, countdown, count-1)
            timer.configure(text=str(count)[0] + '.'+ str(count)[1] + " second left")
        if count < 1:
            mathscreen.destroy()
    except:
        return
    

def showdep():
    global depscreen, depamount, entrydepo, depscore,atmframe,atmtopframe,showbal,showbalindep
    global balance, score, right, expoval, moneyamnt
    
    depscreen = customtkinter.CTkToplevel(main_screen)
    depscreen.title("Balance")
    depscreen.geometry('400x600')
    

    customtkinter.CTkLabel(master = depscreen,text="Please enter an amount you would like to deposit", width = 50,text_font = ('Calibri', 20), fg= 'blue')#.place(x=35)
    
    depscore = customtkinter.CTkLabel(master = depscreen,text="You can deposit : " + str(score) + '$', width = 50)
    depscore#.place(x=35, y = 350)

    atmtopframe =customtkinter.CTkFrame(master=depscreen,width=200,height=50,corner_radius=10)
    atmtopframe.place(x= 100, y = 10)

    atmframe = customtkinter.CTkFrame(master=depscreen,width=200,height=300,corner_radius=10)
    atmframe.place(x= 100, y = 100)
    
    showbalindep = customtkinter.CTkLabel(atmtopframe, text = "Balance: " + str(balance) + '$',text_font= ("Calibri",15))
    showbalindep.place(x=25,y =10)
    
    showbal.configure(text='Balance: ' + str(balance) + '$')
    
    entrydepo = customtkinter.CTkEntry(master = atmframe,placeholder_text=  'Enter a number',width = 150,height=20, text_font= ('Calibri', 12))
    entrydepo.place(x = 25, y = 40)


    depscore = customtkinter.CTkLabel(atmframe, text="You can deposit : " + str(score) + '$', text_font = ('Calibri', 12))
    depscore.place(x= 25, y = 10)
    
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='1',command=lambda: press(1,entrydepo),border_width=2).place(x = 25, y = 60+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='2',command=lambda: press(2,entrydepo),border_width=2).place (x= 75, y = 60+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='3',command=lambda: press(3,entrydepo),border_width=2).place (x= 125, y = 60+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='4',command=lambda: press(4,entrydepo),border_width=2).place ( x=25, y = 100+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='5',command=lambda: press(5,entrydepo),border_width=2).place ( x=75, y = 100+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='6',command=lambda: press(6,entrydepo),border_width=2).place ( x=125, y = 100+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='7',command=lambda: press(7,entrydepo),border_width=2).place ( x=25, y = 140+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='8',command=lambda: press(8,entrydepo),border_width=2).place ( x=75, y = 140+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='9',command=lambda: press(9,entrydepo),border_width=2).place ( x=125, y = 140+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='0',command=lambda: press(0,entrydepo),border_width=2).place ( x=75, y = 180+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='<-',text_font = ('Calibri', 15),command= lambda: backspace(entrydepo),border_width=2).place(x = 125, y = 180+20)
    
    depscreen.bind("<Return>", depoenter)
   
    customtkinter.CTkButton(atmframe,text='Deposit', command=depoenter,width=150, height=40,border_width=2).place(x = 25, y = 240)
    
def showWith():
    global withscreen, depamount, entrydepo, depscore,atmframe,atmtopframe,showbal,scoreval,showbalinwith
    global balance, score, right, expoval, moneyamnt
    
    
    
    withscreen = customtkinter.CTkToplevel(main_screen)
    withscreen.title("Balance")
    withscreen.geometry('400x600')
    

    customtkinter.CTkLabel(master = withscreen,text="Please enter an amount you would like to deposit", width = 50,text_font = ('Calibri', 20), fg= 'blue')#.place(x=35)
    


    atmtopframe =customtkinter.CTkFrame(master=withscreen,width=200,height=50,corner_radius=10)
    atmtopframe.place(x= 100, y = 10)

    atmframe = customtkinter.CTkFrame(master=withscreen,width=200,height=300,corner_radius=10)
    atmframe.place(x= 100, y = 100)
    
    showbalinwith = customtkinter.CTkLabel(atmtopframe, text = "Balance: " + str(balance) + '$',text_font= ("Calibri",15))
    showbalinwith.place(x=25,y =10)
    
    showbal.configure(text='Balance: ' + str(balance) + '$')
    
    entrydepo = customtkinter.CTkEntry(master = atmframe,placeholder_text=  'Enter a number',width = 150,height=20, text_font= ('Calibri', 12))
    entrydepo.place(x = 25, y = 40)

    scoreval = customtkinter.CTkLabel(atmframe, text="Your score is : " + str(score) + '$', text_font = ('Calibri', 12))
    scoreval.place(x= 25, y = 10)
    
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='1',command=lambda: press(1,entrydepo),border_width=2).place(x = 25, y = 60+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='2',command=lambda: press(2,entrydepo),border_width=2).place (x= 75, y = 60+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='3',command=lambda: press(3,entrydepo),border_width=2).place (x= 125, y = 60+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='4',command=lambda: press(4,entrydepo),border_width=2).place ( x=25, y = 100+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='5',command=lambda: press(5,entrydepo),border_width=2).place ( x=75, y = 100+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='6',command=lambda: press(6,entrydepo),border_width=2).place ( x=125, y = 100+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='7',command=lambda: press(7,entrydepo),border_width=2).place ( x=25, y = 140+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='8',command=lambda: press(8,entrydepo),border_width=2).place ( x=75, y = 140+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='9',command=lambda: press(9,entrydepo),border_width=2).place ( x=125, y = 140+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='0',command=lambda: press(0,entrydepo),border_width=2).place ( x=75, y = 180+20)
    customtkinter.CTkButton(atmframe,width = 50,height=40,text='<-',text_font = ('Calibri', 15),command= lambda: backspace(entrydepo),border_width=2).place(x = 125, y = 180+20)
   
    withscreen.bind("<Return>", withenter)
    
    customtkinter.CTkButton(atmframe,text='Withdraw', command=withenter,width=150, height=40,border_width=2).place(x = 25, y = 240)
    
    
def withenter(fake = 0):
    global balance,score,right,expoval, moneyamnt
    try:
        if balance - int(entrydepo.get()) >= 0:
            balance -= int(entrydepo.get())
            score += int(entrydepo.get())
            with open(cFile,'a')as f:
                f.write('\n' + str(balance) + '|' + str(score))
            with open(cFile,'a')as f:
                f.write('\n' + str(balance) + '|' + str(score))
            showbal.configure(text = "Balance: " + str(balance) + '$')
            showbalinwith.configure(text = "Balance: " + str(balance) + '$')
            scoreval.configure(text = "Your score is : " + str(score) + '$')
            scoreval.after(5000, lambda: scoreval.destroy())
        elif balance - int(entrydepo.get()) < 0:
            lessthanonly = customtkinter.CTkLabel(text="PLEASE ONLY ENTER NUMBERS \n LESS THAN OR EQAUL TO " + str(balance), width = 50)
            lessthanonly.place(x=35, y = 300)
            lessthanonly.after(5000, lambda:lessthanonly.destroy())
            
    except:
        
        numsonly = customtkinter.CTkLabel(atmframe,text="PLEASE ONLY ENTER NUMBERS", width = 50,text_font=('Calibri',15) )
        numsonly.place(x=25, y = 300)
        numsonly.after(5000, lambda:numsonly.destroy())
    
    entrydepo.delete(0, END)
                       
#make it so it stops freezing after .after()
    
def backspace(select):
    
    select.delete(len(select.get())-1, END)


def depoenter(fake =0):
    global balance,score,right,expoval, moneyamnt
    try:
        if int(entrydepo.get()) <= score:
            score -= int(entrydepo.get())
            balance += int(entrydepo.get())

            depscore.configure(text = "You can deposit : " + str(score) + '$',width = 50)
            
            with open(cFile,'a')as f:
                f.write('\n' + str(balance) + '|' + str(score))
            showbal.configure(text = "Balance: " + str(balance) + '$')
            showbalindep.configure(text = "Balance: " + str(balance) + '$')
    except:
        numsonly = customtkinter.CTkLabel(atmframe,text="PLEASE ONLY ENTER NUMBERS", width = 50,text_font=('Calibri',15) )
        numsonly.place(x=25, y = 300)
        numsonly.after(5000, lambda:numsonly.destroy())

    entrydepo.delete(0, END)


def press(num,select):
    
    
    val = len(select.get())
    
    select.insert(val, str(num))

def wordGame():
    global guessaword, tries, wordscreen,word,x,y,r,entry1,guess,varlst,l1r1,l2r1,l3r1,l4r1,l5r1,l1r2,l2r2,l3r2,l4r2,l5r2,l1r3,l2r3,l3r3,l4r3,l5r3,l1r4,l2r4,l3r4,l4r4,l5r4,l1r5,l2r5,l3r5,l3r5,l4r5,l5r5, life
    words = []
    lstwords =[]

    with open('words.txt','r')as f:
        lists = f.readlines()
        for i in lists:
            trans = str.maketrans('\n', ' ')
            
            words.append(i.translate(trans))

    wordscreen = customtkinter.CTkToplevel(main_screen)
    wordscreen.title('Word Game')
    wordscreen.geometry('500x500')
    
    guess = ['_','_','_','_','_']

    word = random.choice(words)
    
    user = StringVar()
    tries = None
    life = 4
    x=0
    y=0
    r=0
    
    
    
    l1r1 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l1r1.place(x=0+150,y=0)
    l2r1 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l2r1.place(x=40+150 ,y=0)
    l3r1 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l3r1.place(x=80+150,y=0)
    l4r1 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l4r1.place(x=120+150,y=0)
    l5r1 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l5r1.place(x=160+150,y=0)
    
    l1r2 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l1r2.place(x=0+150,y=45)
    l2r2 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l2r2.place(x=40+150 ,y=45)
    l3r2 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l3r2.place(x=80+150,y=45)
    l4r2 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l4r2.place(x=120+150,y=45)
    l5r2 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l5r2.place(x=160+150,y=45)
    
    l1r3 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l1r3.place(x=0+150,y=90)
    l2r3 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l2r3.place(x=40+150 ,y=90)
    l3r3 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l3r3.place(x=80+150,y=90)
    l4r3 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l4r3.place(x=120+150,y=90)
    l5r3 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l5r3.place(x=160+150,y=90)
    
    l1r4 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l1r4.place(x=0+150,y=135)
    l2r4 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l2r4.place(x=40+150 ,y=135)
    l3r4 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l3r4.place(x=80+150,y=135)
    l4r4 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l4r4.place(x=120+150,y=135)
    l5r4 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l5r4.place(x=160+150,y=135)
    
    l1r5 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l1r5.place(x=0+150,y=180)
    l2r5 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l2r5.place(x=40+150 ,y=180)
    l3r5 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l3r5.place(x=80+150,y=180)
    l4r5 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l4r5.place(x=120+150,y=180)
    l5r5 = customtkinter.CTkFrame(wordscreen,width=30,height=40)
    l5r5.place(x=160+150,y=180)
    
    varlst = [l1r1,l2r1,l3r1,l4r1,l5r1,l1r2,l2r2,l3r2,l4r2,l5r2,l1r3,l2r3,l3r3,l4r3,l5r3,l1r4,l2r4,l3r4,l4r4,l5r4,l1r5,l2r5,l3r5,l4r5,l5r5]
    
    entry1 = customtkinter.CTkEntry(wordscreen,textvariable = user, text_font = ("Calibri", 25), width = 200,justify=CENTER)
    entry1.place(x=150,y=250)
    
    

    customtkinter.CTkButton(wordscreen,text = 'Enter',command = checkwords,width=100, text_font = ("Calibri", 25)).place(x=200,y=300)
    
    guessaword = customtkinter.CTkLabel(wordscreen, text="Guess a 5 letter word",text_font = ("Calibri", 25), width = 100)
    guessaword.place(x=110,y=350)
    
    wordscreen.protocol("WM_DELETE_WINDOW", restarttries)
    wordscreen.bind("<Return>", checkwords)
    
def restarttries():
    global tries
    tries = None
    wordscreen.destroy()
    
def checkwords(fake = 0):
    global tries,life,score
    
    
    

    if life == 0:
        guessaword.destroy()
        customtkinter.CTkLabel(wordscreen, text="You ran out of tries,\n try again next time!\nThe word was " + str(word),text_font = ("Calibri", 25),width = 100).place(x=125,y=300)
        wordscreen.after(3000, lambda: wordscreen.destroy())

    if len(entry1.get()) != 5:
        return
    else:
        life-= 1
    try:
        tries += 5
        
    except:
        tries =0
    
    if len(entry1.get()) == 5:
        try:
            num1 = word.index(entry1.get()[0])
        except:
            num1 = -1

        try:
            num2 = word.index(entry1.get()[1])
        except:
            num2 = -1
        
        try:
            num3 = word.index(entry1.get()[2])
        except:
            num3 = -1
        
        try:
            num4 = word.index(entry1.get()[3])
        except:
            num4 = -1

        try:
            num5 = word.index(entry1.get()[4])
        except:
            num5 = -1

        
        
        if entry1.get()[0] == word[0]:
            guess[0] = word[0]
            varlst[tries].configure(fg_color= 'green')
            customtkinter.CTkLabel(varlst[tries],text = guess[0], text_font = ("Calibri", 20),width = 30).place(x=0,y=2)
        elif num1 >= 0:
            guess[0] = entry1.get()[0]
            varlst[tries].configure(fg_color= '#f7c22f')
            customtkinter.CTkLabel(varlst[tries],text = guess[0],text_font = ("Calibri", 20),width = 30).place(x=0,y=2)
        else:
            guess[0] = entry1.get()[0]
            customtkinter.CTkLabel(varlst[tries],text = guess[0], text_font = ("Calibri", 20),width = 30).place(x=0,y=2)

        if entry1.get()[1] == word[1]:
            guess[1] = word[1]
            varlst[tries+1].configure(fg_color= 'green')
            customtkinter.CTkLabel(varlst[tries+1],text = guess[1], text_font = ("Calibri", 20),width = 30).place(x=0,y=2)
        elif num2 >= 0:
            guess[1] = entry1.get()[1]
            varlst[tries+1].configure(fg_color= '#f7c22f')
            customtkinter.CTkLabel(varlst[tries+1],text = guess[1], text_font = ("Calibri", 20),width = 30).place(x=0,y=2)
        else:
            guess[1] = entry1.get()[1]
            customtkinter.CTkLabel(varlst[tries+1],text = guess[1],text_font = ("Calibri", 20),width = 30).place(x=0,y=2)

        if entry1.get()[2] == word[2]:
            guess[2] = word[2]
            varlst[tries+2].configure(fg_color= 'green')
            customtkinter.CTkLabel(varlst[tries+2],text = guess[2], text_font = ("Calibri", 20),width = 30).place(x=0,y=2)
        elif num3 >= 0:
            guess[2] = entry1.get()[2]
            varlst[tries+2].configure(fg_color= '#f7c22f')
            customtkinter.CTkLabel(varlst[tries+2],text = guess[2], text_font = ("Calibri", 20),width = 30).place(x=0,y=2)
        else:
            guess[2] = entry1.get()[2]
            customtkinter.CTkLabel(varlst[tries+2],text = guess[2],text_font = ("Calibri", 20),width = 30).place(x=0,y=2)

        if entry1.get()[3] == word[3]:
            guess[3] = word[3]
            varlst[tries+3].configure(fg_color= 'green')
            customtkinter.CTkLabel(varlst[tries+3],text = guess[3], text_font = ("Calibri", 20),width = 30).place(x=0,y=2)
        elif num4 >= 0:
            guess[3] = entry1.get()[3]
            varlst[tries+3].configure(fg_color= '#f7c22f')
            customtkinter.CTkLabel(varlst[tries+3],text = guess[3], text_font = ("Calibri", 20),width = 30).place(x=0,y=2)
        else:
            guess[3] = entry1.get()[3]
            customtkinter.CTkLabel(varlst[tries+3],text = guess[3],  text_font = ("Calibri", 20),width = 30).place(x=0,y=2)

        if entry1.get()[4] == word[4]:
            guess[4] = word[4]
            varlst[tries+4].configure(fg_color= 'green')
            customtkinter.CTkLabel(varlst[tries+4],text = guess[4], text_font = ("Calibri", 20),width = 30).place(x=0,y=2)
        elif num5 >= 0:
            guess[4] = entry1.get()[4]
            varlst[tries+4].configure(fg_color= '#f7c22f')
            customtkinter.CTkLabel(varlst[tries+4],text = guess[4], text_font = ("Calibri", 20),width = 30).place(x=0,y=2)
        else:
            guess[4] = entry1.get()[4]
            customtkinter.CTkLabel(varlst[tries+4],text = guess[4],  text_font = ("Calibri", 20),width = 30).place(x=0,y=2)

    if entry1.get()[0] == word[0] and entry1.get()[1] == word[1] and entry1.get()[2] == word[2] and entry1.get()[3] == word[3] and entry1.get()[4] == word[4]:
        guessaword.destroy()
        customtkinter.CTkLabel(wordscreen, text='Congrats, you got it right!',width=100,text_font = ("Calibri", 30)).place(x=50,y=300)
        score += 10
        wordscreen.after(3000, lambda: wordscreen.destroy())
        
        
        
    entry1.delete(0, 'end')

main()
