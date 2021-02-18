#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 14:28:49 2020

@author: manojjagannath
"""
from movmean import movmean
def denoise_classic(y,ws,threshold):
 # Find the moving average of the data and filter according to the threshold. 
    denoise_classic = [0] * len(y)
    y_mean = movmean(y,ws);
 # threshold = 0.5*1e-6;
    for i in range(len(y_mean)): 
         if (abs(y_mean[i]) > threshold):
             denoise_classic[i] = y_mean[i]
    return denoise_classic