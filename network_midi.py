#!/usr/bin/python

#Network midi (v0.02) 3-22-14 1644

#accept network connection and receive midi data. Then pass the data to main.
#The goal of this is to be as close to pygame.midi as possible so they can be used interchangeably with no modifications.

import pygame
import pygame.midi
import socket
from multiprocessing import Process, Value, Pipe, Lock
from time import sleep

PORT=50007


def get_connection():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', PORT))
	s.listen(1)
	conn, addr = s.accept()
	return conn



def server_loop(parent, status, lock):
	
	conn=get_connection()
	
	out=[]
	looping=True
	while looping: 
		
		if status.value==0:
			looping=False
			
		elif status.value==1: #Listen
			try:
				out.append(conn.recv(1024))
				
			except socket.error:
				lock.acquire()
				print('Connection lost')
				lock.release()
				conn=get_connection()
				
		elif status.value==2: #Send data
			lock.acquire()
			print('send!')
			lock.release()
			parent.send(out)
			out=[]
			status.value=1
			
		elif status.value==3:
			parent.recv()
			status.value=1
			
		sleep(.1)
		




#server contoller acts as Input=pygame.midi.Input(device)
#This may be removed with further testing.
#This can be replaced with just reassigning the server to the input object.

def create_server_controller(new_server): #mimic the Input class to increase compatablity 
	
	class server_controller():
		server=new_server
		
		def pause(self):
			self.server.pause()
			
		def unpause(self):
			self.server.unpause()
		
		def read(self, num_events):
			return( self.server.read(num_events) )
		
		def close(self): #Pretend to close midi stream
			pass 
				
	return server_controller()
			
			
		
		
	


def create_server():
	
	class midi_server():
		
		class status: #use english instead of numbers when passing status to the process.
			kill=0
			listen=1
			read=2
			pause=3
					
		
		def __init__(self): #init the process and comm objects
			self.parent, self.child = Pipe()
			self.process_status=Value('i', self.status.listen)
			self.lock = Lock()
			self.process=Process(target=server_loop, args=(self.parent, self.process_status, self.lock))
			
		def init(self): #mimic pygame.midi.init(). Start the process
			self.process.start()
			
		def quit(self): #mimic pygame.midi.quit(). Send the kill signal
			self.process_status.value=self.status.kill
			self.process.join()
			
		def Input(self, *val): #mimic Input=pygame.midi.Input(device). val will accept the device input
			return create_server_controller(self)
		
		def read(self, num_events):
			self.process_status.value=self.status.read
			return(self.child.recv()[0:num_events])
		
		def pause(self):
			self.process_status.value=self.status.pause
		
		def unpause(self):
			self.process_status.value=self.status.read
			self.child.send(1)
		
		
		
		
		
		
	return midi_server()
		
	

		
if __name__=='__main__':
	
	print('main loop')
	midi_handler=create_server()
	midi_handler.init()
	midi_input=midi_handler.Input(0)
	print('done')
	sleep(1)
	for i in range(10):
		print(midi_input.read(10))
		sleep(1)
		
	midi_input.close()
	midi_handler.quit()
	print('!done!')
	
	
