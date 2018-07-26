# Import modules
import sys, pygame, time, math, MSADir
from time import sleep
from pygame.locals import *
from PIL import Image
from MSADir import *

# Initialize
img = Image.open('maze.png')
change = 2
width = img.width * change
height = img.height * change
screen = pygame.display.set_mode((width,height))
background = pygame.image.load('maze.png').convert()
newscreen = pygame.transform.scale(background, (width, height))


#Colors
color = (0, 188, 0)
white = (255, 255, 255)
black = (255, 255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 188, 0)

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

yvalueOfStart = height - blockSize

list = []

# Locate the ending coordinate
for x in range(0,180):
    if pix[x,0] == (255, 255, 255, 255):
        list.append(x)

xvalueOfEnd = list[0] * change
print(xvalueOfEnd)

pygame.draw.rect(newscreen, color, pygame.Rect(xvalueOfStart, yvalueOfStart, blockSize, blockSize))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(0.1)

# Function to move forward
def moveUp(x, y, blocksize, newcolor):
    global direction
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y - blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x
    direction = 1

# Function to move left
def moveDown(x, y, blocksize, newcolor):
    global direction
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y + blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x
    direction = 4
    
# Function to move left  
def moveLeft(x, y, blocksize, newcolor):
    global direction
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y
    direction = 3

# Function to move right
def moveRight(x, y, blocksize, newcolor):
    global direction
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y
    direction = 2

#Initialization of currentX and currentY
def varsInit(x, y):
    global currentX
    global currentY
    global direction
    currentX = x
    currentY = y
    direction = 1

#Algorithm to determine direction to move if facing up
def up(replace):
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        print("up-Move right called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        print("up-Move up called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        print("up-Move left called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        print("up-Move down called")
        time.sleep(0.01)
    
#Algorithm to determine direction to move if facing right
def right(replace):
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        print("right-Move down called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        print("right-Move right called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        print("right-Move up called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        print("right-Move left called")
        time.sleep(0.01)
    
#Algorithm to determine direction to move if facing left
def left(replace):
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        print("left-Move up called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        print("left-Move left called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        print("left-Move down called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        print("left-Move right called")
        time.sleep(0.01)

#Algorithm to determine direction to move if facing down
def down(replace):
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        print("down-Move left called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        print("down-Move down called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        print("down-Move right called")
        time.sleep(0.01)
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        print("down-Move up called")
        time.sleep(0.01)

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, white)

#time.sleep(0.1)

#moveLeft(currentX, currentY, blockSize)
#time.sleep(1)

#moveDown(currentX, currentY, blockSize)
#time.sleep(1)

#moveRight(currentX, currentY, blockSize)
#time.sleep(1)

'''
1 is up
2 is right
3 is left
4 is down
'''

direction = 1

#original
while 0 != currentY:
    if direction == 1:#up
        up(white)
    elif direction == 2:
        right(white)
    elif direction == 3:
        left(white)
    elif direction == 4:
        down(white)

time.sleep(5)
