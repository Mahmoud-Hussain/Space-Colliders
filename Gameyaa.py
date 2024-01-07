import pygame
import os

# initiallize pygame's library
pygame.init() 

HEIGHT , WIDTH = 800,600
SCREEN = pygame.display.set_mode((HEIGHT,WIDTH))

# Adding the Logo on the window
# logo_image = pygame.image.load()
# pygame.display.set_icon(logo_image)

# displaying the name of the window 
pygame.display.set_caption("Space colliders")

FPS = 60

WHITE = (255,255,255)

Yellow_Spaceship_image = pygame.image.load(
    os.path.join('Assets','yellow_spaceship.png' )) 
Yellow_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Yellow_Spaceship_image, (55,60)),270)
Red_Spaceship_image = pygame.image.load(
    os.path.join('Assets','red_spaceship.png' )) 
Red_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Red_Spaceship_image, (55,60)),90)

def draw_Window():
    SCREEN.fill(WHITE)
    SCREEN.blit(Yellow_SpaceShip, (145,100))
    SCREEN.blit(Red_SpaceShip, (545,100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_Window()
             
    pygame.quit()
    
if __name__ == "__main__":
    main() 
       