import pygame #importing pygame module
pygame.init() #initialization

win = pygame.display.set_mode((500,500)) #main window

pygame.display.set_caption("First game") #caption of the main window

screenWidth = 500


#player attributes

x = 50

y = 425

width = 40

height = 60

vel = 5

run = True

isJump = False
jumpcount = 10

#main game loop

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #key pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel :
        x-=vel
    if keys[pygame.K_RIGHT] and x < 500-width-vel:
        x+=vel
    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y-=vel
        if keys[pygame.K_DOWN] and y < 500-height-vel :
            y+=vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg -=1
                
            y -= (jumpcount ** 2)*0.5*neg
            jumpcount -= 1
        else:
            isJump = False
            jumpcount=10
            
        


    win.fill((0,0,0)) #avoiding collison
    pygame.draw.rect(win,(250,0,0),(x,y,width,height)) #shape
    pygame.display.update() #updating the game state



pygame.quit()
