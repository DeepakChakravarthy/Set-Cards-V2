import sys
import os
from tkinter import * 
import tkinter
import pygame
from PIL import ImageTk, Image
def box():
    from tkinter import messagebox
    top.withdraw()
    import demo
    
    messagebox.showinfo("SET - CARDS", "Thank You")
def howplay():
    os.system("howtopay.mp4")
top= Tk()
pygame.init()
top.title("Set-cards")

img = ImageTk.PhotoImage(Image.open('Mainbackground.png'))

w = Label(top,image = img)
pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play()
w.pack(side = "bottom", fill = "both", expand = "yes")
w = Label(top,text="SET CARD GAME ",font =('SET CARD GAME',20))
w.pack()

top.geometry("1366x768")
top.config(bg='black')
resetbtn = Button(top, text = "Existing User",command =box ,activebackground = "green", activeforeground = "aqua").place(x = 1200, y = 100)
sbmitbtn = Button(top, text = "NEW USER",command = box,activebackground = "green", activeforeground = "aqua").place(x = 1200, y = 50)
hwplay = Button(top, text = "How To Play",command =howplay,activebackground = "green", activeforeground = "aqua").place(x = 1200, y = 150)
w.config(bg='green')
w.config(fg='white')
top.mainloop()