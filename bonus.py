import pygame
import settings as stng
import random

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        self.pos = [random.randint(0, stng.screen_resolution[0]-64), 20]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 64, 64)
        self.is_done = False
        self.image = stng.bonus

    def move(self):
        self.rect.y += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def catch(self):
        self.is_done = True