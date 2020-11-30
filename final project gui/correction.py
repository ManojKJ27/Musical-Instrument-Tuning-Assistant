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
    correctitby=0

    tuned=False
    
    if(closest_distance == npabs(Sa_error)):
        print("Target is Sa : ",target," Hz")
        target_pitch=target
        pitch_str="Sa"
        if(abs(Sa_error)<2):
            print("Sa : tuned at ",target,"Hz")
            tuned=True
        else:
            tuned=False
            correctitby=Sa_error
            """
            if(Sa_error>0):
                print("Sa : Increase by ",Sa_error," Hz")
                strint_in="Sa : Increase by "+str(Sa_error)+"Hz"
                tuned=
            else:
                print("Sa : Decrease by ",Sa_error," Hz")
                strint_in="Sa : Decrease by "+str(Sa_error)+"Hz"
                correctitby=Sa_error"""
            
    if(closest_distance == npabs(Pa_error)):
        print("Target is Pa : ",target*3/2," Hz")
        target_pitch=target*3/2
        pitch_str="Pa"
        if(abs(Pa_error)<2):
            print("Pa : tuned at ",target*3/2,"Hz")
            #strint_in="Pa : tuned at "+str(target*3/2)+"Hz"
            tuned=True
        else:
            tuned=False
            correctitby=Pa_error
            """
            if(Pa_error>0):
                print("Pa : Increase by ",Pa_error," Hz")
                strint_in="Pa : Decrease by "+str(Pa_error)+"Hz"
                correctitby=Pa_error
            else:
                print("Pa : Decrease by ",Pa_error," Hz")
                strint_in="Pa : Increase by "+str(Pa_error)+"Hz"
                correctitby=Pa_error"""
            
    if(closest_distance == npabs(Sah_error)):
        print("Target is Sah : ",target*2," Hz")
        target_pitch=target*2
        pitch_str="Sah"
        if(abs(Sah_error)<2):
            print("Sah : tuned at ",target*2,"Hz")
            #strint_in="Sah : tuned at "+str(target*2)+"Hz"
            tuned=True
        else:
            tuned=False
            correctitby=Sah_error
            """
            if(Sah_error>0):
                print("Sah : Increase by ",Sah_error," Hz")
                strint_in="Sah : Increase by "+str(Sah_error)+"Hz"
                correctitby=Sah_error
            else:
                print("Sah : Decrease by ",Sah_error," Hz")
                strint_in="Sah : Decrease by "+str(Sah_error)+"Hz"
                correctitby=Sah_error"""
                
    return target_pitch,pitch_str,tuned,correctitby