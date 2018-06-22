#!/usr/bin/python 3

import os, sys
import pygame
import settings as stng
import player as plr
import bonus as bns
import enemy as enm
import random


class Game(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("monospace", 15)
        self.screen_res = stng.screen_resolution
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_res)
        self.time = pygame.time.get_ticks()
        self.refresh_rate = 40
        pygame.display.set_caption('Space Shooter')
        self.is_end = False
        self.is_running = True
        self.vitality_of_enemies = 1
        self.player = plr.Player()
        self.player_group = pygame.sprite.Group(self.player)
        self.enemies_group = pygame.sprite.Group()
        self.bonuses_group = pygame.sprite.Group()
        self.enemy_bullets_group = pygame.sprite.Group()
        self.player_bullets_group = pygame.sprite.Group()
        self.score = 0
        self.bonuses = []
        self.bullets = []
        self.enemies = []

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
                self.player.move_vec = -2
            elif (self.keys[pygame.K_RIGHT] and self.is_running):
                self.player.move_vec = 2
            else:
                self.player.move_vec = 0
            if(self.keys[pygame.K_SPACE]):
                self.player.shoot(self.bullets)
                self.player_bullets_group.add(self.bullets[-1])

    def run(self):
        self.loop()

    def pause(self):
        self.is_running = False

    def generate_bonuses(self):
        x = random.randint(0, 100000)
        if x < 5:
            #print("SUKCES!")
            self.bonuses.append(bns.Bonus())

    def generate_enemies(self):
        x = random.randint(0, 1000)
        if x < 123 and x > 100:
            #print("SUKCES!")
            self.enemies.append(enm.Enemy())
            self.enemies_group.add(self.enemies[-1])

    def game_over(self):
        self.is_end = True

    def update_scoreboard(self):
        label1 = self.font.render("Score: " + str(self.score), 20, (255, 255, 0))
        label2 = self.font.render("HP: " + str(self.player.life), 20, (255, 0, 0))
        self.screen.blit(label1, (0, 0))
        self.screen.blit(label2, (0, 20))

    def update_battlefield(self):
        for bonus in self.bonuses:
            bonus.move()

        for bullet in self.bullets:
            bullet.move()

        for enemy in self.enemies:
            enemy.move()
            x = enemy.shoot(self.bullets)
            if x:
                self.enemy_bullets_group.add(self.bullets[-1])

        self.player_group.update()
        self.enemies_group.update()
        self.player_bullets_group.update()
        self.enemy_bullets_group.update()
        self.player_group.draw(self.screen)
        self.enemies_group.draw(self.screen)
        self.enemy_bullets_group.draw(self.screen)
        self.player_bullets_group.draw(self.screen)

    def check_collisions(self):
        if not self.player.is_dead:
            b2p = pygame.sprite.groupcollide(self.enemy_bullets_group, self.player_group, True, False)
            print (b2p)
            for collision in b2p:
                self.player.life -= 1
                if self.player.life <= 0:
                    self.player.crash()
                    self.game_over()
            b2b = pygame.sprite.groupcollide(self.player_bullets_group, self.bonuses_group, True, True)
            for collision in b2b:
                self.player.life += 1

        for e in self.enemies_group:
            x = pygame.sprite.spritecollideany(e, self.player_bullets_group)
            if x != None:
                self.score += 10
                e.crash()
                x.kill()

    def loop(self):
        while (not self.is_end):
            if (not self.is_running):
                self.input_event()
            while (self.is_running):
                self.screen.fill((0, 0, 0))
                self.generate_bonuses()
                self.generate_enemies()
                self.update_battlefield()
                self.player.move()
                self.update_scoreboard()
                pygame.display.flip()
                self.input_event()
                self.check_collisions()
                self.clock.tick(self.refresh_rate)




