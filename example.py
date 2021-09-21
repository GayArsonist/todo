import yaml

if __name__ == '__main__':
    # read yaml configuration file
    stream = open("config.yaml", 'r')
    # store yaml config in dictionary object
    dictionary = yaml.load(stream)
    # print all key/value
    for key, value in dictionary.items():
        print (key + " : " + str(value))

import pygame
from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def _init_(self):
        super(Player, self)._init_()
        self.surf = pygame.Surface((75,25))
        self.surf.fill ((225,225,225))
        self.rect = self.surf.get_rect()

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    screen.fill((0,0,0))
    screen.blit(player.surf, player.rect)
    pygame.display.flip()