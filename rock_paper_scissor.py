# creating a rock paper scissor program
import random
list = ['rock','paper','scissor']

u = []
c = []

print("************************")
print("**ROCK**PAPER**SCISSOR**")
print("************************")
print("This is a code for playing 'Rock Paper Scissor'")


def Rock(x,u,c):
    if x == 'rock':
        print("The computer has selected rock \nIt is a tie")
        
    elif x == 'paper':
        print("The computer has selected paper \nThe computer has won")
        c.append(1)
        
    elif x == 'scissor':
        print("The computer has selected scissor \nYou have won")
        u.append(1)
        


def Paper(x,u,c):
    if x == 'rock':
        print("The computer has selected rock \nYou have won")
        u.append(1)

    elif x == 'paper':
        print("The computer has selected paper \nIt is a tie")

    elif x == 'scissor':
        print("The computer has selected scissor \nThe computer has won")
        u.append(1)

def Scissor(x,u,c):
    if x == 'rock':
        print("The computer has selected rock \nThe computer has won")
        c.append(1)
        
    elif x == 'paper':
        print("The computer has selected paper \nYou have won")
        u.append(1)

    elif x == 'scissor':
        print("The computer has selected scissor \nIt is a tie")
        

def play(y):
    if y.lower() == 'rock':
        Rock(x,u,c)
    if y.lower() == 'scissor':
        Scissor(x,u,c)
    if y.lower() == 'paper':
        Paper(x,u,c)

w = 0
while(w<5):
    x = random.choice(list)
    y = input("Enter your choice : ")
    play(y)
    w+=1

print("score user:",len(u),"computer:",len(c))

if len(u)>len(c):
    print("You win")
else: 
    print("You loose")

