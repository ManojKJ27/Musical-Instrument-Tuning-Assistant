# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:04:48 2020

@author: abhin
Inputs : Audio file, speed factor (1 - original, 2 - 2x, 0.5 - 0.5x, etc)
Output : Modified audiofile saved as wav (Best if changed to playback without saving)
"""
import librosa
import soundfile as sf

def speed(path,speedrate):
    filename = path
    
    # Modify speed
    y, sr = librosa.load(filename)
    speed = speedrate # always non-zero
    y_fast = librosa.effects.time_stretch(y, speed)
    
    # Write out audio as 24bit PCM WAV
    rate = sr
    sf.write('changed.wav', y_fast, int(rate/1))
    