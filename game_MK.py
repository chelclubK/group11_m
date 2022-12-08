from tkinter import Tk, Label, PhotoImage
from random import shuffle
from tkinter import messagebox as mb
Rlist=[[1,4,3,6,8],
       [2,4,9,5,7],
       [1,2,3,8,6],
       [0,9,5,7,0]]

shuffle(Rlist)
k=0
otknochka=Tk()
otknochka.title('Memory')
otknochka.resizable(False,False)
state0=PhotoImage(file='pict/Ничего1.png')
fon=PhotoImage(file='pict/Ничего.png')
kartuna=[]
for i in range(10):
        obj=PhotoImage(file='pict/'+str(i)+'.png')
        kartuna.append(obj)

def click(e):
    global k, x1, y1, x2, y2
    kart=e.widget
    xte=kart.grid_info()
    x=xte['column']
    y=xte['row']
    state=kart['text']
    if state== 'close' :
        if k==2:
            if Rlist[y2][x2]==Rlist[y1][x1]:
                #mb.showinfo('information','ЕЕСССТТТЬЬЬЬ!!!!')
                lamp[y1][x1].config(image=fon, text='get')
                lamp[y2][x2].config(image=fon, text='get')
            else:
                #mb.showinfo('information','Неа(((')
                lamp[y1][x1].config(image=state0, text='close')
                lamp[y2][x2].config(image=state0, text='close')
            k=0
        if k==0:
            q=Rlist[y][x]
            kart.config(image=kartuna[q], text='open')
            k=1
            x1=x
            y1=y
        elif k==1:
            q=Rlist[y][x]
            kart.config(image=kartuna[q], text='open')
            k=2
            x2=x
            y2=y

lamp=[]
for i in range(4):
    W=[]
    for j in range(5):
        obj=Label(otknochka,image=state0,text='close')
        obj.grid(row=i,column=j)
        obj.bind('<Button-1>',click)
        W.append(obj)
    lamp.append(W)


otknochka.mainloop()
