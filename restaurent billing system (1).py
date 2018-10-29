from tkinter import *
import tkinter.messagebox
root=Tk()
root.minsize(width=1300,height=700)
x=Label(root,text="restaurent billing",bg="darkviolet",relief=RAISED,font=("arial",15,'bold'),height=2)
x.pack(fill=BOTH)
canvas=Canvas(root,bg="darkgrey")
canvas.pack(side=BOTTOM,fill=BOTH,expand=YES)
mainframe=Frame(canvas,bg="black",relief=RAISED,bd=10)#scroll
mainframe.pack(side=TOP,expand=YES,fill=BOTH)
scrollbar = Scrollbar(canvas)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=canvas.yview)
FR=Frame(mainframe,bg="brown",relief=RAISED,bd=10)
FR.pack(expand=YES,fill=BOTH)
fr1=Frame(FR,bg="blue",relief=RAISED,height=300,width=1000)
fr1.pack(side=LEFT,expand=YES,fill=BOTH)


fr11=Frame(fr1,bg="brown",height=200,width=100,bd=10)
fr11.pack(side=LEFT,expand=YES,fill=BOTH)
fr11a=Frame(fr11,bg="powder blue",relief=RAISED,height=45,width=500,bd=10)
fr11a.pack(side=TOP,expand=YES,fill=BOTH) 
fr11b=Frame(fr11,bg="powder blue",relief=RAISED,height=45,width=500,bd=10)
fr11b.pack(side=TOP,expand=YES,fill=BOTH)
fr11c=Frame(fr11,bg="powder blue",relief=RAISED,height=45,width=500,bd=10)
fr11c.pack(side=TOP,expand=YES,fill=BOTH)
fr11d=Frame(fr11,bg="powder blue",relief=RAISED,height=45,width=500,bd=10)
fr11d.pack(side=TOP,expand=YES,fill=BOTH)


fr1r=Frame(fr1,bg="brown",height=200,width=100,bd=10)
fr1r.pack(side=RIGHT,expand=YES,fill=BOTH)
fr1ra=Frame(fr1r,bg="powder blue",relief=RAISED,height=45,width=500,bd=10)
fr1ra.pack(side=TOP,expand=YES,fill=BOTH)
fr1rb=Frame(fr1r,bg="powder blue",relief=RAISED,height=45,width=500,bd=10)
fr1rb.pack(side=TOP,expand=YES,fill=BOTH)
fr1rc=Frame(fr1r,bg="powder blue",relief=RAISED,height=45,width=500,bd=10)
fr1rc.pack(side=TOP,expand=YES,fill=BOTH)
fr1rd=Frame(fr1r,bg="powder blue",relief=RAISED,height=45,width=500,bd=10)
fr1rd.pack(side=TOP,expand=YES,fill=BOTH)

fr2=Frame(FR,bg="brown",height=300,width=300,bd=10) # receipt frame
fr2.pack(side=RIGHT,expand=YES,fill=BOTH)
l=Label(fr2,text="Reciept",relief=RAISED,font=("arial",10,'bold'),fg="WHITE",bg="black",bd=8)
l.pack(expand=YES,fill=BOTH)
t=Text(fr2,height=30,width=20)
t.pack(expand=YES,fill=BOTH)

#------------------------------------------------------------total---------------------------------------------------------------------------
def total():
    t.insert(END,'itemname'+'\t\t'+'rate'+'\t\t'+'quantity'+'\t\t'+'cost'+'\n')
    total=0
    for i in range(len(ITEMS)):
        if(int(ENTRIES[i].get())==0):
            t.insert(END,'')
            
        else:
            a=int(ENTRIES[i].get())*int(ITEMSCOST[i])
            t.insert(END,ITEMS[i].strip()+"\t\t"+ITEMSCOST[i]+'\t\t'+(ENTRIES[i].get())+'\t\t'+str(a)+'\n')
            total=total+a
    t.insert(END,'\n\n'+'\t\t\t\t'+'total='+"\t\t"+str(total))
   
#----------------------------------------------------------------------reset-------------------------------------------------------------------------

def reset():
    t.delete('1.0',END)
    for i in range(len(ITEMS)):
        ENTRIES[i].delete(0,END)
        ENTRIES[i].insert(END,'0')
  
   
   
#------------------------------------------------------textfieldbuttons--------------------------------------------------------------------------------    
bttn=Button(fr2,text="total",relief=RAISED,bg="darkgrey",fg="black",font=("arial",10,"bold"),borderwidth=3,command=total)
bttn.pack(side=LEFT,expand=YES,fill=BOTH,ipadx=2,ipady=2)
bttn=Button(fr2,text="receipt",relief=RAISED,bg="darkgrey",fg="black",font=("arial",10,"bold"),borderwidth=3)
bttn.pack(side=LEFT,expand=YES,fill=BOTH,ipadx=2,ipady=2)
bttn=Button(fr2,text="reset",relief=RAISED,bg="darkgrey",fg="black",font=("arial",10,"bold"),borderwidth=3,command=reset)
bttn.pack(side=LEFT,expand=YES,fill=BOTH,ipadx=2,ipady=2)

