#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:27:45 2020

@author: manojjagannath
"""

import matplotlib.pyplot as plt
from denoise import denoise
from collections import Counter
from record import record
from numpy import abs as npabs, floor
from correction import correction
from scipy.signal import butter, sosfilt
from pitch_contour import pitch_contour
from plotting import plotting


def pitch(targets):
    
    """ Audio I/O """
    fs, data = record(2) # Read audio from the microphone for 2 seconds
    
    """ Digital Highpass filter at 40Hz """
    sos = butter(10, 40/fs, 'hp',output = 'sos')
    data = sosfilt(sos,data)
    
    """ Energy of the audio signal recorded """
    energy = sum(npabs(data)**2)
    
    if (energy > 1e-1): # Check if signal is prominent; to avoid processing silence
    
        """ Pitch contour generation """
        contour = pitch_contour('recorded.wav')
        
        """ Denoising """
        result, init_pitch = denoise(contour,1) # Remove the unwanted portions from the pitch contour
        
        # Plot the pitch contour
        plotting(result, ylabel = "fundamental frequency [Hz]")
        
        result = floor(result)
    
        """ Histogram """
        cnt = Counter(result) # Output is a dictionary of frequency(Hz) : number of occurences
        keys = list(cnt.keys())
        values = list(cnt.values())
        
        # Plot the Histogram
        plt.bar(keys,values)
        plt.show()
        
        if(len(values) and max(values)>1): # Check for empty list and prominenence of frequency signature
            pitch_freq = keys[values.index(max(values))] # Select the most frequent Hz value
            
            print("Pitch : ",pitch_freq," Hz")
            # print("Number of occurences : ",max(values))  
            print("Initial_estimte : ",init_pitch)
            print("Difference : ", npabs(pitch_freq - init_pitch))
            
            correction(pitch_freq,targets)
            print()
            
        else :
            print()
            
        


