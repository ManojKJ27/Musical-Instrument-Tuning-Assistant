#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:13:03 2020

@author: manojjagannath
"""
def movdiff(y_mean_list):
    # Find the Forward difference of the averaged pitch contour
    
    diff = y_mean_list  
    maxima = 0
    for i in range(len(y_mean_list)-1):
        difference = y_mean_list[i+1]-y_mean_list[i] 
        if(abs(difference) > 2):
            maxima += 1
            if(maxima>1):
                diff[i+1] = diff[i]
            
    return diff
