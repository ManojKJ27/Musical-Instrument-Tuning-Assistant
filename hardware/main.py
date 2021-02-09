#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:12:17 2020

@author: manojjagannath
"""
# import time
# import temp
import pitch_estimate
from user_input import user_input
values="A"
#event, values = window.read()
targets = user_input(values)
i = 1
while (i):
    # tick = time() 
    # temp.pitch()
    
    pitch,target_pitch,target_str,isittuned,correction_value=pitch_estimate.pitch(targets)
    print("target_pitch: "+target_pitch)
    # time.sleep(1)
    # tock = time() # Stop clock
    # print("Execution time : ",tock-tick)
    # i = i+1