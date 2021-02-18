#!/usr/bin/env python3
import signal
import sys
import RPi.GPIO as GPIO
BUTTON_GPIO = 16
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
def mode_pressed_callback(channel):
    print("mode changed")
def instrument_pressed_callback(channel):
	print("instrument changed")