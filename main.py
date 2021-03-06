# Import modules
import sys, pygame, time, math
from time import sleep
from pygame.locals import *
from PIL import Image
# Initialize
img = Image.open('maze.png')
change = 3
width = img.width * change
height = img.height * change
background = [img]
screen = pygame.display.set_mode((width,height))
background = pygame.image.load('maze.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
color = (0,128,0)

# Recognizing black/white
#print(width, height)
#size = [img.size]
#print(size[0])
#colors = img.getcolors()
#print(colors)
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

white = (255, 255, 255)

pygame.draw.rect(newscreen, color, pygame.Rect(xvalueOfStart, yvalueOfStart, blockSize, blockSize))
screen.blit(newscreen, (0, 0))
pygame.display.update()
time.sleep(0.1)

# Function to move forward
def moveUp(x, y, blocksize):
    pygame.draw.rect(newscreen, (0,0,255), pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y - blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x

# Function to move left
def moveDown(x, y, blocksize):
    pygame.draw.rect(newscreen, (0,0,255), pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y + blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x   
    
# Function to move left  
def moveLeft(x, y, blocksize):
    pygame.draw.rect(newscreen, (0,0,255), pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y

# Function to move right
def moveRight(x, y, blocksize):
    pygame.draw.rect(newscreen, (0,0,255), pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y        

# Function to move forward
def moveUpG(x, y, blocksize):
    pygame.draw.rect(newscreen, (0,255,255), pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y - blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x

# Function to move left
def moveDownG(x, y, blocksize):
    pygame.draw.rect(newscreen, (0,255,255), pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y + blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x   
    
# Function to move left  
def moveLeftG(x, y, blocksize):
    pygame.draw.rect(newscreen, (0,255,255), pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y

# Function to move right
def moveRightG(x, y, blocksize):
    pygame.draw.rect(newscreen, (0,255,255), pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y        

moveUp(xvalueOfStart, yvalueOfStart, blockSize)
time.sleep(0.1)

#moveLeft(currentX, currentY, blockSize)
#time.sleep(1)

#moveDown(currentX, currentY, blockSize)
#time.sleep(1)

#moveRight(currentX, currentY, blockSize)
#time.sleep(1)

while 0 != currentY:
    if newscreen.get_at((currentX,currentY - blockSize)) == (255, 255, 255, 255):#up        
        moveUp(currentX, currentY, blockSize)
        print("Move up called")
        time.sleep(0.1)
    elif newscreen.get_at((currentX + blockSize,currentY)) == (255, 255, 255, 255):#right
        moveRight(currentX, currentY, blockSize)
        print("Move right called")
        time.sleep(0.1)
    elif newscreen.get_at((currentX - blockSize,currentY)) == (255, 255, 255, 255):#left
        moveLeft(currentX, currentY, blockSize)
        print("Move left called")
        time.sleep(0.1)
    elif newscreen.get_at((currentX,currentY + blockSize)) == (255, 255, 255, 255):#down
        moveDown(currentX, currentY, blockSize)
        print("Move down called")
        time.sleep(0.1)
    else:
        if newscreen.get_at((currentX,currentY + blockSize)) == (0, 0, 255, 255):#down
            moveDown(currentX, currentY, blockSize)
            print("Move down called")
            time.sleep(0.1)
        elif newscreen.get_at((currentX + blockSize,currentY)) == (0, 0, 255, 255):#right
            moveRight(currentX, currentY, blockSize)
            print("Move right called")
            time.sleep(0.1)
        else:
            if newscreen.get_at((currentX - blockSize,currentY)) == (0, 0, 255, 255):#left
                moveLeftG(currentX, currentY, blockSize)
                print("Move left called")
                time.sleep(0.1)
            elif newscreen.get_at((currentX,currentY - blockSize)) == (0, 0, 255, 255):#up        
                moveUpG(currentX, currentY, blockSize)
                print("Move up called")
                time.sleep(0.1)
time.sleep(5)