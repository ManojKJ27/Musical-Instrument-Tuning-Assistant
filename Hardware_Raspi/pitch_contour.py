#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 08:50:24 2020

@author: manojjagannath
"""
import parselmouth
from plotting import plotting

def pitch_contour(wav_file = "recorded.wav"):
    def draw_pitch(pitch):
        # Extract selected pitch contour

            pitch_values = pitch.selected_array['frequency']
        
        # Plot the pitch contour
            #plotting(pitch_values,ylabel="fundamental frequency [Hz]")
        
            return pitch_values
        
    audio = parselmouth.Sound(wav_file) # Convert it to a Parselmouth.Sound object for pitch estimation
    pitch = audio.to_pitch()

    # Reset output variable
    contour = 0
    # Get the pitch contour
    contour = draw_pitch(pitch) 
    
    return contour