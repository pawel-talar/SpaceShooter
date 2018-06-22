import pygame
import settings as stng
import bullet as blt
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        x = random.randint(0, stng.screen_resolution[0])
        self.pos = [x, 20]
        self.bullet_power = 1
        self.life = 3
        self.move_vec = 1
        self.index = 0
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 64, 64)
        self.is_dead = False
        self.images = stng.loadAnims("enemy0", 30)
        self.image = self.images[self.index]

    def move(self):
        self.rect.y += self.move_vec

    def upgrade(self):
        self.bullet_power += 1
        self.life += 1

    def shoot(self, tab):
        x = random.randint(0, 100)
        if x > 25 and x < 29 and not self.is_dead:
            tab.append(blt.Bullet((self.rect.x + 32, self.rect.y + 62), 1, self.bullet_power))
            return True
        return False

    def crash(self):
        self.is_dead = True
        #self.images = stng.loadAnims("enemy_crash0", 1)
        self.index = 0

    def update(self):
        if self.is_dead == False:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        else:
            if self.index < len(self.images)-1:
                self.index += 1
            else:
                self.kill()
        self.image = self.images[self.index]