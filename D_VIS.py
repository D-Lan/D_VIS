#!/usr/bin/python

#D_VIS Main Script (v0.00)

import pygame
import sys
import os
import visualizer
import pygame.midi as midi
#os.system('clear')


class midi():
	
	channels=[x for x in range(0,15)]
	Input=None
	
	def __init__(self):
		pygame.midi.init()
		self.Input=midi.Input(0)
		
	def update(self):
		##################
		



	







screen=pygame.display.set_mode((1152,864))
fpsClock= pygame.time.Clock()

while True:
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT: sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
		
	midi.update()
	vis.update()
	pygame.display.update()
	fpsClock.tick(30)
	
	
pygame.midi.quit()