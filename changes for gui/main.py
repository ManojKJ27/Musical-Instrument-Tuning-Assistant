#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:12:17 2020
          [sg.Text(size=(40,1), key='-OUTPUT1-')],
          [sg.Text(size=(40,1), key='-OUTPUT2-')],
          [sg.Text(size=(40,1), key='-OUTPUT3-')],
          [sg.Text(size=(40,1), key='-OUTPUT4-')],
@author: manojjagannath
"""
# import time
# import temp
import pitch_estimate
from user_input import user_input
import PySimpleGUI as sg
#from correction import closest_distance,Sa_error,Pa_error,Sah_error
layout1 = [[sg.Text("Enter target Pitch")],
          [sg.Input(key='-INPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]
layout2=[[sg.Text(size=(40,1), key='-OUTPUT1-')],
          [sg.Text(size=(40,1), key='-OUTPUT2-')],
          [sg.Text(size=(40,1), key='-OUTPUT3-')],
          [sg.Text(size=(40,1), key='-OUTPUT4-')],
          [sg.Button('OK')]]
# Create the window
window1 = sg.Window('Pitch detection', layout1)
event, values = window1.read()
inp=values['-INPUT-']
targets = user_input(values)
window1.close()
window2=sg.Window('pitch output',layout2)#,finalize=True)
#event, values = window.read()
#targets = user_input(values)
i = 1
while (i):
    # tick = time() 
    # temp.pitch()
    event, values = window2.read()
    pitch,String,String_in=pitch_estimate.pitch(targets)
    window2['-OUTPUT1-'].update("Target pitch :" + inp)
    if (pitch!=0):
        window2['-OUTPUT2-'].update("Pitch:"+str(pitch))
    window2['-OUTPUT3-'].update(String)
    window2['-OUTPUT4-'].update(String_in )#+ "\n"+String+"\n"+String_in)
    # time.sleep(1)
    # tock = time() # Stop clock
    # print("Execution time : ",tock-tick)
    # i = i+1