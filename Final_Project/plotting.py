#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:26:18 2020

@author: manojjagannath
"""
import matplotlib.pyplot as plt

def plotting(x=None, y=None, xlabel="x axis", ylabel="y axis", grid=False):
    if(y == None):
        y = x
        plt.plot(y)
        plt.ylabel(ylabel)
        plt.grid(grid)
        plt.show()
        
    else:
        plt.plot(x,y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(grid)
        plt.show()
        
   