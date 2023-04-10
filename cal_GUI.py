#Scientific Calculator


from tkinter import *

from tkinter import messagebox
import math

def enter(e):
    et_displayScreen.configure(bg='red')
def leave(e):
    et_displayScreen.configure(bg='yellow')


######################################Binding Function######################################
def on_enter7(e):
    bt_7.configure(bg='red')
def on_leave7(e):
    bt_7.configure(bg='powder blue')


def on_enter8(e):
    bt_8.configure(bg='red')
def on_leave8(e):
    bt_8.configure(bg='powder blue')

def on_enter9(e):
    bt_9.configure(bg='red')
def on_leave9(e):
    bt_9.configure(bg='powder blue')

def on_enter4(e):
    bt_4.configure(bg='red')
def on_leave4(e):
    bt_4.configure(bg='powder blue')


def on_enter5(e):
    bt_5.configure(bg='red')
def on_leave5(e):
    bt_5.configure(bg='powder blue')

def on_enter6(e):
    bt_6.configure(bg='red')
def on_leave6(e):
    bt_6.configure(bg='powder blue')


def on_enter1(e):
    bt_1.configure(bg='red')
def on_leave1(e):
    bt_1.configure(bg='powder blue')


def on_enter2(e):
    bt_2.configure(bg='red')
def on_leave2(e):
    bt_2.configure(bg='powder blue')


def on_enter3(e):
    bt_3.configure(bg='red')
def on_leave3(e):
    bt_3.configure(bg='powder blue')


def on_enter0(e):
    bt_0.configure(bg='red')
def on_leave0(e):
    bt_0.configure(bg='powder blue')


def on_enterC(e):
    bt_C.configure(bg='red')
def on_leaveC(e):
    bt_C.configure(bg='powder blue')


def on_enteradd(e):
    bt_add.configure(bg='red')
def on_leaveadd(e):
    bt_add.configure(bg='powder blue')



def on_entersub(e):
    bt_sub.configure(bg='red')
def on_leavesub(e):
    bt_sub.configure(bg='powder blue')

def on_entermul(e):
    bt_mul.configure(bg='red')
def on_leavemul(e):
    bt_mul.configure(bg='powder blue')

def on_enterdiv(e):
    bt_div.configure(bg='red')
def on_leavediv(e):
    bt_div.configure(bg='powder blue')

def on_entersin(e):
    bt_sin.configure(bg='red')
def on_leavesin(e):
    bt_sin.configure(bg='powder blue')

def on_entercos(e):
    bt_cos.configure(bg='red')
def on_leavecos(e):
    bt_cos.configure(bg='powder blue')

def on_entersqrt(e):
    bt_sqrt.configure(bg='red')
def on_leavesqrt(e):
    bt_sqrt.configure(bg='powder blue')

def on_entertan(e):
    bt_tan.configure(bg='red')
def on_leavetan(e):
    bt_tan.configure(bg='powder blue')

def on_enterlog(e):
    bt_log.configure(bg='red')
def on_leavelog(e):
    bt_log.configure(bg='powder blue')

def on_enterequal(e):
    bt_equal.configure(bg='red')
def on_leaveequal(e):
    bt_equal.configure(bg='powder blue')


#main program with screen-------------------------------------------------------------------------

root = Tk()
root.configure(bg='blue')
root.title('Scientific Calculator')
root.maxsize(width=325,height=315)
root.minsize(width=262,height=315)
root.geometry('262x315')
# root.resizable(width=False,height=False)

root.iconbitmap('calcicon.ico')

# root.geometry('365x490')
def click(number):
    global operator
    operator +=str(number)
    tex.set(operator)

def clear():
    global operator
    operator=''
    tex.set(operator)

def equal():
    global operator
    try:
        result=eval(operator)
        operator=str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification','Try again Something is wrong here',
        parent=root)

def cmsin():
    global operator
    try:
        # result=math.sin(eval(tex.get()))
        result=math.sin(math.radians(float(tex.get())))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try again Something is Wrong here',parent=root)

def cmcos():
    global operator
    try:
        # result=math.cos(eval(tex.get()))
        result = math.cos(math.radians(float(tex.get())))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try again Something is Wrong here',parent=root)

def cmtan():
    global operator
    try:
        # result=math.tan(eval(tex.get()))
        result = math.tan(math.radians(float(tex.get())))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try again Something is Wrong here',parent=root)

