#!/usr/bin/python 3

import os, sys
import pygame
import settings as stng


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen_res = stng.screen_resolution
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_res)
        self.time = pygame.time.get_ticks()
        pygame.display.set_caption('Space Shooter')
        self.is_end = False
        self.is_running = True
        self.vitality_of_enemies = 1

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

    def run(self):
        self.loop()

    def pause(self):
        self.is_running = False

    def loop(self):
        while (not self.is_end):
            if (not self.is_running):
                self.input_event()
            while (self.is_running):
                self.input_event()
                print(self.is_running)

