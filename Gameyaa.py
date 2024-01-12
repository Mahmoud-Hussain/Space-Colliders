import pygame
import os
import random
pygame.font.init()
pygame.init() 
pygame.mixer.init()

WIDTH, HEIGHT= 800,670
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
MAX_HEALTH = 10

WHITE = (255,255,255)
RED = (255,0,0) 
YELLOW = (255,255,0)
BLACK = (0, 0, 0)


BULLET_SHOOT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'shotgun-firing-4-6746.mp3'))

health_font = pygame.font.SysFont('comicsans',20 )
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
Background_Image_scale = pygame.transform.scale(Background_Image, (WIDTH, 600))



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
    SCREEN.fill(BLACK)
    SCREEN.blit(Background_Image_scale, (0,70))
    
    yellow_health_bar = HealthBarYellow(10,10,200,20,MAX_HEALTH,yellow_health)
    yellow_health_bar.draw(SCREEN)
    red_health_bar = HealthBarRed(WIDTH - 210, 10, 200, 20,MAX_HEALTH, red_health)
    red_health_bar.draw(SCREEN)
    red_health_txt = health_font.render("Health of red", 1, WHITE)
    yellow_health_txt = health_font.render("Health of yellow" , 1, WHITE)
    SCREEN.blit(red_health_txt, (WIDTH-red_health_txt.get_width() - 10, 25))
    SCREEN.blit(yellow_health_txt, (10,25))
    SCREEN.blit(Yellow_SpaceShip, (yellow.x, yellow.y))
    SCREEN.blit(Red_SpaceShip, (red.x, red.y))
    
    
    for bullet in red_bullets:
        pygame.draw.rect(SCREEN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(SCREEN, YELLOW, bullet)
    
    pygame.display.update()

def movement_yellow(yellow):  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and yellow.x > 0 :
        yellow.x -= SPACESHIP_VEL  
    if keys[pygame.K_d] and yellow.x < WIDTH/2 -SpaceShip_Width-  10:
        yellow.x += SPACESHIP_VEL  
    if keys[pygame.K_w] and yellow.y > 72:
        yellow.y -= SPACESHIP_VEL 
    if keys[pygame.K_s] and yellow.y < HEIGHT - SpaceShip_Height:
        yellow.y += SPACESHIP_VEL  

def movement_red(red):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and red.x > WIDTH/2 + 10:
        red.x -= SPACESHIP_VEL  
    if keys[pygame.K_RIGHT] and red.x < WIDTH - SpaceShip_Width - 8:
        red.x += SPACESHIP_VEL  
    if keys[pygame.K_UP] and red.y > 72:
        red.y -= SPACESHIP_VEL 
    if keys[pygame.K_DOWN] and red.y  < HEIGHT - SpaceShip_Height:
        red.y += SPACESHIP_VEL

def define_winner(text):
    draw_text = winner_font.render(text, 1, BLACK)
    draw_text1 = winner_font.render(text, 1, RED)
    SCREEN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 
                            2, HEIGHT/2 - draw_text.get_width()/5))
    SCREEN.blit(draw_text1, (WIDTH/2 + 5 - draw_text.get_width() / 
                            2, HEIGHT/2 +5 - draw_text.get_width()/5))
    pygame.display.update()
         
class HealthBarYellow():
    def __init__(self, x, y, w, h, max_hp, hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.max_hp = max_hp
    
    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))
        
class HealthBarRed():
    def __init__(self, x, y, w, h, max_hp, hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.max_hp = max_hp
    
    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))


def main():
    run = True
    while run:
        yellow = pygame.Rect(145, 100, SpaceShip_Width, SpaceShip_Height)
        red = pygame.Rect(545, 100, SpaceShip_Width, SpaceShip_Height)

        red_bullets = []
        yellow_bullets = []

        red_health = 10
        yellow_health = 10

        clock = pygame.time.Clock()

        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_v and len(yellow_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                        yellow_bullets.append(bullet)
                        BULLET_SHOOT_SOUND.play()
                    if event.key == pygame.K_SLASH and len(red_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                        red_bullets.append(bullet)
                        BULLET_SHOOT_SOUND.play()
                    if event.key == pygame.K_r:
                        yellow = pygame.Rect(145, 100, SpaceShip_Width, SpaceShip_Height)
                        red = pygame.Rect(545, 100, SpaceShip_Width, SpaceShip_Height)

                        red_bullets = []
                        yellow_bullets = []

                        red_health = 10
                        
                        yellow_health = 10

                        game_over = False

                if event.type == red_hit:
                    red_health -= 1
                if event.type == yellow_hit:
                    yellow_health -= 1
                
                    

                winner_text = ""
                if red_health <= 0:
                    winner_text = "Yellow wins!"
                    game_over = True

                if yellow_health <= 0:
                    winner_text = "Red wins!"
                    game_over = True
                    
                
                if winner_text != "":
                    define_winner(winner_text)
                    pygame.time.delay(2000)
                    break  # Exit the event loop when the game ends
                
            handle_bullets(yellow_bullets, red_bullets, yellow, red)

            draw_Window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
            movement_yellow(yellow)
            movement_red(red)

            clock.tick(FPS)

            if winner_text != "":
                pygame.time.delay(5000)  # Delay before restarting
                break

if __name__ == "__main__":
    main()
