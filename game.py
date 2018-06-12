#!/usr/bin/python 3

import os, sys	
import pygame
from pygame.locals import *
import settings

class Game(object):
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Space Shooter')
		self.screen_res = settings.screen_resolution
		self.screen = pygame.display.set_mode(self.screen_res, 32)
	def input_event(events):
		for event in events:
			if(event.type == QUIT):
				sys.exit(0)
	def run(self):
		pygame.display.update()
		while True:
   			self.input_event(pygame.event.get())