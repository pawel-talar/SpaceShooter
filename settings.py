import os, sys
import pygame

screen_resolution = (640, 480)
player_bullet = pygame.image.load("img/bullet_player.png")
enemy_bullet = pygame.image.load("img/bullet_enemy.png")
bonus = pygame.image.load("img/bonus.png")

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