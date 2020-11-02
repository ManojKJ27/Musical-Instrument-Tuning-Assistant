#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:38:52 2020

@author: manojjagannath
"""
import numpy as np
from movmean import movmean
from plotting import plotting

def denoise(y,ws,threshold_low=0,threshold_high=0):
# Find the moving average of the data and filter according to the threshold
# Restricting the bandwidth of the pitch contour based on the initial pitch estimate

    denoise_list = []
    
    if(len(y)>1):
        y_mean = movmean(y,ws) # Moving average of pitch contour
        y_mean = list(filter(lambda x: x!=0, y_mean))
        
        plotting(y_mean)
        
        initial_pitch_estimate = np.mean(y_mean)
        
        threshold_low = initial_pitch_estimate - 50
        threshold_high = initial_pitch_estimate + 50
                    
        for i in range(0,len(y_mean)):
            if (np.abs(y_mean[i]) <= threshold_high):
                if (np.abs(y_mean[i]) >= threshold_low):
                    denoise_list.append(y_mean[i])
                
    denoise_list = list(filter(lambda x: x!=0, denoise_list)) # Remove zeros from the list


    return denoise_list, initial_pitch_estimate
