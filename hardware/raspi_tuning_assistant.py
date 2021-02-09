# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:56:52 2021

@author: abhin
"""


import pitch_estimate
from user_input import user_input
from musicplot import Music as dt
import Raspi_Lcd_interface as LCD
import RPi.GPIO as GPIO
def button_pressed_callback(channel):
    global digital_tanpura_selection
    digital_tanpura_selection!=digital_tanpura_selection
    
LCD.init_raspi_LCD();
Toggle_Mode_Switch=10 #Sholud be updates accor to hardware
instrument_names=["Veena","Violin","Flute"];
shruthi_name = ["A","B","B#","C","C#","D","D#","E","F","F#","G","G#"] ;
shruthi_selection=0;
instrument_selection=0;
targets=user_input(shruthi_name[shruthi_selection])
#event1,values1=window1.read(timeout=1)
digital_tanpura_selection=False;
GPIO.setmode(GPIO.BCM)
    
GPIO.setup(Toggle_Mode_Switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(Toggle_Mode_Switch, GPIO.FALLING,callback=button_pressed_callback, bouncetime=200)

if (digital_tanpura_selection):
    
    digitalT=dt(instrument_names[instrument_selection])
    digitalT.sound()
else:
            pitch,target_pitch,target_str,isittuned,correction_value=pitch_estimate.pitch(targets)
            LCD.lcd_string("target_pitch"+(" "*5)+"pitch",1)
            if (correction_value<0):    #target is less then pitch(correction_value=target-pitch)
                if (abs(correction_value)<10):
                    LCD.lcd_string("slight Decrease in Pitch needed",2)
                else:
                    LCD.lcd_string("high Decrease in Pitch needed",2)   
            elif (correction_value==0):
                
                LCD.lcd_string("Correct Pitch",2)
            else:
                
                if (abs(correction_value)<10):
                    LCD.lcd_string("slight Increase in Pitch Needed",2)
                else:
                    LCD.lcd_string("high Increase in Pitch Needed",2)
    
        
        
