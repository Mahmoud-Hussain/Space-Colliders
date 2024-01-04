import pygame

pygame.init()
SCREEN = pygame.display.set_mode((640,400))
    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                
pygame.quit()
        