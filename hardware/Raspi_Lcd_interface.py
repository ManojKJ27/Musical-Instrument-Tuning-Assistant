# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:18:24 2021

@author: abhin
"""
import RPi.GPIO as GPIO
import time
def init_raspi_LCD(self):
    
    
    
    #should be changed according to the connection of hardware
    self.LCD_rs=1
    self.LCD_e=2
    self.LCD_D4 =3
    self.LCD_D5 =4
    self.LCD_D6 =5
    self.LCD_D7 =6
    
    self.LCD_Width = 16 #length of each line in lcd
    self.LCD_CHR = True
    self.LCD_CMD = False
    self.LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
    self.LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
    self.E_PULSE = 0.0005
    self.E_DELAY = 0.0005

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(self.LCD_e, GPIO.OUT)  # E
    GPIO.setup(self.LCD_rs, GPIO.OUT) # RS
    GPIO.setup(self.LCD_D4, GPIO.OUT) # DB4
    GPIO.setup(self.LCD_D5, GPIO.OUT) # DB5
    GPIO.setup(self.LCD_D6, GPIO.OUT) # DB6
    GPIO.setup(self.LCD_D7, GPIO.OUT) # DB7
    lcd_init(self)
    
def lcd_init(self):
  lcd_display(0x28,self.LCD_CMD) # Selecting 4 - bit mode with two rows
  lcd_display(0x0C,self.LCD_CMD) # Display On,Cursor Off, Blink Off
  lcd_display(0x01,self.LCD_CMD) # Clear display

 
def lcd_display(self,bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(self.LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(self.LCD_D4, False)
  GPIO.output(self.LCD_D5, False)
  GPIO.output(self.LCD_D6, False)
  GPIO.output(self.LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(self.LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(self.LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(self.LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(self.LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(self.LCD_D4, False)
  GPIO.output(self.LCD_D5, False)
  GPIO.output(self.LCD_D6, False)
  GPIO.output(self.LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(self.LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(self.LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(self.LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(self.LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable(self):
  # Toggle enable
  
  GPIO.output(self.LCD_e, True)
  time.sleep(self.E_PULSE)
  GPIO.output(self.LCD_e, False)
  time.sleep(self.E_DELAY)
 
def lcd_string(self,message,line):
  # Send string to display
 
  message = message.ljust(self.LCD_WIDTH," ")
 
  lcd_display(line, self.LCD_CMD)
 
  for i in range(self.LCD_WIDTH):
    lcd_display(ord(message[i]),self.LCD_CHR)
 