# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:04:48 2020

@author: abhin
"""
import wave
def speed(path,speedrate):
    CHANNELS = 1
    swidth = 2
    
    spf = wave.open(path, 'rb')
    #RATE=spf.getframerate()
    signal = spf.readframes(-1)
    
    wf = wave.open('changed.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(swidth)
    wf.setframerate(speedrate)
    wf.writeframes(signal)
    wf.close()