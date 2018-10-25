from tkinter import *
import time
#=====================create window===================
root=Tk()
root.title("calc")
root.geometry('400x400')
def display(value):   
    global s
    s=s+value
    text.set(s)
def result():
    global s
    try:
        s=str(eval(text.get()))  #calculate the result
        text.set(s)
    except Exception as e:
        s=''
        text.set(e)
def counter_label():
    label.config(text=time.ctime())
    label.after(1000,counter_label)
def clear():
    global s
    s=''
    text.set(s)
def clear1():
    global s
    s=s[:len(s)-1]
    text.set(s)

counter=0
s=''
text=StringVar()
f=Frame(root) #create frame in window
e1=Entry(f,bg='powderblue',relief=RAISED,textvariable=text,bd=5,font=('arial',20,'bold'),justify='right',width=25) #entry is use to put the values and show the results in calculater
e1.grid(padx=5,pady=5,columnspan=4,sticky='NSWE')
s1=['789/','456*','123+','.0-'] 
k=1
for i in s1:
    l=0
    for j in i:
        b=Button(f,text=j,bg='powder blue',bd=5,width=3,font=('arial',20,'bold'),command=lambda x=j:display(x))
        b.grid(row=k,column=l,sticky='NSWE')
        l=l+1
    k=k+1
b=Button(f,text='=',bg='powder blue',bd=5,width=3,font=('arial',20,'bold'),command=result) #create Button
b.grid(row=4,column=3,sticky='NSWE')                                                       #grid is use to set the location of button
b=Button(f,text='c',bg='powder blue',bd=5,width=3,font=('arial',20,'bold'),command=clear)
b.grid(row=5,column=0,columnspan=2,sticky='NSWE')
b=Button(f,text='ce',bg='powder blue',bd=5,width=3,font=('arial',20,'bold'),command=clear1)
b.grid(row=5,column=2,columnspan=2,sticky='NSWE')
label=Label(f,font=('arial',20,'bold'),bg='powder blue',bd=15,height=2)
label.grid(row=6,column=0,columnspan=4,sticky='NSWE') 
counter_label()        #call counter_label function
f.pack(fill=BOTH,expand=YES)

root.mainloop()   
