
import tkinter
from tkinter import *
from tkinter import messagebox
top=Tk()
top.withdraw()
from pygame.locals import *
def dc ():
    import pygame

    import sys
    c6=0
    c1=0
    c2=0
    c =0
    c5 =0
    c7 =0
    c3= 0
    pygame.init()
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.play()
    surface = pygame.display.set_mode((1366,768))
    black = (0,0,0)
    white = (255,255,255)
    background = pygame.image.load("Background.JPG")
    pygame.display.set_caption("SET-CARDS")
    gameIcon = pygame.image.load('icon.jpg')
    pygame.display.set_icon(gameIcon)
    imagerect = background.get_rect()
    pygame.display.toggle_fullscreen()
    size = ((140,70))
    brown = 193, 154, 107
    card1_pink_diamond = pygame.image.load("1 RED D DIA.PNG").convert()
    card1_pink_diamond = pygame.transform.scale(card1_pink_diamond, (80,100))
    card1_violet_diamond = pygame.image.load("1 BLUE D DIA.PNG").convert()
    card1_violet_diamond = pygame.transform.scale(card1_violet_diamond,(80,100))
    card1_green_diamond = pygame.image.load("2 BLUE D DIA.PNG").convert()
    card1_green_diamond = pygame.transform.scale(card1_green_diamond, (80,100))
    card1_pink_star = pygame.image.load("1 RED D SQUI.PNG").convert()
    card1_pink_star = pygame.transform.scale(card1_pink_star,(80,100))
    card2_violet_rect = pygame.image.load("2 BLUE D RECT.PNG").convert()
    card2_violet_rect = pygame.transform.scale(card2_violet_rect,(80,100))
    card1_violet_star = pygame.image.load("1 BLUE D SQUI.PNG").convert()
    card1_violet_star = pygame.transform.scale(card1_violet_star,(80,100))
    card1_pink_rect = pygame.image.load("1 RED D RECT.PNG").convert()
    card1_pink_rect = pygame.transform.scale(card1_pink_rect,(80,100))
    card2_green_rect = pygame.image.load("card 2 green rect.PNG").convert()
    card2_green_rect = pygame.transform.scale(card2_green_rect,(80,100))
    card1_violet_rect = pygame.image.load("1 BLUE D RECT.PNG").convert()
    card1_violet_rect = pygame.transform.scale(card1_violet_rect,(80,100))

    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render("Level 3", True, (250, 80, 37))
    surface.blit(background,(0,0))
    font = pygame.font.SysFont("comicsansms", 25)
    text1 = font.render("  ", True, (255, 255,255))
    font = pygame.font.SysFont("comicsansms", 34)
    gameover = font.render(" ((GOOD)) ",True,(255,255,255))
    Wrong = font.render("((Try Again))",True,(255,255,255))
    Note = font.render(" Find a 2 Set Cards ",True,(255,255,255))
    re = font.render("       ** ",True,(255,255,255))
    reset = font.render(" RESET COMPLETED ",True,(255,255,255))

    top = (180,240)
    left = (123,30)
    width = 80
    height = 100
    width1 = 200
    height1 = 100
    width2 = 0
    height2 = 0

    card1  = pygame.draw.rect(surface,black,(457,193,width,height))
    card3 = pygame.draw.rect(surface,black,(200,321,width,height))
    card5 = pygame.draw.rect(surface,black,(700,325,width,height))
    card2 = pygame.draw.rect(surface,black,(700,195,width,height))
    card4 = pygame.draw.rect(surface,black,(457,319,width,height))
    card = pygame.draw.rect(surface,black,(200,185,width,height))
    card6 = pygame.draw.rect(surface,black,(200,447,width,height))
    card7 = pygame.draw.rect(surface,black,(457,450,width,height))
    card8 = pygame.draw.rect(surface,black,(700,455,width,height))
    gameover1 = pygame.draw.rect(surface,black,(1120,68,width1,height1))
    gameover2 = pygame.draw.rect(surface,black,(1120,70,width1,height1))
    lev = pygame.draw.rect(surface,black,(8,52,width2,height2))
    go = pygame.image.load("Continue.png")
    go = pygame.transform.scale(go, (100,100))
    b = pygame.draw.rect(surface,brown,(1120,555,102,100))
    r = pygame.image.load("Replay.png")
    r = pygame.transform.scale(r, (100,100))


    rb = pygame.draw.rect(surface,brown,(1120,400,102,100))

#rect = rect.move(40,80)
#def game_loop():

    while True:
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pressed1 and rb.collidepoint(pos):
                c1 =0
                c6 =0
                c2 =0
                c5 =0
                c7=0
                c =0
                surface.blit(reset,gameover1)
            if pressed1 and b.collidepoint(pos):
                if (c1 == 1 and c6 ==1 and c2 == 1):
                    print("one set correct")
                    if (c == 1 and c5 == 1 and c7 == 1):
                        print("Second Set Correct")
                if (c1 ==1 and c2==1 and c5 ==1)and(c==1 and c5 ==1 and c7==1):
                    import FOURTHL
                    surface.blit(gameover,gameover1)
                else:
                    surface.blit(Wrong,gameover1)

            if card1.collidepoint(pos) and pressed1:
                c1 += 1
                print("Correct")
            if card.collidepoint(pos) and pressed1:
                c +=1
                print("Correct")
            if card2.collidepoint(pos) and pressed1:
                c2 += 1
                print("CORRECT")
            if card6.collidepoint(pos)and pressed1:
                c6 += 1
                print("Correct")
            if card3.collidepoint(pos)and pressed1:
                print("Wrong")
            if card4.collidepoint(pos)and pressed1:

                print("Wrong")
            if card5.collidepoint(pos)and pressed1:
                c5 +=1
                print("Correct")
            if card7.collidepoint(pos)and pressed1:
                print("Correct")
                c7 +=1
            if card8.collidepoint(pos)and pressed1:
                print("Wrong")

        surface.blit(card1_pink_diamond,card1)
        surface.blit(card1_green_diamond,card3)
        surface.blit(card1_violet_diamond,card5)
        surface.blit(card1_pink_star,card2)
        surface.blit(card2_violet_rect,card4)
        surface.blit(card1_violet_star,card)
        surface.blit(card1_pink_rect,card6)
        surface.blit(card1_violet_rect,card7)
        surface.blit(card2_green_rect,card8)
        surface.blit(text,lev)
        surface.blit(text1,b)
        surface.blit(go,b)
        surface.blit(Note,imagerect)
        surface.blit(r,rb)
        pygame.display.update()

dc()