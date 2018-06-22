import os, sys
import pygame
import gc
gc.collect()
#images and anims

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

#audios
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
crash_sound = pygame.mixer.Sound("audio/Crush8-Bit.ogg")
shoot_sound = pygame.mixer.Sound("audio/medetix__pc-bitcrushed-lazer-beam.ogg")
pygame.mixer.music.load("audio/game_theme.mp3")
pygame.mixer.music.play(4)