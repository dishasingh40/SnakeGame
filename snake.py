import pygame
import random
from pygame import font



pygame.init()

width = 800
height = 800
screen = pygame.display.set_mode((width,height))
 
pygame.display.set_caption("Snake Game")

icon = pygame.image.load(r"C:\Users\JALAJ SINGH\Downloads\iconsnake-removebg.png")
pygame.display.set_icon(icon)

score = 0
#position of snake on xaxis and yaxis
Xaxis = 400
Yaxis = 700
Xaxis_change = 0
Yaxis_change = 0
#Xapple = random.randint(1,780)
#Yapple = random.randint(1,780)
Xapple,Yapple = random.randrange(0,720)//10*10,random.randrange(0,720)//10*10
 
body_list = [(Xaxis,Yaxis)]
    
def playing():
    global Xapple,Yapple,Xaxis,Yaxis
    
    Xaxis += Xaxis_change
    Yaxis += Yaxis_change
    
    #scrore = font.render("Score : " +str(len(body_list)),True,(33,44,55))
    #screen.blit(scrore [0,0])
    
    body_list.append((Xaxis,Yaxis))
    if (Xapple == Xaxis and Yapple == Yaxis):
      while((Xapple,Yapple) in body_list):
          Xapple,Yapple = random.randrange(0,width)//10*10,random.randrange(0,height)//10*10
    else:
        del body_list[0]
    
    screen.fill((49,74,16))
    dim_rect = [Xapple,Yapple,20,20]
    sn_rect = pygame.draw.rect(screen,(233,44,44),dim_rect)

    for (i,j) in body_list :
        dim_food = [i,j,20,20]
        sn_food = pygame.draw.rect(screen,(2,10,190),dim_food)
    pygame.display.update()
                                 
        

     #back = pygame.image.load(r'C:\Users\JALAJ SINGH\Desktop\New folder\background1.png')    
     #screen.blit(back,(0,0))     

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50) 

      
done = True 
while done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            exit()
            
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                if Xaxis_change != -10:
                      Xaxis_change += 10
                Yaxis_change = 0
            elif event.key == pygame.K_LEFT :
                if Xaxis_change != 10:
                    Xaxis_change += -10
                Yaxis_change = 0
            elif event.key == pygame.K_UP :
                if Yaxis_change != 10:
                    Yaxis_change += -10
                Xaxis_change = 0
            elif event.key == pygame.K_DOWN :
                if Yaxis_change != -10:
                    Yaxis_change += 10
                Xaxis_change = 0
            
            
        
    if Xaxis >= 780 or Xaxis < 20 or Yaxis >= 780 or Yaxis < 20 :
            done = False 
        
    #RGB       
    #screen.blit(back,(0,0))
    screen.fill((49,74,16))
    
    
    if Xaxis >= 760 :
        Xaxis = 760
    elif Xaxis <= 0:
        Xaxis = 0
        
    if Yaxis >= 760 :
        Yaxis = 760
    elif Yaxis <= 0:
        Yaxis = 0
    
    clock.tick(30)
    playing()
    
    pygame.display.update() 

