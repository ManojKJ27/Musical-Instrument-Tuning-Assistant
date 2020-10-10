#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:38:52 2020

@author: manojjagannath
"""
import numpy as np
# import pandas as pd

def movmean(y,ws):
    y_mean_list = []
    # y_series = pd.Series(y)
    # windows = y_series.rolling(ws)
    # y_mean = windows.mean()
    # y_mean_list = y_mean.tolist()
    
    start = 0; end = start + ws;
    while(end<=len(y)):
        y_mean_list.append(np.mean(y[start:end]))
        start = end + 1
        end = start + ws
        
    return y_mean_list

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
