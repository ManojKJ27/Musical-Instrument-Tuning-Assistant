#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:19:02 2020

@author: manojjagannath
"""
import numpy as np
def movmean(y,ws):
    # Find the Moving average of the pitch contour
    
    y_mean_list = []
    start = 0; end = start + ws; # Set window parameters
    while(end<=len(y)):
        y_mean_list.append(np.mean(y[start:end]))
        start = end + 1
        end = start + ws
        
    return y_mean_list