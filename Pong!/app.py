import pygame
from random import randint

pygame.init()

width = 900
height = 800

pygame.display.set_caption('Pong!')
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

scl = 20

sclWidth = width / scl
sclHeight = height / scl

black =  (0,0,0)
white = (255,255,255)

puck = {
    'x' : sclWidth / 2,
    'y' : sclHeight / 2,

    'x speed' : randint(-2,2) / 4.0,
    'y speed' : randint(-2,2) / 4.0,

    'size' : scl
 }

player = {
    'x' : sclWidth - 2,
    'y' : sclHeight / 2,

    'height' : 5 * scl,
    'width' : 1 * scl
 }

AI = {
    'x' : 2,
    'y' : sclHeight / 2,

    'height' : 5 * scl,
    'width' : 1 * scl
 }



while puck['x speed'] == 0:
    puck['x speed'] = randint(-2,2) / 4.0

while puck['y speed'] == 0:
    puck['y speed'] = randint(-2,2) / 4.0

def reset():
    player['x'] = sclWidth - 2
    player['y'] = sclHeight / 2

    AI['x'] = 2
    AI['y'] = sclHeight / 2

    puck['x'] = sclWidth / 2
    puck['y'] = sclHeight / 2

    puck['x speed'] = randint(-2,2) / 4.0
    puck['y speed'] = randint(-2,2) / 4.0

    while puck['x speed'] == 0:
        puck['x speed'] = randint(-2,2) / 4.0

    while puck['y speed'] == 0:
        puck['y speed'] = randint(-2,2) / 4.0
     

def update():
    if(player['x'] - 1 == puck['x']):
        
        if(player['y'] >= puck['y'] - (player['height'] / scl) and puck['y'] >= player['y']):
            puck['x speed'] *= -1

    if(AI['x'] + 1 == puck['x']):
        
        if(AI['y'] >= puck['y'] - (AI['height'] / scl) and puck['y'] >= AI['y']):
            puck['x speed'] *= -1
    
    player['y'] = pygame.mouse.get_pos()[1] / scl - ((player['height'] / 2)) / scl
    
    if puck['y'] >= sclHeight - 1 or puck['y'] <= 0:
        puck['y speed'] *= -1
    
    if puck['x'] >= sclWidth - 1 or puck['x'] <= 0:
        reset()
    
    puck['x'] += puck['x speed']
    puck['y'] += puck['y speed']

    AI['y'] += puck['y speed']

def draw():
    screen.fill(black)
    
    pygame.draw.rect(screen,white,(puck['x'] * scl,puck['y'] * scl,puck['size'],puck['size']))
    pygame.draw.rect(screen,white,(AI['x'] * scl,AI['y'] * scl,AI['width'],AI['height']))
    pygame.draw.rect(screen,white,(player['x'] * scl,player['y'] * scl,player['width'],player['height']))
    
    pygame.display.update()

gameExit = False

while not gameExit:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            gameExit = True

        

    update()
    draw()

    clock.tick(35)

pygame.quit()
