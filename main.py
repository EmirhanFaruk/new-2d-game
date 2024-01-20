
# Modification date: Mon Jul  4 20:01:40 2022

# Production date: Sun Sep  3 15:43:48 2023

import pygame
import math

wScreen = 1200
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))

class Ball(object):
    def __init__(self, x, y, radius, colour):
        self.llx = x
        self.lly = y
        self.lx = x
        self.ly = y
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

    def draw(self, win):
        if self.y< hScreen - self.radius:
            pygame.draw.line(win, (125, 125, 125), (self.llx, self.lly), (self.lx, self.ly))
            pygame.draw.circle(win, (150, 150, 150), (self.lx, self.ly), self.radius)
        pygame.draw.circle(win, (100, 100, 100), (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius - 1)
        

    @staticmethod
    def ballPath(startx, starty, power, angle, time):
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time)**2) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)

        return (newx, newy)

def findAngle(pos):
    sX = da_ball.x
    sY = da_ball.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle
    return angle

def redrawWindow():
    win.fill((0, 0, 0))
    da_ball.draw(win)
    pygame.draw.line(win, (255, 255, 255), line[0], line[1])
    pygame.display.update()


da_ball = Ball(600, hScreen - 6, 5, (200, 200, 200))

x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    if shoot:
        if da_ball.y < hScreen - da_ball.radius:
            time += 0.3
            po = Ball.ballPath(x, y, power, angle, time)
            da_ball.llx = da_ball.lx
            da_ball.lly = da_ball.ly
            da_ball.lx = da_ball.x
            da_ball.ly = da_ball.y
            da_ball.x = po[0]
            da_ball.y = po[1]
        else:
            shoot = False
            da_ball.y = hScreen - 6
    
        
    mouse_pos = pygame.mouse.get_pos()
    line = [(da_ball.x, da_ball.y), mouse_pos]
    redrawWindow()
    """
    if not(shoot) and da_ball.y >= hScreen - da_ball.radius - 1:
        shoot = True
        x = da_ball.x
        y = da_ball.y
        time = 0
        power = math.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2)/8
        angle = findAngle(mouse_pos)
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not shoot:
                shoot = True
                x = da_ball.x
                y = da_ball.y
                time = 0
                power = math.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2)#/8
                angle = findAngle(mouse_pos)

pygame.quit()
