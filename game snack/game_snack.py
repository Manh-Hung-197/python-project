import pygame
import random , time, sys

from pygame.key import name

pygame.init()

m = 20
red = (255, 0, 0)
blue = (65, 105, 255)
black  = (0, 0, 0) 
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 128, 0)

Imgbody = pygame.transform.scale(pygame.image.load('mui_ten.png'), (m, m))
Imghead = pygame.transform.scale(pygame.image.load('nhat.png'), (m, m))
Imgfood = pygame.transform.scale(pygame.image.load('tim.jpg'), (m, m))


win = pygame.display.set_mode((735,475))
pygame.display.set_caption('SNAKE')

#khoi tao ran, thuc an
snake = [100, 60]
snake_body = [[100, 60],[80, 60], [60,60]]
foodx = random.randrange(1, 71)
foody = random.randrange(1, 45)
if foodx % 2 != 0:
    foodx += 1
if foody % 2 != 0:
    foody += 1
foodpos = [foodx * 10, foody * 10]
foodflat = True
direction = 'RIGHT'
changeto = direction
score = 0

#game over
def game_over():
    gfont = pygame.font.SysFont('consolas', 40)
    gsurf = gfont.render('game over!', True, red)
    grect = gsurf.get_rect()
    grect.midtop = (360, 150)
    show_score(0) #(xu li sau)
    win.blit(gsurf, grect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

#xu li ham show_score
def show_score(choice = 1):
    sfont = pygame.font.SysFont('consolas', 20)
    ssurf = sfont.render('SCORE: {0}'.format(score), True, black)
    srect = ssurf.get_rect()
    if  choice == 1:
        srect.midtop = (70, 20)
    else:
        srect.midtop = (360, 230)
    win.blit(ssurf, srect)

while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # dieu khien
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:#right
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT:#left
                changeto = 'LEFT'
            if event.key == pygame.K_UP:#up
                changeto = 'UP'
            if event.key == pygame.K_DOWN:#down
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:#esc
                pygame.event.post(pygame.event.Event(pygame.QUIT))


    # huong di
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'


    #update vi tri
    if direction == 'RIGHT':
        snake[0] += m
    if direction == 'LEFT':
        snake[0] -= m
    if direction == 'UP':
        snake[1] -= m
    if direction == 'DOWN':
        snake[1] += m

    #san moi
    snake_body.insert(0, list(snake))
    if snake[0] == foodpos[0] and snake[1] == foodpos[1]:
        score += 1
        foodflat = False
    else:
        snake_body.pop()

    #sinh san
    if foodflat == False:
        foodx = random.randrange(1, 71)
        foody = random.randrange(1, 45)
        if foodx % 2 != 0:
            foodx += 1
        if foody % 2 != 0:
            foody += 1
        foodpos = [foodx *10, foody * 10]
    foodflat = True


    # update ran, thuc an, body len man hinh
    win.fill(green)
    for pos in snake_body:
        win.blit(Imgbody, pygame.Rect(pos[0], pos[1], m, m))
    win.blit(Imghead, pygame.Rect(snake_body[0][0],snake_body[0][1],m, m))
    win.blit(Imgfood, pygame.Rect(foodpos[0], foodpos[1], m, m))

    # di chuyen cham canh or an chinh minh
    if snake[0] > 710 or snake[0] < 10:
        game_over()
    if snake[1] > 450 or snake[1] < 10:
        game_over()

    for b in snake_body[1:]:
        if snake[0] == b[0] and snake[1] == b[1]:
            game_over()
    
    #duong vien
    pygame.draw.rect(win, gray, (10, 10, 715, 455), 2)
    show_score()
    pygame.display.flip()