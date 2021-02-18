#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:40:15 2020

@author: manojjagannath
"""

def user_input(values):
# Take input from user 
# Build the corresponding set of major frequencies
    
    target_pitch = 0
    base_pitch_list = [55,58,61,65,69,73,77,82,87,92,98,104];
    shruthi_name = ["A","B","B#","C","C#","D","D#","E","F","F#","G","G#"] ; 
    
    target_pitch_class = values
    #target_pitch_class = input("Enter the target pitch : ")
    for i in range(len(shruthi_name)):
        if(target_pitch_class.upper() == shruthi_name[i]):
            target_pitch = base_pitch_list[i]
            
    if(target_pitch == 0):
        print("Wrong input, terminating program")
        exit()
        
    target_set = [target_pitch,target_pitch*3/2,target_pitch*2,
                  target_pitch*3,target_pitch*4,
                  target_pitch*6, target_pitch*8]
    
    print("Target frequencies : ",target_set)
    
    return target_set