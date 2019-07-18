import sys
from tkinter import * 
import tkinter

from PIL import ImageTk, Image
def box():
    from tkinter import messagebox
    
    messagebox.showinfo("SET CARDS Registering", "Thank You For Registering\n\n Please Choose Your Level\n\nEnjoy Playing")
    FullName = var1.get()
    NickName = var2.get()
    f = open("user.txt","w")
    f.write("%s <= FULL NAME \n"%FullName)
    f.write("%s <= NICK NAME \n"%NickName)
    f.close()
    print(FullName)
    print(NickName)
def clear():
    e1 = Entry(top).place(x = 250, y = 218)  
    e2 = Entry(top).place(x = 250, y = 300)  
def beginner():
    top.withdraw()
    import FIRSTL
    
def Intermediate():
    top.withdraw()
    import THIRDL
def ProPlayer():
    top.withdraw()
    import FOURTHL
top= Tk()
var1 = StringVar()#declaring the variable to store the text
var2 = StringVar()#.....\....\...
top.title("Set-cards Registering")
#img = ImageTk.PhotoImage(Image.open('db.png'))
#w = Label(top,image = img)
#w.pack(side = "bottom", fill = "both", expand = "yes")
#w = Label(top,text="SET CARD GAME ",font =('SET CARD GAME',20))
#w.pack()
top.geometry("1366x768")
top.config(bg='black')
name = Label(top, text = "Full Name",font = 'Algerian 15 bold',background = "black",fg = "white").place(x = 116,y = 215)
nick = Label(top, text = "NickName",font = 'Algerian 15 bold',background = "black",fg = "white").place(x = 116,y = 300)
Level = Label(top,text = "Choose Your Level To Play",font = 'Algerian  15 bold italic underline',background = "Green",fg = "white").place(x = 999, y = 216)
resetbtn = Button(top, text = "   Reset   ",command =clear ,font = 'HarlowSolidItalic 14 bold italic',background = "blue",foreground = "White").place(x = 116, y = 400)
sbmitbtn = Button(top, text = " Continue ",command = box,font = 'HarlowSolidItalic 14 bold italic',background = "blue",foreground = "white").place(x = 260, y = 400)
easybtn = Button(top, text = "BEGINNER",command =beginner ,font = 'Algerian 14 bold underline',background = "black",fg = "white").place(x = 1120, y = 260)
easybtn = Button(top, text = "INTERMEDIATE",command =Intermediate ,font = 'Algerian 14 bold underline',background = "black",fg = "blue").place(x = 1120, y = 330)
easybtn = Button(top, text = "PRO PLAYER",command =ProPlayer ,font = 'Algerian 14 bold underline',background = "black",fg = "red").place(x = 1120, y = 400)
e1 = Entry(top,textvariable= var1).place(x = 250, y = 218)  
e2 = Entry(top,textvariable = var2).place(x = 250, y = 300) 
#w.config(bg='green')
#w.config(fg='white')
top.config(cursor="star")
top.mainloop()