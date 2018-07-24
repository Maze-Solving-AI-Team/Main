# Import modules
import sys, pygame, time, math
from time import sleep
from pygame.locals import *
from PIL import Image
# Initialize
img = Image.open('maze.png')
change = 5
width = img.width * change
height = img.height * change
background = [img]
screen = pygame.display.set_mode((width,height))
background = pygame.image.load('maze.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0, 0))
pygame.display.update()
color = (0,128,0)

# Recognizing black/white
print(width, height)
size = [img.size]
print(size[0])
colors = img.getcolors()
print(colors)
pix = img.load()
list = []

# Locate the starting coordinate
for x in range(0,180):
    if pix[x,179] == (255, 255, 255, 255):
        list.append(x)

xvalueOfStart = list[0] * change
print(xvalueOfStart)

blockSize = len(list) * change

list = []

# Locate the ending coordinate
for x in range(0,180):
    if pix[x,0] == (255, 255, 255, 255):
        list.append(x)

xvalueOfEnd = list[0] * change
print(xvalueOfEnd)

# Make maze appear on screen for set amount of seconds
for x in range(0,100):
    screen.blit(newscreen, (0, 0))
    pygame.draw.rect(newscreen, color, pygame.Rect(xvalueOfStart, height - blockSize, 5 * change, 5 * change))
    pygame.display.update()
    time.sleep(0.1)