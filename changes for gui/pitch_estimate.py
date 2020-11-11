#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:27:45 2020

@author: manojjagannath
"""
import parselmouth
from denoise import denoise
from scipy.io import wavfile as wv
from collections import Counter
from record import record
from numpy import abs as npabs, round as npround, floor
from correction import correction
import PySimpleGUI as sg
#from main import window
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
    
    record(1) # Record audio from the microphone for 2 seconds and store it as 'recorded.wav'
    fs, data = wv.read('recorded.wav') # Read the recorded audio
    audio = parselmouth.Sound("recorded.wav") # Convert it to a Parselmouth.Sound object for pitch estimation
    rms = sqrt(mean(data**2))# Strength of audio signal recorded
    String=" "
    String_in= " "
    pitchf=0
    if (rms >= 1e3): # Check if signal is prominent; to avoid processing silence
        pitch = audio.to_pitch()

        # Reset output variables to enable continuos processing
        output = 0
        result = 0
        output = draw_pitch(pitch) # Get the pitch contour

        result, init_pitch = denoise(output,1) # Remove the unwanted portions from the pitch contour
        
        result = npround(result) # Limit precission for histogram analysis
    
        cnt = Counter(result) # Histogram; ouput is a dictionary of frequency(Hz) and number of occurences
        keys = list(cnt.keys()) # Convert dictionary to lists
        values = list(cnt.values()) 
            
        if(len(values) and max(values)>1): # Check for empty list and prominenence of frequency signature
            pitch_freq = keys[values.index(max(values))]
            print("Pitch : ",pitch_freq," Hz")
            # print("Number of occurences : ",max(values))  
            # print("Initial_estimte : ",init_pitch)
            # print("Difference : ", npabs(pitch_freq - init_pitch))
            String,String_in=correction(pitch_freq,targets)
            pitchf=pitch_freq
    # Output a message to the window
            #return pitch,String,String_in
            #window['-OUTPUT-'].update("Target pitch :" + values['-INPUT-'] + "\n"+String+"\n"+String_in)
            print()
        else :
            print()
    return pitchf,String,String_in
    
