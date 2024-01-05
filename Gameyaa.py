import pygame

pygame.init()
SCREEN = pygame.display.set_mode((800,600))

#Adding the Logo on the window
logo_image = pygame.image.load('car.png')
pygame.display.set_icon(logo_image)

#displaying the name of the window 
pygame.display.set_caption("Gameyaa")

#creating a player
player = pygame.rect((350,250,50,50))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                
pygame.quit()
        