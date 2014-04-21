#!/usr/bin/python


#This will handle all geometry and textures showing on screen.
#Main will handle drawing the geometry.
#Main will have access to visualizer info

#Step-by-step

#Import pygame objects so textures and rects can be used.
#Load all visualizers. All visualizers will be contained in this script
#Initialize the first visualizer. Load all images.
#Wait for Main to pass on midi (and fft) info
#Update all geometry and textures
#Main will then draw the visualizer

import pygame
import sequence


def falloff(val): #Square falloff for basic visuals
	test=int(   val-   (val**2)/5   )
	if test<1:
		return 0
	else:
		return test




def create_bar(new_path, new_range):
	
	class bar():
		Range=new_range
		path=new_path
		channels=[]
		value=0
		images=None
		
		def load(self): #begin_loading will start a seperate process that will obtain all images
			sequence.load(
				self.path, self.Range)
		
		
		def update(self):
			global midi
			
			for channel in self.channels:
				if midi[channel]<self.value:
					self.value=midi[channel]
				else:
					self.value=falloff(self.value)
					
	return(bar())
	


def create_TestVis():
	
	class TestVis():
		
		elements=[create_bar('/home/dylan/Python/D_VIS/Vis/TestVis/Bar1/Bar', range(100)),
				  create_bar('/home/dylan/Python/D_VIS/Vis/TestVis/Bar2/Bar', range(100)),
				  create_bar('/home/dylan/Python/D_VIS/Vis/TestVis/Bar3/Bar', range(100)),
				  create_bar('/home/dylan/Python/D_VIS/Vis/TestVis/Bar4/Bar', range(100)),				  
				  create_bar('/home/dylan/Python/D_VIS/Vis/TestVis/Bar5/Bar', range(100)),				  
				  create_bar('/home/dylan/Python/D_VIS/Vis/TestVis/Bar6/Bar', range(100))				  
			]
		
		def init(self):
			for element in self.elements: element.load()
			
		'''
		def finnish_init(self):
			for element in self.elements: element.finnish_loading()
			load.end()
		'''
		
		def update(self):
			for element in self.elements: element.update()
	
	return(TestVis())
	
	

TV=create_TestVis()
TV.init()










