#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:27:45 2020

@author: manojjagannath
"""
import parselmouth
# import matplotlib.pyplot as plt
from denoise import denoise
from scipy.io import wavfile as wv
from collections import Counter
from math import floor
from record import record
from numpy import mean
from numpy import abs as npabs


# audio = parselmouth.Sound("/Users/manojjagannath/Desktop/PROJECT2/Veena/Sa_E.wav")

def pitch():
    def draw_pitch(pitch):
    # Extract selected pitch contour

            pitch_values = pitch.selected_array['frequency']
        
    # Plot the pitch contour
        # plt.plot(pitch.xs(), pitch_values)#, 'o', markersize=2)
        # plt.grid(False)
        # plt.ylim(0, pitch.ceiling)
        # plt.ylabel("fundamental frequency [Hz]")
        # plt.show()
        
            return pitch_values
        
    record(2) # Record audio from the microphone for 2 seconds and store it as 'recorded.wav'
    fs, data = wv.read('recorded.wav') # Read the recorded audio
    audio = parselmouth.Sound("recorded.wav") #Convert it to a Parselmouth.Sound object for pitch estimation

    if (mean(npabs(audio.values.T))>1e-5): # Check if signal is prominent; to avoid processing silence
        pitch = audio.to_pitch()

        # Reset output variables to enable continuos processing
        output = 0
        result = 0
        output = draw_pitch(pitch) # Get the pitch contour

        result = denoise(output,1,20,520) # Remove the unwanted portions from the pitch contour
        for i in range(0,len(result)) : 
                result[i] = floor(result[i]) # Limit precission for histogram analysis
    
        cnt = Counter(result) # Histogram; ouput is a dictionary of frequency(Hz) and number of occurences
        keys = []
        values = []
        for key in cnt : # Convert dictionary to lists
            keys.append(key)
            values.append(cnt[key])
            
        if(len(values) and max(values)>1): # Check for empty list and prominenence of frequency signature
            pitch_count = keys[values.index(max(values))]
            print("Pitch : ",pitch_count)
        else :
            print()


