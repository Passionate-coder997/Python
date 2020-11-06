from tkinter import *
from tkinter import messagebox
from pytube import YouTube

def down():
	
	string=Entry.get(E1)
	messagebox.showinfo(win,string)

win = Tk()

lbl=Label(win, anchor=CENTER, text='Download any video from YouTube',font=('Comic Sans MS',20,'italic')).pack(padx=50, pady=20)
lbl1 = Label(win, text='Paste your link here:').place(x=150,y=100)
E1 = Entry(win, width=50).place(x=300, y=100)
btn=Button(win, text='Start Download', font=('None',15,'bold'),command=down).pack(side=BOTTOM)

win.geometry('800x300+100+50')
win.mainloop()