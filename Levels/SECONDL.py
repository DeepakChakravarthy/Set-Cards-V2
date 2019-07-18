import tkinter
from tkinter import *
from tkinter import messagebox
top= Tk()
top.withdraw()
from pygame.locals import *
def dc1 ():
    import pygame
    import sys
    c1=0
    c5=0
    c3=0
    pygame.init()
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.play()
    surface = pygame.display.set_mode((1366,768))
    black = (0,0,0)
    white = (255,255,255)
    background = pygame.image.load("Background 1.JPG")
    pygame.display.set_caption("SET-CARDS")
    gameIcon = pygame.image.load('ico.jpg')
    pygame.display.set_icon(gameIcon)
    imagerect = background.get_rect()
    size = ((140,70))
    card1_pink_diamond = pygame.image.load("1 PINK D DIA.png").convert()
    card1_pink_diamond = pygame.transform.scale(card1_pink_diamond, (150,200))
    card1_violet_diamond = pygame.image.load("1 BLUE D RECT.png").convert()
    card1_violet_diamond = pygame.transform.scale(card1_violet_diamond,(150,200))
    card1_green_diamond = pygame.image.load("2 BLUE D DIA.png").convert()
    card1_green_diamond = pygame.transform.scale(card1_green_diamond, (150,200))
    card1_blue_squigi = pygame.image.load("1 BLUE D SQUI.png").convert()
    card1_blue_squigi = pygame.transform.scale(card1_blue_squigi,(150,200))
    card2_violet_rect = pygame.image.load("2 BLUE D RECT.png").convert()
    card2_violet_rect = pygame.transform.scale(card2_violet_rect,(150,200))
    card3_violet_rect = pygame.image.load("3 BLUE D RECT.png").convert()
    card3_violet_rect = pygame.transform.scale(card3_violet_rect,(150,200))
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render("Level 2", True, (250, 80, 37))
    surface.blit(background,(0,0))
    font = pygame.font.SysFont("comicsansms", 25)
    text1 = font.render(" ", True, (255, 255,255))
    font = pygame.font.SysFont("comicsansms", 34)
    gameover = font.render(" ((GOOD)) ",True,(255,255,255))
    Wrong = font.render("((Try Again))",True,(255,255,255))
    Note = font.render("Find a Consecutive Cards",True,(255,255,255))
    top = (180,240)
    left = (123,30)
    width = 150
    height = 200
    width1 = 200
    height1 = 100
    width2 = 0
    height2 = 0
    red = 255,255,255
    brown = 193, 154, 107
    card1  = pygame.draw.rect(surface,black,(500,200,width,height))
    card3 = pygame.draw.rect(surface,black,(257,421,width,height))
    card5 = pygame.draw.rect(surface,black,(757,430,width,height))
    card2 = pygame.draw.rect(surface,black,(750,200,width,height))
    card4 = pygame.draw.rect(surface,black,(500,420,width,height))
    card = pygame.draw.rect(surface,black,(257,200,width,height))
    gameover1 = pygame.draw.rect(surface,black,(1120,68,width1,height1))
    lev = pygame.draw.rect(surface,black,(8,52,width2,height2))
    go = pygame.image.load("Continue.png")
    go = pygame.transform.scale(go, (100,100))
    b = pygame.draw.rect(surface,brown,(1120,555,102,100))
    r = pygame.image.load("Replay.png")
    r = pygame.transform.scale(r, (100,100))
    rb = pygame.draw.rect(surface,brown,(1120,400,102,100))
    while True:
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pressed1 and rb.collidepoint(pos):
                c1=0
                c5=0
                c3=0
                messagebox.showinfo("SET-CARDS","Reset is Done")
            if b.collidepoint(pos) and pressed1:
                if (c1 == 1 or c1 ==2  and c3 ==1 or c3 ==2 and c5 == 1 or c5==2):
                    messagebox.showinfo("SET-CARDS","SET IS DONE")
                    import THIRDL
                    surface.blit(gameover,gameover1)
                else:

                    response = messagebox.askquestion("SET - CARDS", "SET IS WRONG TRY AGAIN")
                    if (response=='yes'):
                        c1 = 0
                        c5 = 0
                        c3 = 0
                        messagebox.showinfo("SET-CARDS","Reset is Done")
                    else:
                        pygame.display.quit()
            if card5.collidepoint(pos) and pressed1:
                c1 += 1
                print("Correct")
            if card1.collidepoint(pos) and pressed1:

                print("Wrong")
            if card2.collidepoint(pos) and pressed1:
                print("Wrong")
            if card4.collidepoint(pos)and pressed1:
                c3 += 1
                print("Correct")
            if card3.collidepoint(pos)and pressed1:

                print("Wrong")
            if card.collidepoint(pos)and pressed1:
                c5 += 1
                print("Correct")
        surface.blit(card1_pink_diamond,card1)
        surface.blit(card1_green_diamond,card3)
        surface.blit(card1_violet_diamond,card5)
        surface.blit(card1_blue_squigi,card2)
        surface.blit(card2_violet_rect,card4)
        surface.blit(card3_violet_rect,card)
        surface.blit(text,lev)
        surface.blit(text1,b)
        surface.blit(go,b)
        surface.blit(r,rb)
        surface.blit(Note,imagerect)
        pygame.display.update()

dc1()