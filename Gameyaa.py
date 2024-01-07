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

SpaceShip_Width , SpaceShip_Height = 55, 60 

Yellow_Spaceship_image = pygame.image.load(
    os.path.join('Assets','yellow_spaceship.png' )) 
Yellow_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Yellow_Spaceship_image, (SpaceShip_Width,SpaceShip_Height)),270)

Red_Spaceship_image = pygame.image.load(
    os.path.join('Assets','red_spaceship.png' )) 
Red_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Red_Spaceship_image, (SpaceShip_Width,SpaceShip_Height)),90)

Background_Image = pygame.image.load(
    os.path.join('Assets','background-01.jpg'))
Background_Image_scale = pygame.transform.scale(Background_Image, (HEIGHT,WIDTH))

yellow = pygame.Rect(145, 100, SpaceShip_Width, SpaceShip_Height)
red = pygame.Rect(545, 100, SpaceShip_Width, SpaceShip_Height)

    
def draw_Window():
    SCREEN.fill(WHITE)
    SCREEN.blit(Background_Image_scale, (0,0))
    SCREEN.blit(Yellow_SpaceShip, (yellow.x, yellow.y))
    SCREEN.blit(Red_SpaceShip, (red.x, red.y))
    pygame.display.update()

def movement_yellow():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        yellow.x -= 5  
    if keys[pygame.K_RIGHT]:
        yellow.x += 5  
    if keys[pygame.K_UP]:
        yellow.y -= 5 
    if keys[pygame.K_DOWN]:
        yellow.y += 5  

def movement_red():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        red.x -= 5  
    if keys[pygame.K_d]:
        red.x += 5  
    if keys[pygame.K_w]:
        red.y -= 5 
    if keys[pygame.K_s]:
        red.y += 5  



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_Window()
        movement_yellow()  
        movement_red()   
    pygame.quit()
    
if __name__ == "__main__":
    main() 
       