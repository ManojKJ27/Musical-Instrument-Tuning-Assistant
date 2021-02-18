# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:31:51 2020

@author: abhin
"""

import pygame,mutagen.mp3

song_file = "D:/s/final project/Musical-Instrument-Tuning-Assistant-Python-Codes/Musical-Instrument-Tuning-Assistant-Python-Codes/Final_Project/songa.mp3"

mp3 = mutagen.mp3.MP3(song_file)
print(mp3.info.sample_rate)
pygame.mixer.init(size=8)

pygame.mixer.music.load(song_file)
pygame.mixer.music.play()