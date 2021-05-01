# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:24:37 2020

@author: abhin
"""
import RPi.GPIO as GPIO
import LCD_raspi as LCD
import time
import pygame
from speedchange import speed
from convertaudio import converttomp3 as tomp3
#from speedchange import speed
class Music:

	
	def __init__(self):
		
		self.frequency=1.0
		self.count=0
		self.isplaying=False
		pygame.init()
		
	def reset(self):
		self.frequency=1.0
		self.count=0
		self.isplaying=False
	def lcd_mc(self):
		LCD_LINE_1 = 0x80 	
		LCD_LINE_2 = 0xC0 	
		LCD_CHR = GPIO.HIGH
		LCD_CMD = GPIO.LOW
		LCD.lcd_send_byte(LCD_LINE_2, LCD_CMD)
		LCD.lcd_message("Digital Tanpura")
		
	def sound(self,instrument,target,command):
		frequency=1.0
		LCD_LINE_1 = 0x80 	
		LCD_LINE_2 = 0xC0 	
		LCD_CHR = GPIO.HIGH
		LCD_CMD = GPIO.LOW
		LCD.lcd_send_byte(LCD_LINE_1, LCD_CMD)
		print(instrument+"  "+str(target)+" "+"DT")
		LCD.lcd_message(instrument+"  "+str(target)+" "+"DT")
		LCD.lcd_send_byte(LCD_LINE_2, LCD_CMD)
		
		pygame.mixer.music.set_volume(1)
		self.path="MP3/"+str(instrument)+" "
		print("path set...!!! count :"+str(self.count))
		if command == "Play":
			if ((self.isplaying==False) and (self.count==0)):
				print("excuted play")
				self.count=1
				
				frequency=1
				pygame.mixer.init()
		
				pygame.mixer.music.load(self.path+str(target)+".mp3")
				
				pygame.mixer.music.play(-1)
				#self.window['-OUTPUT1-'].update(frequency)
				LCD.lcd_message("Playing...")
			else:
				if (self.count%2==1):
					pygame.mixer.music.pause()
					LCD.lcd_message("Paused   ||")
					self.count+=1
				else:
					pygame.mixer.music.unpause()
					LCD.lcd_message("Playing...")
					self.count+=1
		elif command== 'Stop':
			self.count=0
			#pygame.mixer.music.unload()
			pygame.mixer.music.stop()
			LCD.lcd_message("Stop")
		
		elif command=='Slow':
			frequency=frequency/2
			print(self.path+str(target)+".mp3"+"  "+str(frequency),end="\n")
			pygame.mixer.music.load(self.path+str(target)+".mp3")
			
			pygame.mixer.music.play(-1)
			pygame.mixer.music.stop()
			print("slow",end="\n")
			start=time.time()
			speed(self.path+str(target)+".wav",frequency)
			print("Speed changed...",end="\n")
			end=time.time()
			tomp3('changed')
			pygame.mixer.init()
			print(end-start,"\nchanged...")
			pygame.mixer.music.load("changed.mp3")
			
			pygame.mixer.music.play(-1)

			
		elif command=='Fast':
			frequency=frequency*2
			print(self.path+str(target)+".mp3"+"  "+str(frequency),end="\n")
			pygame.mixer.music.load(self.path+str(target)+".mp3")
			
			pygame.mixer.music.play(-1)
			pygame.mixer.music.stop()
			print("Fast...",end="\n")
			start=time.time()
			speed(self.path+str(target)+".wav",2)
			tomp3('changed')
			end=time.time()
			pygame.mixer.init()
			print(end-start," \n Changed...")
	
			pygame.mixer.music.load("changed.mp3")
			
			pygame.mixer.music.play(-1)