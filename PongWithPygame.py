import pygame, random


WHITE = (255, 255, 255)
RED = (255, 0, 0)
RandomList = [-1, 1]

pygame.init()
LeftScore = 0
RightScore = 0
master = pygame.display.set_mode((1250, 750))
NumberFont = pygame.font.SysFont("Comic Sans", 50)
pygame.display.set_caption("Pong!")

winner = " "
x1 = 1150
x2 = 100
y1 = 275
y2 = 275
x3 = 600
y3 = 375
width = 10
height = 100
vel = 12
vel2 = 4
vel3 = 4

def Delay():
    pygame.time.delay(1000)
def RandomDirection(direction):
    global x3, y3, vel2, vel3, x1, x2
    RandomY = random.choice(RandomList)
    x3 = 600
    y3 = 370
    if direction == 'right':
        x3 = x1
        vel3 = abs(vel3) * -1
    else:
        x3 = x2 + width
        vel3 = abs(vel3)
    vel2 = abs(vel2) + 0.05
    vel2 *= RandomY

Running = True
while Running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y1 > vel:
        y1 -= vel

    if keys[pygame.K_DOWN] and y1 < 650:
        y1 += vel

    if keys[pygame.K_w] and y2 > vel:
        y2 -= vel

    if keys[pygame.K_s] and y2 < 650:
        y2 += vel

    if y3 > vel and y3 < 735:
        y3 += vel2
    else:
        vel2 *= -1
        y3 += vel2

    if x3 > x1 and x3 < (x1+width) and y3 > y1 and y3 < (y1+height):
        vel3 *= -1
        x3 += vel3
    else:
        x3 += vel3

    if x3 > x2 and x3 < (x2+width) and y3 > y2 and y3 < (y2+height):
        vel3 *= -1
        x3 += vel3
    else:
        x3 += vel3

    if x3 < 0:
        RightScore += 1
        RandomDirection('right')
    if x3 > 1250:
        LeftScore += 1
        RandomDirection('left')
    if RightScore >= 21:
        winner = "Right Wins!"
        Running = False
    if LeftScore >= 21:
        winner = "Left Wins!"
        Running = False

    master.fill((0, 0, 0))
    pygame.draw.rect(master, WHITE, (x1, y1, width, height))
    pygame.draw.rect(master, WHITE, (x2, y2, width, height))
    pygame.draw.rect(master, WHITE, (x3, y3, 10, 10))
    LeftText = NumberFont.render(str(LeftScore), True, WHITE)
    RightText = NumberFont.render(str(RightScore), True, WHITE)
    WinningText = NumberFont.render(str(winner), True, WHITE)
    master.blit(LeftText, (10, 10))
    master.blit(RightText, (1220, 10))
    master.blit(WinningText, (750, 10))
    pygame.display.update()

Delay()

pygame.quit()