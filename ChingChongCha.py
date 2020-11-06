from tkinter import *
from tkinter import messagebox
import random
#from PIL import ImageTk,Image
 
# global score variables
# wins losses ties
w = 0
l = 0
t = 0
 
 
# decides the winner
# called by rock, paper and scissors buttons
# p = player choice either rock, paper or scissors
def game(p):
 
    global w
    global l
    global t
 
    # getting the computers choice
    c = ['rock', 'paper', 'scissors']
    c = random.choice(c)
 
    # seeing who won by checking c (computer choice) to p (player choice)
    if p == c:
        r = 'tied'
    elif (p == 'rock' and c == 'paper') or (p == 'paper' and c == 'scissors') or (p == 'scissors' and c == 'rock'):
        r = 'lost'
    else:
        r = 'won'
 
    if r == 'tied':
        t += 1
    elif r == 'lost':
        l += 1
    else:
        w += 1
 
    # updating the labels that display the last rounds results and the score
    lbl_result['text'] = 'You %s! You played %s, the computer played %s.' % (r, p, c)
    lbl_score['text'] = 'Score:\nYou: %s     Computer: %s     Ties: %s' % (w, l, t)
 
 
# resets the score, called by the reset toolbar button thingy
# sets w l t to zero then updates the labels
def reset():
    global w
    global l
    global t
    w = 0
    l = 0
    t = 0
 
    lbl_score['text'] = 'Score:\nYou: %s          Computer: %s          Ties: %s' % (w, l, t)
    lbl_result['text'] = 'Good Luck!'
  
def ex():
    msg=messagebox.askyesno('Confirm',"Are You sure", icon='warning')
    if msg==YES:
        root.destroy()
# gui maker parts
root = Tk()
 
# window properties
root.wm_title("Rock Paper Scissors")
 
root.iconbitmap(default='icon.ico') 
lbl_result = Label(root, text='Good Luck!', font=('Comic Sans MS', 10, 'bold'))
lbl_result.grid(row=0, column=1)
 
lbl_score = Label(root, text='Score:\nYou: 0          Computer: 0          Ties: 0', font=('Comic Sans MS', 10, 'bold'))
lbl_score.grid(row=1, column=0)
 
# buttons, rock, paper and scissors
photo=PhotoImage(file="stone.gif")

photo = photo.subsample(11,9)

st = Button(root, text='Stone', bg='grey', width=215, height=270, command=lambda: game('rock'), image = photo, compound= LEFT, font=('Comic Sans Ms',20,'italic'))
st.grid(row=2, column=0, pady=20)

phpr=PhotoImage(file='paper.gif')

phpr = phpr.subsample(3,3)

pr = Button(root, text='Paper', bg='white', width=215, height=270, command=lambda: game('paper'), image = phpr, compound = LEFT, font=('Comic Sans Ms',20,'italic'))
pr.grid(row=2, column=1, padx=(10, 20))

phsc = PhotoImage(file='sci.gif')

phsc = phsc.subsample(3,3)

sci = Button(root, text='Scissors', bg='silver', width=215, height=270, command=lambda: game('scissors'), image=phsc, compound = LEFT, font=('Comic Sans Ms',20,'italic'))
sci.grid(row=2, column=2, padx=(10, 20))

#adding menubar
menubar=Menu(root)
root.config(menu=menubar)
gameoption=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Game Options', menu=gameoption)
gameoption.add_command(label='Play Again', command=reset)
gameoption.add_command(label='Exit', command=ex)

root.geometry("850x400+200+50") 
root.mainloop()