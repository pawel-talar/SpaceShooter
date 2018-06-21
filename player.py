import pygame
import settings as stng

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.images = []
        self.images.append(pygame.image.load("img/player01.png"))
        self.images.append(pygame.image.load("img/player02.png"))
        self.images.append(pygame.image.load("img/player03.png"))
        self.images.append(pygame.image.load("img/player04.png"))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(310, 400, 64, 64)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]