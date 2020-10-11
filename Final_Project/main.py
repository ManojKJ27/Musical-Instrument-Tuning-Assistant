#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:12:17 2020

@author: manojjagannath
"""
from time import time
import temp
i = 0
while (i<2):
    tick = time() 
    temp.pitch()
    tock = time() # Stop clock
    print("Execution time : ",tock-tick)
    i = i+1