#---------------------------------------------------------------------lists------------------------------------------------------------------------------

    
FRAMES=[]    
ENTRIES=[]
ITEMS=[]
ITEMSCOST=[]

# values of  pizza


def additem1():
    f=(Frame(fr11a))
    fr.append(f)
    FRAMES.append(f)
    f.pack(expand=YES,fill=BOTH)
    x1=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x1.pack(side=LEFT,expand=YES,fill=BOTH)
    items1.append(x1)
    x2=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x2.pack(side=LEFT,expand=YES,fill=BOTH)
    itemscost1.append(x2)
    
def ok1():
    y=items1[len(items1)-1].get()
    y1=itemscost1[len(itemscost1)-1].get()
    items1[len(items1)-1].destroy()
    itemscost1[len(itemscost1)-1].destroy()
    l=Label(FRAMES[len(FRAMES)-1],text=y,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMS.append(y)
    l=Label(FRAMES[len(FRAMES)-1],text=y1,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMSCOST.append(y1)
    x=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)

   
    
    
x=Label(fr11a,text="PIZZA",bg="darkgrey")
x.pack(fill=BOTH)
b=Button(x,text="additem",command=additem1)
b.pack(side=LEFT)
b=Button(x,text="ok",command=ok1)
b.pack(side=LEFT)
l=["vegetable     ","cheese         ","double          ","mushroom  "]
l1=["80","85","90","99"]
fr=[]
items1=[]
itemscost1=[]
for i in range(4):
    fr.append(Frame(fr11a))
    FRAMES.append(Frame(fr11a))
    fr[i].pack(expand=YES,fill=BOTH)
    x=Label(fr[i],text=l[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    items1.append(x)
    ITEMS.append(l[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Label(fr[i],text=l1[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    itemscost1.append(x)
    ITEMSCOST.append(l1[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Entry(fr[i],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
  
   

# values of  Burger
def additem2():
    f=(Frame(fr11b))
    fr.append(f)
    FRAMES.append(f)
    f.pack(expand=YES,fill=BOTH)
    x1=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x1.pack(side=LEFT,expand=YES,fill=BOTH)
    items2.append(x1)
    x2=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x2.pack(side=LEFT,expand=YES,fill=BOTH)
    itemscost2.append(x2)
    
    
def ok2():
    y=items2[len(items2)-1].get()
    y1=itemscost2[len(itemscost2)-1].get()
    items2[len(items2)-1].destroy()
    itemscost2[len(itemscost2)-1].destroy()
    l=Label(FRAMES[len(FRAMES)-1],text=y,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMS.append(y)
    l=Label(FRAMES[len(FRAMES)-1],text=y1,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMSCOST.append(y1)
    x=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)

   
   

x=Label(fr11b,text="Burger",bg="darkgrey")
x.pack(fill=BOTH)
b=Button(x,text="additem",command=additem2)
b.pack(side=LEFT)
b=Button(x,text="ok",command=ok2)
b.pack(side=LEFT)
l=["  vegetable  ","cheese       ","alootikki     ","cutlet          "]
l1=["80","85","90","99"]
fr=[]
items2=[]
itemscost2=[]

for i in range(4):
    f=Frame(fr11b)
    fr.append(f)
    FRAMES.append(f)
    fr[i].pack(expand=YES,fill=BOTH)
    x=Label(fr[i],text=l[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    items2.append(x)
    ITEMS.append(l[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Label(fr[i],text=l1[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    itemscost2.append(x)
    ITEMSCOST.append(l1[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Entry(fr[i],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)

   
    
   
y=0
y1=0
    
# values of pasta
def additem3():
    f=(Frame(fr11c))
    fr.append(f)
    FRAMES.append(f)
    f.pack(expand=YES,fill=BOTH)
    x1=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x1.pack(side=LEFT,expand=YES,fill=BOTH)
    items3.append(x1)
    
    x2=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x2.pack(side=LEFT,expand=YES,fill=BOTH)
    itemscost3.append(x2)
    
def ok3():
    y=items3[len(items3)-1].get()
    y1=itemscost3[len(itemscost3)-1].get()
    items3[len(items3)-1].destroy()
    itemscost3[len(itemscost3)-1].destroy()
    l=Label(FRAMES[len(FRAMES)-1],text=y,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMS.append(y)
    l=Label(FRAMES[len(FRAMES)-1],text=y1,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMSCOST.append(y1)
    x=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   
   

x=Label(fr11c,text="Pasta",bg="darkgrey")
x.pack(fill=BOTH)
b=Button(x,text="additem",command=additem3)
b.pack(side=LEFT)
b=Button(x,text="ok",command=ok3)
b.pack(side=LEFT)
l=["Red         ","white      ","meonize","chesse  "]
l1=["80","85","90","99"]
fr=[]
items3=[]
itemscost3=[]


for i in range(4):
    fr.append(Frame(fr11c))
    fr[i].pack(expand=YES,fill=BOTH)
    x=Label(fr[i],text=l[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    items3.append(x)
    ITEMS.append(l[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Label(fr[i],text=l1[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    itemscost3.append(x)
    ITEMSCOST.append(l1[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Entry(fr[i],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   
    
 

# values of soup
def additem4():  
 
    f=(Frame(fr11d))
    fr.append(f)
    FRAMES.append(f)
    f.pack(expand=YES,fill=BOTH)
    x1=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x1.pack(side=LEFT,expand=YES,fill=BOTH)
    items4.append(x1)
    x2=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x2.pack(side=LEFT,expand=YES,fill=BOTH)
    itemscost4.append(x2)
    
def ok4():
    y=items4[len(items4)-1].get()
    y1=itemscost4[len(itemscost4)-1].get()
    items4[len(items4)-1].destroy()
    itemscost4[len(itemscost4)-1].destroy()
    l=Label(FRAMES[len(FRAMES)-1],text=y,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMS.append(y)
    l=Label(FRAMES[len(FRAMES)-1],text=y1,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMSCOST.append(y1)
    x=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   
   


x=Label(fr11d,text="Soup",bg="darkgrey")
x.pack(fill=BOTH)
b=Button(x,text="additem",command=additem4)
b.pack(side=LEFT)
b=Button(x,text="ok",command=ok4)
b.pack(side=LEFT)
l=["tomato  ","corn       ","carrot   "," vegge   "]
l1=["80","85","90","99"]
fr=[]
items4=[] 
itemscost4=[]

for i in range(4):
    fr.append(Frame(fr11d))
    fr[i].pack(expand=YES,fill=BOTH)
    x=Label(fr[i],text=l[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    items4.append(x)
    ITEMS.append(l[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Label(fr[i],text=l1[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    itemscost4.append(x)
    ITEMSCOST.append(l1[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Entry(fr[i],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   
   

# values in munchurian
def additem5():  
   
    f=(Frame(fr1ra))
    fr.append(f)
    FRAMES.append(f)
    f.pack(expand=YES,fill=BOTH)
    x1=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x1.pack(side=LEFT,expand=YES,fill=BOTH)
    items5.append(x1)
    x2=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x2.pack(side=LEFT,expand=YES,fill=BOTH)
    itemscost5.append(x2)
    
def ok5():
    y=items5[len(items5)-1].get()
    y1=itemscost5[len(itemscost5)-1].get()
    items5[len(items5)-1].destroy()
    itemscost5[len(itemscost5)-1].destroy()
    l=Label(FRAMES[len(FRAMES)-1],text=y,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMS.append(y)
    l=Label(FRAMES[len(FRAMES)-1],text=y1,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMSCOST.append(y1)
    x=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   

x=Label(fr1ra,text="Munchurian",bg="darkgrey")
x.pack(fill=BOTH)
b=Button(x,text="additem",command=additem5)
b.pack(side=LEFT)
b=Button(x,text="ok",command=ok5)
b.pack(side=LEFT)
l=["gravy          ","dry              ","withrice     "," cheese     "]
l1=["80","85","90","99"]
fr=[]
items5=[] 
itemscost5=[]

for i in range(4):
    fr.append(Frame(fr1ra))
    fr[i].pack(expand=YES,fill=BOTH)
    x=Label(fr[i],text=l[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    items5.append(x)
    ITEMS.append(l[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Label(fr[i],text=l1[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    itemscost5.append(x)
    ITEMSCOST.append(l1[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Entry(fr[i],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   
# values in sandwich
def additem6():  
    f=(Frame(fr1rb))
    fr.append(f)
    FRAMES.append(f)
    f.pack(expand=YES,fill=BOTH)
    x1=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x1.pack(side=LEFT,expand=YES,fill=BOTH)
    items6.append(x1)
    x2=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x2.pack(side=LEFT,expand=YES,fill=BOTH)
    itemscost6.append(x2)

def ok6():
    y=items6[len(items6)-1].get()
    y1=itemscost6[len(itemscost6)-1].get()
    items6[len(items6)-1].destroy()
    itemscost6[len(itemscost6)-1].destroy()
    l=Label(FRAMES[len(FRAMES)-1],text=y,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMS.append(y)
    l=Label(FRAMES[len(FRAMES)-1],text=y1,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMSCOST.append(y1)
    x=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   

x=Label(fr1rb,text="sandwich",bg="darkgrey")
x.pack(fill=BOTH)
b=Button(x,text="additem",command=additem6)
b.pack(side=LEFT)
b=Button(x,text="ok",command=ok6)
b.pack(side=LEFT)
l=[" vegge        ","  grill           ","  jumbo       "," meonise   "]
l1=["80","85","90","99"]
fr=[]
items6=[] 
itemscost6=[]

for i in range(4):
    fr.append(Frame(fr1rb))
    fr[i].pack(expand=YES,fill=BOTH)
    x=Label(fr[i],text=l[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    items6.append(x)
    ITEMS.append(l[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Label(fr[i],text=l1[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    itemscost6.append(x)
    ITEMSCOST.append(l1[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Entry(fr[i],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   
   

# values in noodles
def additem7():  
   
    f=(Frame(fr1rc))
    fr.append(f)
    FRAMES.append(f)
    f.pack(expand=YES,fill=BOTH)
    x1=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x1.pack(side=LEFT,expand=YES,fill=BOTH)
    items7.append(x1)
    x2=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x2.pack(side=LEFT,expand=YES,fill=BOTH)
    itemscost7.append(x2)
    
def ok7():
    y=items7[len(items7)-1].get()
    y1=itemscost7[len(itemscost7)-1].get()
    items7[len(items7)-1].destroy()
    itemscost7[len(itemscost7)-1].destroy()
    l=Label(FRAMES[len(FRAMES)-1],text=y,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMS.append(y)
    l=Label(FRAMES[len(FRAMES)-1],text=y1,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMSCOST.append(y1)
    x=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   
  


x=Label(fr1rc,text="noodles",bg="darkgrey")
x.pack(fill=BOTH)
b=Button(x,text="additem",command=additem7)
b.pack(side=LEFT)
b=Button(x,text="ok",command=ok7)
b.pack(side=LEFT)
l=["   maggie   ","   hakka     ","chowmein"," yipeee      "]
l1=["80","85","90","99"]
fr=[]
items7=[] 
itemscost7=[]
for i in range(4):
    fr.append(Frame(fr1rc))
    fr[i].pack(expand=YES,fill=BOTH)
    x=Label(fr[i],text=l[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    items7.append(x)
    ITEMS.append(l[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Label(fr[i],text=l1[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    itemscost7.append(x)
    ITEMSCOST.append(l1[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Entry(fr[i],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   
  
# values in sizzler
def additem8():  
   
    f=(Frame(fr1rd))
    fr.append(f)
    FRAMES.append(f)
    f.pack(expand=YES,fill=BOTH)
    x1=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x1.pack(side=LEFT,expand=YES,fill=BOTH)
    items8.append(x1)
    x2=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x2.pack(side=LEFT,expand=YES,fill=BOTH)
    itemscost8.append(x2)
def ok8():
    y=items8[len(items8)-1].get()
    y1=itemscost8[len(itemscost8)-1].get()
    items8[len(items8)-1].destroy()
    itemscost8[len(itemscost8)-1].destroy()
    l=Label(FRAMES[len(FRAMES)-1],text=y,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMS.append(y)
    l=Label(FRAMES[len(FRAMES)-1],text=y1,font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    l.pack(side=LEFT,expand=YES,fill=BOTH)
    ITEMSCOST.append(y1)
    x=Entry(FRAMES[len(FRAMES)-1],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)
   
   
x=Label(fr1rd,text="sizzler",bg="darkgrey")
x.pack(fill=BOTH)
b=Button(x,text="additem",command=additem8)
b.pack(side=LEFT)
b=Button(x,text="ok",command=ok8)
b.pack(side=LEFT)
l=["vegetable ","    chinese ","         italian","     maxican"]
l1=["80","85","90","99"]
fr=[]  
items8=[] 
itemscost8=[]
for i in range(4):
    fr.append(Frame(fr1rd))
    fr[i].pack(expand=YES,fill=BOTH)
    x=Label(fr[i],text=l[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    items8.append(x)
    ITEMS.append(l[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Label(fr[i],text=l1[i],font=("arial",8,'bold'),justify=LEFT,relief=RAISED)
    itemscost8.append(x)
    ITEMSCOST.append(l1[i])
    x.pack(side=LEFT,expand=YES,fill=BOTH)
    x=Entry(fr[i],bg="white",font=("arial",8,"bold" ),relief=RAISED)
    x.insert(END,'0')
    ENTRIES.append(x)
    x.pack(side=LEFT,expand=YES,fill=BOTH)

   
  



root.mainloop()
