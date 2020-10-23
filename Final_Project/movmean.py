#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:19:02 2020

@author: manojjagannath
"""
import numpy as np
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