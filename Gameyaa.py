import pygame
import os
import random

# initiallize pygame's library
pygame.init() 

WIDTH, HEIGHT= 800,600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Adding the Logo on the window
# logo_image = pygame.image.load()
# pygame.display.set_icon(logo_image)

# displaying the name of the window 
pygame.display.set_caption("Space colliders")

FPS = 60
SPACESHIP_VEL = 7
WHITE = (255,255,255)
BACKGROUND_IMAGES = ['background-01.jpg', 'backgound2-01.jpg', 'background3.jpg', 'background4.jpg']
rand = random.randint(0,3)

SpaceShip_Width , SpaceShip_Height = 55, 60 

Yellow_Spaceship_image = pygame.image.load(
    os.path.join('Assets','yellow_spaceship.png' )) 
Yellow_SpaceShip = pygame.transform.rotate(
    pygame.transform.scale(Yellow_Spaceship_image, (SpaceShip_Width,SpaceShip_Height)),270)

Red_Spaceship_image = pygame.image.load(
    os.path.join('Assets','red_spaceship.png' )) 
Red_SpaceShip = pygame.transform.rotate(
    pygame.transform.scale(Red_Spaceship_image, (SpaceShip_Width,SpaceShip_Height)),90)

Background_Image = pygame.image.load(
    os.path.join('Assets', BACKGROUND_IMAGES[rand]))
Background_Image_scale = pygame.transform.scale(Background_Image, (WIDTH, HEIGHT))



    
def draw_Window(red,yellow):
    
    SCREEN.fill(WHITE)
    SCREEN.blit(Background_Image_scale, (0,0))
    SCREEN.blit(Yellow_SpaceShip, (yellow.x, yellow.y))
    SCREEN.blit(Red_SpaceShip, (red.x, red.y))
    pygame.display.update()

def movement_yellow(red,yellow):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and yellow.x - SPACESHIP_VEL > 0:
        yellow.x -= SPACESHIP_VEL  
    if keys[pygame.K_RIGHT] and yellow.x < WIDTH/2 - SpaceShip_Width - 10:
        yellow.x += SPACESHIP_VEL  
    if keys[pygame.K_UP] and yellow.y - SPACESHIP_VEL > 0:
        yellow.y -= SPACESHIP_VEL 
    if keys[pygame.K_DOWN] and yellow.y < HEIGHT - SpaceShip_Height:
        yellow.y += SPACESHIP_VEL  

def movement_red(red,yellow):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and red.x > WIDTH/2 + 10:
        red.x -= SPACESHIP_VEL  
    if keys[pygame.K_d] and red.x < WIDTH - SpaceShip_Width - 8:
        red.x += SPACESHIP_VEL  
    if keys[pygame.K_w] and red.y - SPACESHIP_VEL > 0:
        red.y -= SPACESHIP_VEL 
    if keys[pygame.K_s] and red.y < HEIGHT - SpaceShip_Height:
        red.y += SPACESHIP_VEL  



def main():
    print(rand)
    yellow = pygame.Rect(145, 100, SpaceShip_Width, SpaceShip_Height)
    red = pygame.Rect(545, 100, SpaceShip_Width, SpaceShip_Height)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_Window(red,yellow)
        movement_yellow(red,yellow)  
        movement_red(red,yellow)   
    pygame.quit()
    
if __name__ == "__main__":
    main() 
       