from matplotlib.pyplot import magnitude_spectrum
import pygame, sys, random 

pygame.init()

size = (width, height) = 478,639
(width,height) = 478,639
screen = pygame.display.set_mode(size)

ground_scroll = 0
scroll_speed = 4

speed = [0,0]
gravity = 0.5
class MainCharacter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./bird.svg")
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect = self.image.get_rect()
        self.rect.center = (width/3, height/2)

main = MainCharacter()

main_sprite = pygame.sprite.Group()
main_sprite.add(main)

clock = pygame.time.Clock()
bgc = (135,206,235)

bg = pygame.image.load("background3.png")
bg = pygame.transform.scale(bg, (500,560))
ground = pygame.image.load("ground.png")
ground = pygame.transform.scale(ground, (520,76))



def gameOver():
    screen.fill((0,0,0))
    ##text = pygame.font.Font('Times New Roman', 40)
    

while True:
    clock.tick(60)
    screen.blit(bg, (0,0))
    screen.blit(ground, (ground_scroll,560))
    main_sprite.draw(screen)

    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 20:
        ground_scroll = 0


    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        speed[1] -= 1
    
    if main.rect.bottom > height:
        speed[1] = 0
        gameOver()
    if main.rect.top < 0:
        speed[1] = 0
    speed[1] += gravity
    ##main.rect = main.rect.move(speed)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
