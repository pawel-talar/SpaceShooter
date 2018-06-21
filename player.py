import pygame
import os
import settings as stng
import bullet as blt

def loadAnims(phrase, repeat):
    imgs = os.listdir("img")
    imgs.sort()
    images = []
    for img in imgs:
        # print ('img/' + img)
        if img.startswith(phrase):
            images.append(pygame.image.load('img/' + img))
            current_size = len(images)
            for i in range(repeat):
                images.append(0)
                images[current_size + i] = images[current_size - 1]
    return images

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.pos = [310, 400]
        self.bullet_power = 1
        self.life = 3
        self.move_vec = 0
        self.index = 0
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 64, 64)
        self.is_dead = False
        self.images = loadAnims("player0", 30)
        self.image = self.images[self.index]

    def move(self):
        if (stng.screen_resolution[0] - 64 >= self.rect.x + self.move_vec and self.rect.x + self.move_vec >= 0):
            self.rect.x += self.move_vec

    def upgrade(self):
        self.bullet_power += 1
        self.life += 1

    def shoot(self, tab):
        tab.append(blt.Bullet((self.rect.x+32, self.rect.y), 0, self.bullet_power))

    def crash(self):
        self.is_dead = True
        self.images = loadAnims("player_crash", 1)
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