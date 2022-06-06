#this is my first project in python
#rock paper scissor
from tkinter import *
import random

rps=Tk()
rps.geometry("300x340")
rps.title("Rock-Paper-Scissor")

user_score=0
comp_score=0
user_choice=""
comp_choice=""

def choicetonumber(choice):
    rps ={"rock":0,"paper":1,"scissor":2}
    a=rps[choice]
    return a

def numbertochoice(number):
    rps ={0:"rock",1:"paper",2:"scissor"}
    a = rps[number]
    return a


#final result
def result(human_choice,com_choice):
    global user_score
    global comp_score
    user = choicetonumber(human_choice)
    comp = choicetonumber(com_choice)
    if (user==comp):
        print("TIE")
        str="TIE"
    elif((user-comp)%3==1):
        print("YOU WIN")
        user_score += 1
        str = "YOU WINS"
    else:
        print("COMPUTER WINS")
        comp_score+=1
        str="COMPUTER WINS"
    text_area = Text(master =rps,font=("arial",15,"italic bold "),relief=RIDGE,bg="aqua",fg="darkslategrey",width=26)
    text_area.grid(column =0,row=4)
    answer="{win}  \n\nYOUR CHOICE :  {uc} \nCOMPUTER CHOICE : {cc} \n\nYOUR SCORE : {u} \nCOMPUTER SCORE : {c}".format(win=str,uc= user_choice,cc=comp_choice,u=user_score,c=comp_score)
    text_area.insert(END,answer)

def rock():
    global user_choice
    global comp_choice
    user_choice="rock"
    comp_choice= random.choice(["rock","paper","scissor"])
    result(user_choice,comp_choice)

def scissor():
    global user_choice
    global comp_choice
    user_choice="scissor"
    comp_choice= random.choice(["rock","paper","scissor"])
    result(user_choice,comp_choice)


def paper():
    global user_choice
    global comp_choice
    user_choice = "paper"
    comp_choice = random.choice(["rock","paper","scissor"])
    result(user_choice,comp_choice)



#creating labels and buttons
button_rock= Button(text="             ROCK                  ",bg="brown",font = ("arial",15,"italic bold"),relief=RIDGE, activebackground="#059458", activeforeground="white",
                            width=24,command =rock)
button_rock.grid(column =0,row=1)
button_paper= Button(text="             PAPER                  ",bg="yellow",font = ("arial",15,"italic bold"),relief=RIDGE, activebackground="#059458", activeforeground="white",
                            width=24,command =paper)
button_paper.grid(column =0,row=2)
button_scissor= Button(text="             SCISSORS                 ",bg="hotpink",font = ("arial",15,"italic bold"),relief=RIDGE, activebackground="#059458", activeforeground="white",
                            width=24,command =scissor)
button_scissor.grid(column =0,row=3)

rps.mainloop()
