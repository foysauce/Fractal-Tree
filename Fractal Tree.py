import pygame
import sys
import math

pygame.init()

width = 1000
height = 800
white = (255,255,255)
red = (255,0,0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0,0,0)

screen = pygame.display.set_mode((width, height))
screen.fill(black)

#iterations
itr = 5

#length of tree truck
length = height/3

#division of length.
div = 1.5

# Angle in degrees
DA = 60

#thickness of tree
thick = 2

#This should always be 90
angle = 90

p1 = [width/2,height]

plist = [[angle, p1]]

level = 1
count = 1

for x in range(itr+1):
    if x == 0:
        pass
    else:
        for p in plist:
            p2 = [p[1][0]-length*math.cos(math.radians(p[0])), p[1][1]-length*math.sin(math.radians(p[0]))]
            pygame.draw.line(screen, green, p[1], p2, thick)
            angle1 = p[0] - DA
            angle2 = p[0] + DA
            plist.append([angle1,p2])
            plist.append([angle2,p2])
            print(p)
            print(count)
            print(length)
            count += 1
            if count == 2**level:
                length = length/div
                level += 1
                print("level phase")

            if count >= 2**itr:
                break
            
            if length <= 2:
                break

while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()
    pygame.display.update()