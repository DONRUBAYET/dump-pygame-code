import pygame #importing pygame module
pygame.init() #initialization

win = pygame.display.set_mode((500,500)) #main window

pygame.display.set_caption("First game") #caption of the main window


#player attributes
x = 50

y = 50

width = 40

height = 60

vel = 10

run = True

#main game loop

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #key pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=vel
    if keys[pygame.K_RIGHT]:
        x+=vel
    if keys[pygame.K_UP]:
        y-=vel
    if keys[pygame.K_DOWN]:
        y+=vel


    win.fill((0,0,0)) #avoiding collison
    pygame.draw.rect(win,(250,0,0),(x,y,width,height)) #shape
    pygame.display.update() #updating the game state



pygame.quit()
