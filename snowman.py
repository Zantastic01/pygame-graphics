# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Winter Cabin"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (122, 53, 25)
YELLOW = (243, 247, 160)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])
    

''' Make stars '''
stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)

# Game loop
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Drawing code
    ''' clouds '''
    screen.fill(BLACK)
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)

    '''ground'''
    pygame.draw.rect(screen, WHITE, [0, 450, 800, 600])

    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)
    
    ''' fence '''
    y = 410 
    for x in range(5, 1100, 30):
        pygame.draw.polygon(screen, WHITE, [[x+10, y], [x+20, y+20],
                                            [x+20, y+50], [x, y+50],
                                            [x, y+20]])
    pygame.draw.line(screen, WHITE, [0, 430], [800, 430], 5)
    pygame.draw.line(screen, WHITE, [0, 450], [800, 450], 5)

    '''house'''
    for s in stars:
        pygame.draw.rect(screen, BROWN, [300, 250, 300, 200])
        pygame.draw.rect(screen, BLACK, [300, 250, 300, 200], 3)
        pygame.draw.ellipse(screen, WHITE, s)
        pygame.draw.polygon(screen, BLACK, [[250, 250], [450, 150], [650, 250]], 5)
        pygame.draw.polygon(screen, BROWN, [[250, 250], [450, 150], [650, 250]])
        pygame.draw.rect(screen, BLACK, [400, 300, 100, 150], 5)
        pygame.draw.rect(screen, BROWN, [400, 300, 100, 150])
        pygame.draw.ellipse(screen, BLACK, [415, 360, 15, 15])
    '''sun'''
    pygame.draw.ellipse(screen, YELLOW, [50, 200, 100, 100])

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
