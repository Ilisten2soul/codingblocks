import pygame
import random
import os
pygame.mixer.init()

pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
#creating window
screen_width=900
screen_height=500
gameWindow=pygame.display.set_mode((screen_width,screen_height))#(width,height)
#background image
bgimg=pygame.image.load('D:\py\snake.jpg')
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha() #convert_alpha() doesn`t let the game slown down everytime image is rendered on the screen as image rendering is the slow process
#game title
pygame.display.set_caption('GameWithShivam')
pygame.display.update()
clock=pygame.time.Clock()
font = pygame.font.SysFont(None,55)#create a font object from system fonts
 #creating screen
    #creating screen
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])#snake_x and snake_y are coordinates of position
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(white)
        text_screen('welcome to snakes',black,250,300)
        text_screen('press space to play',black,250,380)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('D:\py\on_and_on.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)
#craete a game loop
#game loop
def gameloop():
    #Game specific variables
       #game specific variables
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    snake_size=30
    fps=60
    velocity_x=0
    velocity_y=0
    snk_list=[]
    snk_length=1
    food_x=random.randint(20,screen_width/2)#(initial point,final point)
    food_y=random.randint(20,screen_height/2)
    score= 0
    init_velocity=5
    if(not os.path.exists('high_score.txt')):
                with open('high_score.txt','w') as f:
                    f.write('0')
    with open('D:\py\high_score.txt','r')as f:
        high_score=f.read()
    while not exit_game:
        if game_over:
            with open('high_score.txt','w') as f: #note 'high_score.txt' implies D:\py\high_score.txt'
                f.write(str(high_score))
            gameWindow.fill(white)
            text_screen('Game Over!Press Enter to continue',red,100,300)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                
                    if event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                
                    if event.key == pygame.K_UP:
                        velocity_y=-init_velocity #pygame uses odd coordinate system
                        velocity_x=0

                    if event.key == pygame.K_DOWN:
                        velocity_y=+init_velocity
                        velocity_x=0
                    
                    if event.key ==pygame.K_q:
                        score+=10


            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score += 10
                food_x=random.randint(20,screen_width/2)#(initial point,final point)
                food_y=random.randint(20,screen_height/2)
                snk_length+=5
                if score>int(high_score):
                    high_score=score
            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))

            text_screen('Score:'+str(score)+'Highscore:'+str(high_score),red,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
            pygame.mixer.music.load('D:\py\on_and_on.mp3')
            pygame.mixer.music.play()
            if snake_x<0 or snake_x>screen_width or snake_y>screen_height or snake_y<0:
                game_over=True
            pygame.mixer.music.load('D:\py\on_and_on.mp3')
            pygame.mixer.music.play()
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)#it means every second this much frames will be passed
    
    pygame.quit()
    quit()
welcome()