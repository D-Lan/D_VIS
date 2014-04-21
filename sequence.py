#!/usr/bin/python

#Theaded image loader (v0.01)
#Load images in a thread so Main can go on.
#Contain loaded sequences in a dict

import threading
import pygame

image={}

def load_sequence_thread(path, Range):
	image[path]=[i for i in Range]
	for i in Range:
		suffix=str(i).zfill(4)
		image[path][i]=(pygame.image.load(path+suffix+'.png' ))


def load(path, Range):
	thread=threading.Thread(target=load_sequence_thread, args=(path, Range))
	thread.start()













