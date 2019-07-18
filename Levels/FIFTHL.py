import tkinter 
from tkinter import *
from tkinter import messagebox
top= Tk()
top.withdraw()
from pygame.locals import *
def dc1 ():
    import pygame
    import sys
    c=0
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    c7=0
    c8=0
    c9=0
    c10=0
    c11=0
    pygame.init()
    surface = pygame.display.set_mode((1366,756))
    black = (0,0,0)
    white = (255,255,255)
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.play()
    background = pygame.image.load("Background.JPG")  
    pygame.display.set_caption("SET-CARDS")
    gameIcon = pygame.image.load('ico.jpg')
    pygame.display.set_icon(gameIcon)
    imagerect = background.get_rect() 
    size = ((140,70))
    GREEN2_D_SQUI = pygame.image.load("2 BLUE P RECT.png").convert()   #(image-2)
    GREEN2_D_SQUI = pygame.transform.scale(GREEN2_D_SQUI,(175,125))
    BLUE2_D_DIAMOND = pygame.image.load("3 GREEN S SQUI.png").convert()   #(image-6)
    BLUE2_D_DIAMOND = pygame.transform.scale(BLUE2_D_DIAMOND,(175,125))
    card1_red_diamond = pygame.image.load("1 RED D DIA.png").convert() #(image-4)
    card1_red_diamond = pygame.transform.scale(card1_red_diamond, (175,125))
    card3_green_squigi = pygame.image.load("3 GREEN S RECT.png").convert()#(image-3)
    card3_green_squigi = pygame.transform.scale(card3_green_squigi,(175,125))
    card4_blue_rect  =pygame.image.load("3 BLUE P SQUI.png").convert()
    card4_blue_rect =pygame.transform.scale(card4_blue_rect,(175,125))
    card4_green_diamond =pygame.image.load("1 GREEN D RECT.png").convert()
    card4_green_diamond =pygame.transform.scale(card4_green_diamond,(175,125))
    card1_green_diamond=pygame.image.load("3 RED D DIA.png").convert()
    card1_green_diamond=pygame.transform.scale(card1_green_diamond,(175,125))
    card2_red_squigi=pygame.image.load("1 GREEN D DIA.png").convert()
    card2_red_squigi=pygame.transform.scale(card2_red_squigi,(175,125))
    card3_red_rect=pygame.image.load("2 RED S RECT.png").convert()
    card3_red_rect=pygame.transform.scale(card3_red_rect,(175,125))
    card4_blue_diamond=pygame.image.load("2 RED S SQUI.png").convert()
    card4_blue_diamond=pygame.transform.scale(card4_blue_diamond,(175,125))
    card2_blue_squigi = pygame.image.load("2 RED S DIA.png").convert() #(image-5)
    card2_blue_squigi = pygame.transform.scale(card2_blue_squigi,(175,125))
    card1_blue_squigie = pygame.image.load("3 RED P RECT.png").convert() #(image-1)
    card1_blue_squigie= pygame.transform.scale(card1_blue_squigie,(175,125))
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render("Level 5", True, (250, 80, 37))
    surface.blit(background,(0,0))
    font = pygame.font.SysFont("comicsansms", 25)
    text1 = font.render(" ", True, (255, 255,255))
    font = pygame.font.SysFont("comicsansms", 34)
    gameover = font.render(" ((GOOD)) ",True,(255,255,255))
    Wrong = font.render("((Try Again))",True,(255,255,255))
    Note = font.render("Find Set",True,(255,255,255))
    top = (180,240)
    left = (123,30)
    width = 175
    height = 125
    width1 =200
    height1 =100
    width2=0
    height2=0
    red = 255,255,255
    brown = 193, 154, 107
    card1  = pygame.draw.rect(surface,black,(330,150,width,height))
    card4 = pygame.draw.rect(surface,black,(100,350,width,height))
    card6 = pygame.draw.rect(surface,black,(550,350,width,height))
    card2 = pygame.draw.rect(surface,black,(550,150,width,height))
    card5 = pygame.draw.rect(surface,black,(330,350,width,height))
    card = pygame.draw.rect(surface,black,(100,150,width,height))
    card3=pygame.draw.rect(surface,black,(770,150,width,height))
    card7=pygame.draw.rect(surface,black,(770,350,width,height))
    card8=pygame.draw.rect(surface,black,(100,550,width,height))
    card9=pygame.draw.rect(surface,black,(330,550,width,height))
    card10=pygame.draw.rect(surface,black,(550,550,width,height))
    card11=pygame.draw.rect(surface,black,(770,550,width,height))
    gameover1=pygame.draw.rect(surface,black,(1120,68,width1,height1))
    lev = pygame.draw.rect(surface,black,(8,52,width2,height2))
    go = pygame.image.load("Continue.png")
    go = pygame.transform.scale(go, (100,100))
    b = pygame.draw.rect(surface,brown,(1120,555,102,100))
    r = pygame.image.load("Replay.png")
    r = pygame.transform.scale(r, (100,100))   
    rb = pygame.draw.rect(surface,brown,(1120,400,102,100))
    #messagebox.showwarning("SET-CARDS","Note: In this Level Click all the Sets and Finally Click Submit Button")
    while True:
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if b.collidepoint(pos) and pressed1:
                if (c== 1 and c1 ==1 and c2 == 1 and c3 == 2 and c4 == 3 and c5 ==1 and c6 ==2 and c7 ==1 and c8==1 and c9 ==1 and c10 ==2 and c11 == 2):
                    messagebox.showinfo("SET-CARDS","SET IS DONE")
                    surface.blit(gameover,gameover1)
                else:
                    response = messagebox.askquestion("SET - CARDS", "NOT FOUND PROPERLY TRY AGAIN")
                    if (response=='yes'):
                        c = 0
                        c1 = 0
                        c2 = 0
                        c3=0
                        c4=0
                        c5=0
                        c6=0
                        c7=0
                        c8=0
                        c9=0
                        c10=0
                        c11=0
                        messagebox.showinfo("SET-CARDS","Reset is Done")
                    else:
                        pygame.display.quit()
            if card.collidepoint(pos)and pressed1:
                c += 1
                print("card  pressed")
            if card1.collidepoint(pos) and pressed1:
                c1 += 1
                print("card 1 pressed")
            if card2.collidepoint(pos) and pressed1:
                c2 += 1
                print("card 2 pressed")
            if card3.collidepoint(pos)and pressed1:
                c3 += 1
                print("card 3 pressed")
            if card4.collidepoint(pos)and pressed1:
                c4 += 1
                print("card 4 pressed")
            if card5.collidepoint(pos) and pressed1:
                c5 += 1
                print("card 5 pressed")
            if card6.collidepoint(pos) and pressed1:
                c6 += 1
                print("card 6 pressed")
            if card7.collidepoint(pos) and pressed1:
                c7 += 1
                print("card 7 pressed")
            if card8.collidepoint(pos) and pressed1:
                c8+= 1
                print("card 8 pressed")
            if card9.collidepoint(pos) and pressed1:
                c9 += 1
                print("card 9 pressed")
            if card10.collidepoint(pos) and pressed1:
                c10 += 1
                print("card 10 pressed")
            if card11.collidepoint(pos) and pressed1:
                c11 += 1
                print("card 11 pressed")
        surface.blit(GREEN2_D_SQUI,card1)
        surface.blit(card1_red_diamond,card3)
        surface.blit(BLUE2_D_DIAMOND,card5)
        surface.blit(card3_green_squigi,card2)
        surface.blit(card2_blue_squigi,card6)
        surface.blit(card1_blue_squigie,card)
        surface.blit(card4_blue_rect,card4)
        surface.blit(card4_green_diamond,card7)
        surface.blit(card1_green_diamond,card8)
        surface.blit(card2_red_squigi,card9)
        surface.blit(card3_red_rect,card10)
        surface.blit(card4_blue_diamond,card11)
        surface.blit(text,lev)
        surface.blit(text1,b)
        surface.blit(go,b)
        surface.blit(r,rb)
        surface.blit(Note,imagerect)
        pygame.display.update()

dc1()