def cmlog():
    global operator
    try:
        # result=math.log(eval(tex.get()))
        result = math.log(float(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try again Something is Wrong here',parent=root)

def cmsqrt():
    global operator
    try:
        result=math.sqrt(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try again Something is Wrong here',parent=root)








##########################################main program######################################################
tex=StringVar()
operator=''
et_displayScreen = Entry(root, bg='yellow', bd=20, font=('arail', 15, 'bold'),
                    justify='right',relief=SUNKEN, textvariable=tex)
et_displayScreen.focus_set()
#, insertwidth=5,insertbackground='red',justify='right'

#bt_7=Button(root, text='7',bg='#FFEBCD',bd=5,activebackground='green',relief=RAISED,font=('arail',12,'bold'),
#            activeforeground='white',height=1,width=3 )



bt_7=Button(root, text='7',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click(7) )

bt_7.grid(row=1,column=0)

bt_8=Button(root, text='8',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click(8) )

bt_8.grid(row=1,column=1)

bt_9=Button(root, text='9',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click(9) )
bt_9.grid(row=1,column=2)

bt_sin=Button(root, text='sin',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=cmsin )
bt_sin.grid(row=0,column=4)

bt_4=Button(root, text='4',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click(4) )
bt_4.grid(row=2,column=0)

bt_5=Button(root, text='5',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click(5) )
bt_5.grid(row=2,column=1)

bt_6=Button(root, text='6',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click(6) )
bt_6.grid(row=2,column=2)

bt_cos=Button(root, text='cos',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=cmcos )
bt_cos.grid(row=1,column=4)

bt_1=Button(root, text='1',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click(1) )
bt_1.grid(row=3,column=0)

bt_2=Button(root, text='2',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click(2) )
bt_2.grid(row=3,column=1)

bt_3=Button(root, text='3',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click(3) )
bt_3.grid(row=3,column=2)

bt_tan=Button(root, text='tan',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=cmtan )
bt_tan.grid(row=2,column=4)

bt_0=Button(root, text='0',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click(0) )
bt_0.grid(row=4,column=0)

bt_C=Button(root, text='C',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=clear )
bt_C.grid(row=4,column=1)

bt_equal=Button(root, text='=',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=equal)
bt_equal.grid(row=4,column=2)

bt_sqrt=Button(root, text='sqrt',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=cmsqrt )
bt_sqrt.grid(row=3,column=4)

bt_log=Button(root, text='log',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=cmlog )
bt_log.grid(row=4,column=4)

bt_add=Button(root, text='+',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click('+') )
bt_add.grid(row=1,column=3)

bt_sub=Button(root, text='-',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click('-') )
bt_sub.grid(row=2,column=3)

bt_mul=Button(root, text='*',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click('*') )
bt_mul.grid(row=3,column=3)

bt_div=Button(root, text='/',bg='powder blue',bd=8,activebackground='green',relief=RAISED,font=('arail',12,'bold italic'),
           activeforeground='white',height=2,width=4,command=lambda:click('/') )
bt_div.grid(row=4,column=3)

#
# et_displayScreen.grid(row=0,column=0,columnspan=4)
#
# root.mainloop()

###################################### Binding ######################################
et_displayScreen.bind('<Enter>',enter)
et_displayScreen.bind('<Leave>',leave)

bt_7.bind('<Enter>',on_enter7)
bt_7.bind('<Leave>',on_leave7)

bt_8.bind('<Enter>',on_enter8)
bt_8.bind('<Leave>',on_leave8)

bt_9.bind('<Enter>',on_enter9)
bt_9.bind('<Leave>',on_leave9)

bt_4.bind('<Enter>',on_enter4)
bt_4.bind('<Leave>',on_leave4)

bt_5.bind('<Enter>',on_enter5)
bt_5.bind('<Leave>',on_leave5)

bt_6.bind('<Enter>',on_enter6)
bt_6.bind('<Leave>',on_leave6)

bt_1.bind('<Enter>',on_enter1)
bt_1.bind('<Leave>',on_leave1)

bt_2.bind('<Enter>',on_enter2)
bt_2.bind('<Leave>',on_leave2)

bt_3.bind('<Enter>',on_enter3)
bt_3.bind('<Leave>',on_leave3)

bt_add.bind('<Enter>',on_enteradd)
bt_add.bind('<Leave>',on_leaveadd)

bt_sub.bind('<Enter>',on_entersub)
bt_sub.bind('<Leave>',on_leavesub)

bt_mul.bind('<Enter>',on_entermul)
bt_mul.bind('<Leave>',on_leavemul)

bt_div.bind('<Enter>',on_enterdiv)
bt_div.bind('<Leave>',on_leavediv)

bt_sin.bind('<Enter>',on_entersin)
bt_sin.bind('<Leave>',on_leavesin)

bt_cos.bind('<Enter>',on_entercos)
bt_cos.bind('<Leave>',on_leavecos)

bt_tan.bind('<Enter>',on_entertan)
bt_tan.bind('<Leave>',on_leavetan)

bt_sqrt.bind('<Enter>',on_entersqrt)
bt_sqrt.bind('<Leave>',on_leavesqrt)

bt_C.bind('<Enter>',on_enterC)
bt_C.bind('<Leave>',on_leaveC)

bt_equal.bind('<Enter>',on_enterequal)
bt_equal.bind('<Leave>',on_leaveequal)

bt_log.bind('<Enter>',on_enterlog)
bt_log.bind('<Leave>',on_leavelog)

et_displayScreen.grid(row=0,column=0,columnspan=4)

root.mainloop()
