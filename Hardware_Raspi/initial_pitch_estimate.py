#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:48:31 2020

@author: manojjagannath
"""
import numpy as np

def initial_pitch_estimate(data,user_input=0):
# A rough estimate of pitch to determine the mean range of the pitch contour
    
    pitch_estimate = np.mean(data)
    
    threshold_low = 50
    threshold_high = 425
    
    if(pitch_estimate>threshold_high):
            threshold_high = pitch_estimate + 2
    if(pitch_estimate <= threshold_low):
            threshold_low = pitch_estimate - 2
            
    return threshold_low, threshold_high

    # if(user_input == 'a'):
        
    #     threshold_low = 53
    #     threshold_high = 230
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2
           
    # elif(user_input == 'b'):
        
    #     threshold_low = 56
    #     threshold_high = 243
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2
           
    # elif(user_input == 'b#'):
        
    #     threshold_low = 59
    #     threshold_high = 256
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2
           
    # elif(user_input == 'c'):
        
    #     threshold_low = 63
    #     threshold_high = 271
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2

    # elif(user_input == 'c#'):
        
    #     threshold_low = 67
    #     threshold_high = 287
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2
           
    # elif(user_input == 'd'):
        
    #     threshold_low = 73
    #     threshold_high = 303
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2
           
    # elif(user_input == 'd#'):
        
    #     threshold_low = 75
    #     threshold_high = 321
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2

    # elif(user_input == 'e'):
        
    #     threshold_low = 80
    #     threshold_high = 340
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2
           
    # elif(user_input == 'f'):
        
    #     threshold_low = 85
    #     threshold_high = 360
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2
           
    # elif(user_input == 'f#'):
        
    #     threshold_low = 90
    #     threshold_high = 380
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2
           
    # elif(user_input == 'g'):
        
    #     threshold_low = 96
    #     threshold_high = 402
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2
           
    # elif(user_input == 'g#'):
        
    #     threshold_low = 102
    #     threshold_high = 425
    
    #     if(pitch_estimate>threshold_high):
    #         threshold_high = pitch_estimate + 5
    #     if(pitch_estimate <= threshold_low):
    #        threshold_low = pitch_estimate - 2