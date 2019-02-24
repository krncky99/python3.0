#python program for stop watch using tkinter module
from tkinter import *
root=Tk()
root.title("StopWatch")
root.minsize(width=250,height=70)
global counter
counter=-1
#start function for start watch
def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
def counter_label(label):
    def count():
        if running:
            global counter
            #TO manage the intial delay
            if counter ==-1:
                display="starting..."
            else:
                display=str(counter)
            label['text']=display
            label.after(1000,count)
            counter+=1
    count()
#stop function to stop the watch
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running=False
#reset fuction to reset the watch
def Reset(label):
    global counter
    counter=-1
    #if reset is press after press stop
    if running==False:
        reset['state']='disabled'
        label['text']='Welcome!'
    #if reset is press while the stopwatch is running.
    else:
        label['text']='starting...'
        
    
#Front GUI          
label=Label(root,text="Welcome!",fg="Black",font="arial 20 bold")
label.pack()
start=Button(root,text='start',width=15,command=lambda:Start(label))
stop=Button(root,text='stop',width=15,state='disabled',command=Stop)
reset=Button(root,text='reset',width=15,state='disabled',command=lambda:Reset(label))
start.pack()
reset.pack()
stop.pack()
root.mainloop()
           
