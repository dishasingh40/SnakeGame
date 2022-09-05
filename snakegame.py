# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:08:27 2022

@author: DISHA SINGH
"""



import pygame
import time
import random
import mysql.connector

mydb = mysql.connector.connect(host='localhost',database='snakegame',user='root',password='double_mask')
mycursor = mydb.cursor()


def snakess():    
    snake_speed = 15
     
    window_x = 720
    window_y = 480
    
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
     
    pygame.init()
     
    pygame.display.set_caption('Snake Game')
    
    game_window = pygame.display.set_mode((window_x, window_y))
     
    fps = pygame.time.Clock()
     
    snake_position = [100, 50]
     
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]
    
    fruit_position = [random.randrange(1, (window_x//10)) * 10,
                      random.randrange(1, (window_y//10)) * 10]
     
    fruit_spawn = True
     

    direction = 'RIGHT'
    change_to = direction
     
    score = 0
     

    def show_score(choice, color, font, size):
       
        score_font = pygame.font.SysFont(font, size)
        
        score_surface = score_font.render('Score : ' + str(score), True, color)
         
        score_rect = score_surface.get_rect()
         
        game_window.blit(score_surface, score_rect)
     
    def game_over():
       
        my_font = pygame.font.SysFont('times new roman', 50)
        val= score , name
        mycursor.execute("update user1 set score = %s where user_name = %s",val)
        mydb.commit()
        
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)
         

        game_over_rect = game_over_surface.get_rect()
         
        game_over_rect.midtop = (window_x/2, window_y/4)
         
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
         
        time.sleep(2)
    
        pygame.quit()
         
        quit()
     
    done = True
    while done:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
    
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
     
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10
    
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()
             
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                              random.randrange(1, (window_y//10)) * 10]
             
        fruit_spawn = True
        game_window.fill(black)
         
        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))
     
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()
     
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
     
        show_score(1, white, 'times new roman', 20)
     
        pygame.display.update()
     
        fps.tick(snake_speed)
        
        
print("******************** SNAKE GAME ********************")  
      
print("1. New User")
print("2. Exixting User")
ch = int(input("Enter your choice 1 or 2 :"))

if ch == 1:
    name = input("Enter user name for new account :")
    pas = input("Enter the password :")
    sc = 0
    val = name,pas,sc
    
    mycursor.execute("INSERT INTO USER1 VALUES(%s,%s,%s)",val)
    mydb.commit()
    snakess()
elif ch == 2:
    name = input("Enter your user name:")
    pas = input("Enter your password :")
    mycursor.execute("select user_name from user1")
    data = mycursor
    data = mycursor.fetchall()
        
    coun=len(data)
    for i in range(0,coun):
        if name not in data[i]:
            print("wrong username")
        else:
            mycursor.execute("select password from user1")
            data = mycursor
            data = mycursor.fetchall()
            for j in range(0, coun):
                if pas not in data[j]:
                    print("Wrong password")
                else:
                    print("What do you want: 1.Check Last Score Or 2.Play Game.")
                    dis=int(input("Enter Option :"))
                    if dis == 1:
                        val = name , pas
                        mycursor.execute("select score from user1 where user_name = %s and password = %s",val)
                        data = mycursor
                        data = mycursor.fetchall()
                        
                        print("Your Total score is ",data)
                    elif dis == 2:    
                        snakess()
                    else:
                        print("Invalid ")
        
        
        mydb.commit()