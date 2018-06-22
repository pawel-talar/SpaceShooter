import pygame
import settings as stng

class Bullet(pygame.sprite.Sprite):
    # p = 1 - bullet of enemy, 0 - bullet of player
    def __init__(self, pos, p, power):
        super(Bullet, self).__init__()
        self.pos = pos
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 2, 5)
        self.is_collide = False
        self.power = power
        if p == 0:
            self.image = stng.player_bullet
            self.speed_vec = -4
        elif p == 1:
            self.image = stng.enemy_bullet
            self.speed_vec = 4

    def move(self):
        self.rect.y += self.speed_vec

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def catch(self):
        self.is_collide = True