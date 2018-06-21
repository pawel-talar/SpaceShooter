import pygame
import os
import settings as stng

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.pos = [310, 400]
        self.images = []
        self.bullet_power = 1
        self.life = 3
        self.images.append(pygame.image.load("img/player01.png"))
        self.images.append(pygame.image.load("img/player02.png"))
        self.images.append(pygame.image.load("img/player03.png"))
        self.images.append(pygame.image.load("img/player04.png"))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 64, 64)
        self.is_dead = False

    def move(self, par):
        self.rect.x += par

    def upgrade(self):
        self.bullet_power += 1
        self.life += 1

    def crash(self):
        self.is_dead = True
        self.images = []
        imgs = os.listdir("img")
        imgs.sort()
        print (imgs)
        for img in imgs:
            print ('img/' + img)
            if img.startswith("player_crash"):
                self.images.append(pygame.image.load('img/' + img))
                current_size = len(self.images)
                for i in range(10):
                    self.images.append(0)
                    self.images[current_size+i] = self.images[current_size-1]
        self.index = 0

    def update(self):
        if self.is_dead == False:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        else:
            if self.index < len(self.images)-1:
                self.index += 1
        self.image = self.images[self.index]