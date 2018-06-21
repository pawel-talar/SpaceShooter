#!/usr/bin/python 3

import os, sys
import pygame
import settings as stng
import player as plr
import bonus as bns
import enemy
import random


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen_res = stng.screen_resolution
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_res)
        self.time = pygame.time.get_ticks()
        self.refresh_rate = 150
        pygame.display.set_caption('Space Shooter')
        self.is_end = False
        self.is_running = True
        self.vitality_of_enemies = 1
        self.player = plr.Player()
        self.player_group = pygame.sprite.Group(self.player)
        self.bonuses = []

    def input_event(self):
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if (event.type == pygame.QUIT):
                sys.exit(0)
            if (self.keys[pygame.K_p]):
                if (self.is_running):
                    self.pause()
                else:
                    self.is_running = True
            if (self.keys[pygame.K_d]):
                self.player.crash()
            if (self.keys[pygame.K_LEFT] and self.is_running):
                self.player.move_vec = -1
            elif (self.keys[pygame.K_RIGHT] and self.is_running):
                self.player.move_vec = 1
            else:
                self.player.move_vec = 0

    def run(self):
        self.loop()

    def pause(self):
        self.is_running = False

    def generate_bonuses(self):
        x = random.randint(0, 10000)
        if x < 5:
            print("SUKCES!")
            self.bonuses.append(bns.Bonus())

    def update_battlefield(self):
        for bonus in self.bonuses:
            bonus.move()
            bonus.draw(self.screen)

    def loop(self):
        while (not self.is_end):
            if (not self.is_running):
                self.input_event()
            while (self.is_running):
                self.screen.fill((0, 0, 0))
                self.generate_bonuses()
                self.update_battlefield()
                self.player_group.update()
                self.player_group.draw(self.screen)
                self.player.move()
                pygame.display.flip()
                self.input_event()
                self.clock.tick(self.refresh_rate)



