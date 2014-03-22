#!/usr/bin/python

#Planning for D_VIS (v0.01)

import pygame #used to handle keyboard input and possibly display?
import sys	#for the exit method. if exit is the only method used under sys then change to from sys import exit



#visualizer will contain all images, image handling methods, and math used to load and driver the visualizer
#Name subject to change
#Pygame window will either be handled in visualizer or in this main loop.
import visualizer



#ui is the text based interface that the user will see and use to change outputs and visualizers
#this will need basic keyboard input from the pygame.event in this main loop
import ui



#Skip the formalities and go straigt to assignment. No promting user about avaliable devices.
#network_midi will work interchangably with pygame.midi.Input for more flexability
import network_midi as midi_input #



#Either prompt user or manualy add device integer.
#Manualy would be faster but less userfriendly
midi_output=get_midi_output()

	

#exit() instead of just calling sys.exit() makes adding calls easier than adding them in the main loop
def exit(): #Quit method
	sys.exit()
	


#This will loop until the user exits
#This will handle everything that happens
while 1: #Main loop
	
	for event in pygame.event.get(): #Pygame event loop
		
		if event.type == pygame.QUIT: exit() #exit from the exit button
		
		elif event.type == pygame.KEYDOWN: #If event is a key press
			if event.key == pygame.K_ESCAPE:exit() #exit by hitting the escape key. 
			
	
	midi = midi_input.read() #use interchangably between network_midi and pygame.midi
	visualizer.update(midi) #Update the visualizer with the midi input
	pygame.display.update() #Possibly remove this if pygame display is handled in visualizer.
	fpsClock.tick(30) #Keep a constant framerate
			
			
#Above is the bare minimum for a show. Below are extras.


#This will handle midi output to the light console. If interface is possible
#This will probably use usb to midi output
import midi_light 


#This will handle the audio input analysis
#This will try to mimic midi_input as close as possible to stay consistant
import fft_input


#Get camera input. This will probably get moved into visualizer to keep it simple
#This will probably never be implemented. This is just an idea.
import web_cam

