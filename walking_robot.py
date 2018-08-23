import pygame
pygame.init()

win = pygame.display.set_mode((200,200))

pygame.display.set_caption("Walking Robot")

walkRight = [pygame.image.load('right.png')]
walkLeft = [pygame.image.load('left.png')]
walkTop = [pygame.image.load('top.png')]
walkDown = [pygame.image.load('down.png')]
char = pygame.image.load('stand.png')

clock = pygame.time.Clock()

screenWidth = 200
x = 0
y = 0
width = 25
height = 25
vel = 5

left = False
right = False
top = False
down = False
walkCount = 0

def redrawGameWindow():
    global walkCount


    win.fill((0,0,0))

    if walkCount + 1 >= 5:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount], (x,y))
        walkCount += 1
    elif top:
        win.blit(walkTop[walkCount], (x,y))
        walkCount += 1
    elif down:
        win.blit(walkDown[walkCount], (x,y))
        walkCount += 1
    else:
        win.blit(char,(x,y))

    pygame.display.update()

#Main Loop
run = True

while run:
    clock.tick(4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        right = True
        left = False
    elif keys[pygame.K_UP] and y > vel:
        y -= vel
        top = True
        down = False
    elif keys[pygame.K_DOWN] and y < screenWidth - height - vel:
        y += vel
        down = True
        top = False
    else:
        right = False
        left = False
        top = False
        down = False
        walkCount = 0


    redrawGameWindow()

pygame.quit()
