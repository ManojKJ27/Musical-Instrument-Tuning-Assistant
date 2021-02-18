
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

BUTTON_INSTRU_GPIO = 16
BUTTON_T_P_GPIO = 26
LCD_LINE_1 = 0x80 	
LCD_LINE_2 = 0xC0 	
LCD_CHR = GPIO.HIGH
LCD_CMD = GPIO.LOW
instrument_selected=0
target_pitch_selected=0
def mode_pressed_callback(channel):
    print("mode changed")
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

instruments=["Violin","Veena","Flute"]
Target_pitch=["A","B","B#","C","C#","D","D#","E","F","F#","G","G#"]
values=str(Target_pitch[target_pitch_selected])
targets = user_input(str(Target_pitch[target_pitch_selected]))


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_INSTRU_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_T_P_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTON_INSTRU_GPIO, GPIO.FALLING, 
    callback=instrument_pressed_callback, bouncetime=150)
GPIO.add_event_detect(BUTTON_T_P_GPIO, GPIO.FALLING, 
    callback=target_pitch_callback, bouncetime=150)
signal.signal(signal.SIGINT, interrupt.signal_handler)
#signal.pause()

try:

	while (True):
		#GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING,callback=instrument_pressed_callback, bouncetime=100)
		signal.signal(signal.SIGINT, interrupt.signal_handler)
		pitch,target_pitch,target_str,isittuned,correction_value=pitch_estimate.pitch(targets)
		LCD.lcd_init()

		LCD.lcd_send_byte(LCD_LINE_1, LCD_CMD)
		print(instruments[instrument_selected]+"  "+str(pitch)+" "+str(Target_pitch[target_pitch_selected]))
		LCD.lcd_message(instruments[instrument_selected]+"  "+str(pitch)+" "+str(Target_pitch[target_pitch_selected]))
		LCD.lcd_send_byte(LCD_LINE_2, LCD_CMD)
		#LCD.lcd_send_byte(0x07, LCD_CMD)
		#LCD.lcd_string("target_pitch"+(" "*5)+"pitch",1)
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
except KeyboardInterrupt:
	LCD.lcd_send_byte(LCD_LINE_1, LCD_CMD)
	
	LCD.lcd_message(" "*16)
	LCD.lcd_send_byte(LCD_LINE_2, LCD_CMD)
	LCD.lcd_message(" "*16)
	GPIO.cleanup()
finally:
    GPIO.cleanup()