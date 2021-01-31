# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:06:35 2021

@author: abhin
"""

import RPi.GPIO as GPIO

Toggle_Mode_Switch=10#Sholud be updates accor to hardware
Device_Mode=False
def button_pressed_callback(channel):
    global Device_Mode
    Device_Mode!=Device_Mode
    
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(Toggle_Mode_Switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(Toggle_Mode_Switch, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)