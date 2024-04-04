import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_COUNT = 0  # Initializing coin count

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):  # Define a coin class
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Coin image
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), random.randint(20, SCREEN_HEIGHT - 20))

    def update(self):
        pass


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        if self.rect.top > 0:
              if pressed_keys[K_UP]:
                  self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:        
              if pressed_keys[K_DOWN]:
                  self.rect.move_ip(0, 5)


P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

coins = pygame.sprite.Group()  # Group for coins


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

COIN_APPEAR = pygame.USEREVENT + 2  # Custom event for coin appearance
pygame.time.set_timer(COIN_APPEAR, 2000)  # Set coin appearance every 5 seconds

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5
        if event.type == COIN_APPEAR:  # Check if it's time for a new coin
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    coin_count = font_small.render("Coins: " + str(COIN_COUNT), True, BLACK)  # Display coin count
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_count, (300,10))

    # Check for coin collection
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)  # The True argument will remove the coin upon collision
    if collected_coins:
        COIN_COUNT += len(collected_coins)  # Increase coin count by the number of coins collected

    for entity in all_sprites:
        if hasattr(entity, 'move'):
            entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()      

    pygame.display.update()
    FramePerSec.tick(FPS)
