from matplotlib.pyplot import magnitude_spectrum
import pygame, sys, random 

pygame.init()

size = (width, height) = 478,639
(width,height) = 478,639
screen = pygame.display.set_mode(size)

#game variables
ground_scroll = 0
scroll_speed = 4
game_over = False
flying = False

speed = [0,0]
gravity = 0.4
class MainCharacter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./bluebird.png")
        self.image = pygame.transform.scale(self.image, (43,30))

        self.rect = self.image.get_rect()
        self.rect.center = (width/4, height/2)
    def update(self, is_true):
        if is_true:
            new_image = pygame.transform.rotate(self.image, 30)
        else:
            new_image = pygame.transform.rotate(self.image, -60)
        old_center = self.rect.center
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.center = old_center


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x,y, z):
        super().__init__()
        self.image = pygame.image.load("./pipe.png")
        self.image = pygame.transform.scale(self.image, (80, height/2))

        self.rect = self.image.get_rect()
        if z == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x,y]
        elif z == -1:
            self.rect.topleft = [x,y]
        
        



main_sprite = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()    

bird = MainCharacter()
main_sprite.add(bird)

bot_obstacle = Obstacle(300, int(height/2), -1)
top_obstacle = Obstacle(300, int(height/2), 1)
obstacle_group.add(bot_obstacle)
obstacle_group.add(top_obstacle)

clock = pygame.time.Clock()
bgc = (135,206,235)

bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (500,560))
ground = pygame.image.load("ground.png")
ground = pygame.transform.scale(ground, (520,76))



def gameOver():
    speed[1] = 0
    ##text = pygame.font.Font('Times New Roman', 40)
    
is_rotated = False

while True:
    clock.tick(60)
    main_sprite.draw(screen)
    obstacle_group.draw(screen)
    screen.blit(bg, (0,0))
    screen.blit(ground, (ground_scroll,560))
    

    ##scrolling background
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 20:
        ground_scroll = 0
   

    key = pygame.key.get_pressed()

    ##sprite rotation 
    if speed[1]<0 and is_rotated == False:
        bird .update(True)
        is_rotated = True
    ##if speed[1]>0 and is_rotated == True:
    ##   main.update(False)
    ##    is_rotated = False

    ##movement control for sprite
    if key[pygame.K_SPACE]:
        speed[1] -= .8
    
    ##sprite movement limitation settings
    if bird.rect.bottom > 560:
        speed[1] = 0
        gameOver()
    if bird.rect.top < 0:
        speed[1] = 0
    speed[1] += gravity
    bird.rect = bird.rect.move(speed)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
