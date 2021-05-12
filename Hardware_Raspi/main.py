
"""
Created on Sat Feb 8 18:12:17 2021

@author: abhin
"""
import signal
import sys
import pitch_estimate
from user_input import user_input
import LCD_raspi as LCD
import time
import RPi.GPIO as GPIO
import interrupt_raspi as interrupt
from realtimewire import realwire
from musicplotraspi import Music as dt

BUTTON_INSTRU_GPIO = 16
BUTTON_T_P_GPIO = 26
BUTTON_MODE_GPIO=20
BUTTON_PLAY_GPIO=5
BUTTON_STOP_GPIO=6
BUTTON_FAST_GPIO=10
BUTTON_SLOW_GPIO=9
BUTTON_EXIT_GPIO=11

LCD_LINE_1 = 0x80 	
LCD_LINE_2 = 0xC0 	
LCD_CHR = GPIO.HIGH
LCD_CMD = GPIO.LOW

instrument_selected=0
target_pitch_selected=0
mode_selected=0

instruments=["Violin","Veena","Flute"]
Target_pitch=["A","B","B#","C","C#","D","D#","E","F","F#","G","G#"]
digital_tanpura=dt()			#initializing digital tanpura

def instrument_pressed_callback(channel):
	global instrument_selected
	if instrument_selected==2:
		instrument_selected=0
	else:
		instrument_selected+=1
	print("instrument changed")
def target_pitch_callback(channel):
	global target_pitch_selected
	if target_pitch_selected==11:
		target_pitch_selected=0
	else:
		target_pitch_selected+=1
	print("Target Pitch Changed")
def mode_callback(channel):
	global mode_selected,instrument_selected,target_pitch_selected,instruments,Target_pitch,digital_tanpura
	LCD.lcd_send_byte(LCD_LINE_2, LCD_CMD)
	LCD.lcd_message("MODE CHANGE")
	if mode_selected==0:
		digital_tanpura=dt()
		mode_selected=1
	elif mode_selected==1 :
		digital_tanpura.sound(instruments[instrument_selected],Target_pitch[target_pitch_selected],"Stop")
		mode_selected=2
	else:
		LCD.lcd_message("wire")
		
		mode_selected=0
	#time.sleep(0.5)
	if mode_selected==0:
		LCD.lcd_message("PITCH DETECTION")
	else:
		LCD.lcd_message("DIGITAL TANPURA")
		digital_tanpura.lcd_mc()
		
		#digital_tanpura.sound(instruments[instrument_selected],Target_pitch[target_pitch_selected],"Play")
	
	print("mode change")
	
def play_callback(channel):
	global mode_selected,instrument_selected,target_pitch_selected,instruments,Target_pitch,digital_tanpura
	if mode_selected==1:
		print("playing")
		digital_tanpura.sound(instruments[instrument_selected],Target_pitch[target_pitch_selected],"Play")
	
def stop_callback(channel):
	global mode_selected,instrument_selected,target_pitch_selected,instruments,Target_pitch,digital_tanpura
	digital_tanpura.sound(instruments[instrument_selected],Target_pitch[target_pitch_selected],"Stop")
	
def fast_callback(channel):
	global mode_selected,instrument_selected,target_pitch_selected,instruments,Target_pitch,digital_tanpura
	digital_tanpura.sound(instruments[instrument_selected],Target_pitch[target_pitch_selected],"Fast")

def slow_callback(channel):
	global mode_selected,instrument_selected,target_pitch_selected,instruments,Target_pitch,digital_tanpura
	digital_tanpura.sound(instruments[instrument_selected],Target_pitch[target_pitch_selected],"Slow")
	

values=str(Target_pitch[target_pitch_selected])
targets = user_input(str(Target_pitch[target_pitch_selected]))


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_INSTRU_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_T_P_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_MODE_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PLAY_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_STOP_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_FAST_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_SLOW_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.add_event_detect(BUTTON_INSTRU_GPIO, GPIO.FALLING, 
	callback=instrument_pressed_callback, bouncetime=500)
GPIO.add_event_detect(BUTTON_MODE_GPIO, GPIO.FALLING, 
	callback=mode_callback, bouncetime=500)
GPIO.add_event_detect(BUTTON_T_P_GPIO, GPIO.FALLING, 
	callback=target_pitch_callback, bouncetime=500)
GPIO.add_event_detect(BUTTON_PLAY_GPIO, GPIO.FALLING, 
	callback=play_callback, bouncetime=500)
GPIO.add_event_detect(BUTTON_STOP_GPIO, GPIO.FALLING, 
	callback=stop_callback, bouncetime=500)
GPIO.add_event_detect(BUTTON_FAST_GPIO, GPIO.FALLING, 
	callback=fast_callback, bouncetime=500)
GPIO.add_event_detect(BUTTON_SLOW_GPIO, GPIO.FALLING, 
	callback=slow_callback, bouncetime=500)

signal.signal(signal.SIGINT, interrupt.signal_handler)
#signal.pause()
def algo():
	while (True):
		
		if(mode_selected==1):
			pass
			
		elif (mode_selected==2):
			realwire()
		else:
			values=str(Target_pitch[target_pitch_selected])
			targets = user_input(str(Target_pitch[target_pitch_selected]))

			
			pitch,target_pitch,target_str,isittuned,correction_value=pitch_estimate.pitch(targets)
			LCD.lcd_init()

			LCD.lcd_send_byte(LCD_LINE_1, LCD_CMD)
			print(instruments[instrument_selected]+"  "+str(pitch)+" "+str(Target_pitch[target_pitch_selected]))
			LCD.lcd_message(instruments[instrument_selected]+"  "+str(pitch)+" "+str(Target_pitch[target_pitch_selected]))
			LCD.lcd_send_byte(LCD_LINE_2, LCD_CMD)
			
			if (pitch==0):
				LCD.lcd_message("Silence Detected")	#printing Silence
			else:			#if not silence then
				if (correction_value<0):    #target is less then pitch(correction_value=target-pitch)
					if (abs(correction_value)<10):
						LCD.lcd_message("Decrease Pitch")
					else:
						LCD.lcd_message("Decrease Pitch")   
				elif (correction_value==0):

					LCD.lcd_message("Correct Pitch")
				else:

					if (abs(correction_value)<10):
						LCD.lcd_message("Increase Pitch")
					else:
						LCD.lcd_message("Increase Pitch")
				print("target pitch : "+str(values))
				print("current pitch :"+str(pitch))
				print("correct value by :"+str(correction_value))
try:

	algo()
except KeyboardInterrupt:
	LCD.lcd_send_byte(LCD_LINE_1, LCD_CMD)
	
	LCD.lcd_message(" "*16)
	LCD.lcd_send_byte(LCD_LINE_2, LCD_CMD)
	LCD.lcd_message(" "*16)
	GPIO.cleanup()
finally:
	GPIO.cleanup()