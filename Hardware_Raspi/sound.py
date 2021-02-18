# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:46:51 2020

@author: abhin
"""

import PySimpleGUI as sg
import pygame

class Music:

    def __init__(self, file):
        self.sound = file

    def play(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

        pygame.init()
        
        pygame.mixer.init()
        
        pygame.mixer.music.load('song1.mp3')
        
        pygame.mixer.music.play(-1)
        
    def volchange(volume):
        pygame.mixer.music.set_volume(volume)  # The set_volume range is from 0.00 to 1.00 (every 0.01)

    def isplaying():
        return pygame.mixer.music.get_busy()

layout = [
    [sg.Button('Play'),sg.Button('stop'), 
     sg.Slider(key = 'volume', range=(0, 100), 
     orientation='h', size=(10, 15), default_value= 100)]
]

window = sg.Window('Help me', layout)

while True:
    event, values = window.read()
    if event == 'Play':
        path = "song1.mp3"
        music = Music(path)
        music.play()
    if Music.isplaying():
        Music.volchange(float(values['volume'] / 100))
    if event=='stop':
        pygame.mixer.music.stop()