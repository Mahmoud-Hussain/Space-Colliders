import pygame
import os
import random
pygame.font.init()
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
Bullets_vel = 7
MAX_BULLETS = 3


WHITE = (255,255,255)
RED = (255,0,0) 
YELLOW = (255,255,0)

health_font = pygame.font.SysFont('comicsans',40 )
winner_font = pygame.font.SysFont('comicsans', 100)

yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

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



def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullets in yellow_bullets:
        bullets.x += Bullets_vel
        if red.colliderect(bullets):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullets)
        elif bullets.x > WIDTH:
            yellow_bullets.remove(bullets)

    for bullets in red_bullets:
        bullets.x -= Bullets_vel
        if yellow.colliderect(bullets):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullets)
        elif bullets.x < 0:
                red_bullets.remove(bullets)

 
    
def draw_Window(red,yellow,red_bullets, yellow_bullets, red_health, yellow_health):
    
    SCREEN.blit(Background_Image_scale, (0,0))
    red_health_txt = health_font.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_txt = health_font.render("Health: " + str(yellow_health), 1, WHITE)
    SCREEN.blit(red_health_txt, (WIDTH-red_health_txt.get_width() - 10, 10))
    SCREEN.blit(yellow_health_txt, (10,10))
    SCREEN.blit(Yellow_SpaceShip, (yellow.x, yellow.y))
    SCREEN.blit(Red_SpaceShip, (red.x, red.y))
    
    
    for bullet in red_bullets:
        pygame.draw.rect(SCREEN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(SCREEN, YELLOW, bullet)
    
    pygame.display.update()

def movement_yellow(yellow):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and yellow.x - SPACESHIP_VEL > 0:
        yellow.x -= SPACESHIP_VEL  
    if keys[pygame.K_RIGHT] and yellow.x < WIDTH//2 - SpaceShip_Width - 10:
        yellow.x += SPACESHIP_VEL  
    if keys[pygame.K_UP] and yellow.y - SPACESHIP_VEL > 0:
        yellow.y -= SPACESHIP_VEL 
    if keys[pygame.K_DOWN] and yellow.y < HEIGHT - SpaceShip_Height:
        yellow.y += SPACESHIP_VEL  

def movement_red(red):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and red.x > WIDTH/2 + 10:
        red.x -= SPACESHIP_VEL  
    if keys[pygame.K_d] and red.x < WIDTH - SpaceShip_Width - 8:
        red.x += SPACESHIP_VEL  
    if keys[pygame.K_w] and red.y - SPACESHIP_VEL > 0:
        red.y -= SPACESHIP_VEL 
    if keys[pygame.K_s] and red.y < HEIGHT - SpaceShip_Height:
        red.y += SPACESHIP_VEL  

def define_winner(text):
    draw_text = winner_font.render(text, 1, WHITE)
    SCREEN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 
                            2, HEIGHT/2 - draw_text.get_width()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    yellow = pygame.Rect(145, 100, SpaceShip_Width, SpaceShip_Height)
    red = pygame.Rect(545, 100, SpaceShip_Width, SpaceShip_Height)
    
    red_bullets = []
    yellow_bullets = []
    
    red_health = 10
    yellow_health = 10
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_l and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5 )
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_v and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 -2, 10, 5 )
                    red_bullets.append(bullet)
        
            if event.type == red_hit:
                red_health -= 1 
            if event.type == yellow_hit:
                yellow_health -= 1 
               
            winner_text = "" 
            if red_health <=0 :
                winner_text = "Yellow wins!"
            if yellow_health <=0 :
                winner_text = "Red wins!"
            if winner_text != "" :
                define_winner(winner_text)
                break
            
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        draw_Window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        movement_yellow(yellow)  
        movement_red(red)   
        
    main()
    
if __name__ == "__main__":
    main() 
       