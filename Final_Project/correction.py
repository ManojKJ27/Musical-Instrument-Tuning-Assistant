#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:23:05 2020

@author: manojjagannath
"""
from numpy import floor
from numpy import abs as npabs

def correction(pitch,targets):
# Find the errors, 
# Determine the closest note frequency 
# Display the corrective action required
    
    if(floor(pitch<targets[2])):
        target = targets[0]
    else:
        target = targets[2]
        
    # print("Target_base : ",target)
    
    Sa_error = target - pitch 
    Pa_error = target*3/2 - pitch
    Sah_error = target*2 - pitch
    
    closest_distance = min(npabs(Sa_error),npabs(Pa_error),npabs(Sah_error))
    
    if(closest_distance == npabs(Sa_error)):
        print("Target is Sa : ",target," Hz")
        
        if(abs(Sa_error)<2):
            print("Sa : tuned at ",target,"Hz")
        else:
            if(Sa_error>0):
                print("Sa : Increase by ",Sa_error," Hz")
            else:
                print("Sa : Decrease by ",Sa_error," Hz")
            
    if(closest_distance == npabs(Pa_error)):
        print("Target is Pa : ",target*3/2," Hz")
        
        if(abs(Pa_error)<2):
            print("Pa : tuned at ",target*3/2,"Hz")
        else:
            if(Pa_error>0):
                print("Pa : Increase by ",Pa_error," Hz")
            else:
                print("Pa : Decrease by ",Pa_error," Hz")
            
    if(closest_distance == npabs(Sah_error)):
        print("Target is Sa : ",target*2," Hz")
        
        if(abs(Sah_error)<2):
            print("Sa : tuned at ",target*2,"Hz")
        else:
            if(Sah_error>0):
                print("Sa : Increase by ",Sah_error," Hz")
            else:
                print("Sa : Decrease by ",Sah_error," Hz")