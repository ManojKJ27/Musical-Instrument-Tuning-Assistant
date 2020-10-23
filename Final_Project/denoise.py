#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:38:52 2020

@author: manojjagannath
"""
import numpy as np
from movmean import movmean
# import pandas as pd

def denoise(y,ws,threshold_low,threshold_high):
# Find the moving average of the data and filter according to the threshold. 

    denoise_list = []

    if(len(y)>1):
        y_mean = movmean(y,ws);
        for i in range(0,len(y_mean)):
            if (np.abs(y_mean[i]) <= threshold_high):
                if (np.abs(y_mean[i]) >= threshold_low):
                    denoise_list.append(y_mean[i])
                
    denoise_list = list(filter(lambda x: x!=0, denoise_list)) 


    # if (np.abs(y)>=threshold_low and np.abs(y)<=threshold_high) :
    #     denoise_list = y 
    # else:
    #     denoise_list = 0
    
    return denoise_list
