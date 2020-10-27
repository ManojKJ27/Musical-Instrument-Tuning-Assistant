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
# from numpy import mean,fft,conj,array,correlate
from numpy import abs as npabs
# from pitch_by_xcorr import pitch_by_xcorr
# import librosa
from correction import correction
# from user_input import user_input

# audio = parselmouth.Sound("/Users/manojjagannath/Desktop/PROJECT2/Veena/Sa_E.wav")

def pitch(targets):
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
    
    # targets = user_input()
    
    record(1) # Record audio from the microphone for 2 seconds and store it as 'recorded.wav'
    fs, data = wv.read('recorded.wav') # Read the recorded audio
    audio = parselmouth.Sound("recorded.wav") # Convert it to a Parselmouth.Sound object for pitch estimation
    energy = sum(npabs(audio.values.T)**2) # Energy of audio signal recorded
    # plt.plot(audio.values.T)
    # plt.show()
    # estimate = pitch_by_xcorr(data)
    # print("Xcorr : ",estimate)
    

    if (energy > 1e-1): # Check if signal is prominent; to avoid processing silence
        pitch = audio.to_pitch()

        # Reset output variables to enable continuos processing
        output = 0
        result = 0
        output = draw_pitch(pitch) # Get the pitch contour

        result, init_pitch = denoise(output,1) # Remove the unwanted portions from the pitch contour
        
        for i in range(0,len(result)) : 
                result[i] = floor(result[i]) # Limit precission for histogram analysis
    
        cnt = Counter(result) # Histogram; ouput is a dictionary of frequency(Hz) and number of occurences
        keys = []
        values = []
        for key in cnt : # Convert dictionary to lists
            keys.append(key)
            values.append(cnt[key])
            
        if(len(values) and max(values)>1): # Check for empty list and prominenence of frequency signature
            pitch_freq = keys[values.index(max(values))]
            print("Pitch : ",pitch_freq," Hz")
            # print("Number of occurences : ",max(values))  
            # print("Initial_estimte : ",init_pitch)
            # print("Difference : ", npabs(pitch_freq - init_pitch))
            correction(pitch_freq,targets)
            print()
        else :
            print()
            
        


