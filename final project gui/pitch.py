# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:22:40 2020

@author: abhin
"""

import pitch_estimate
from user_input import user_input
import PySimpleGUI as sg

layout1 = [[sg.Text("Enter target Pitch")],
          [sg.Combo(["A","B","B#","C","C#","D","D#","E","F","F#","G","G#"], size=(20, 3), enable_events=True, key='combo')],
          [sg.Button('Ok'), sg.Quit()]]

layout2=[[sg.Text(size=(40,1),font="Courier", key='-OUTPUT1-')],
          [sg.Text(size=(40,1),font="Courier", key='-OUTPUT2-')],
          [sg.Text(size=(40,1),font="Courier", key='-OUTPUT3-')],
          [sg.Text(size=(40,1),font="Courier", key='-OUTPUT4-')],
          [sg.Text(size=(20,1),font="Courier", key='-OUTPUT5-'),sg.ProgressBar(50, orientation='h',size=(20, 20),bar_color=("white","blue"),  key='progressbar1'),sg.ProgressBar(50, orientation='h',size=(20, 20),bar_color=("blue","white"),  key='progressbar2'),sg.Text(size=(40,1),font="Courier", key='-OUTPUT6-')],
          [sg.Text(" "*50,size=(29,1)),sg.Text("|"+" "*52+"|"+" "*14+"|"+" "*11+"|"+" "*52+"|",justification='center')],
          [sg.Text(" "*200,size=(30,1)),sg.Text("Low"+" "*23+" "+" "*25+"High",font="Courier",justification='center')],
          [sg.Button('Resume/Pause'),sg.Button('Quit')]]
window2=sg.Window('Pitch Analysis',layout2,no_titlebar=True)
progress_bar1 = window2['progressbar1']
progress_bar2 = window2['progressbar2']
window1=sg.Window('Pitch Detection',layout1)
event1,values1=window1.read()
received_input=values1['combo']
targets=user_input(values1)
window1.close()

show_pitch,isittuned=True,False
while(1):
    event2,values2=window2.read(timeout=2)
    if event2 in (None,'Quit'):
            break
    elif (event2=='Resume/Pause'):
        show_pitch=not show_pitch
    if show_pitch:
        pitch,target_pitch,target_str,isittuned,correction_value=pitch_estimate.pitch(targets)
        if(target_pitch==0):
            pass
        
        elif(pitch==0):
                 window2['-OUTPUT1-'].update('target pitch from user:'+received_input)
                 window2['-OUTPUT2-'].update('detecting scilence')
                 window2['-OUTPUT3-'].update(' ')
                 window2['-OUTPUT4-'].update(' ')
                 window2['-OUTPUT5-'].update("Error")
                 progress_bar1.UpdateBar(50+correction_value)
                 progress_bar2.UpdateBar(correction_value)
                 window2['-OUTPUT6-'].update("Correct Pitch")
        
        else:
            window2['-OUTPUT1-'].update('target pitch from user:'+received_input)
            window2['-OUTPUT2-'].update('Pitch of ur instrument :'+str(pitch))
            window2['-OUTPUT3-'].update('Target is'+target_str+' '+str(target_pitch))
            if (isittuned):
                window2['-OUTPUT4-'].update('Playing at correct Pitch')
            else:
                window2['-OUTPUT4-'].update('Correct the Pitch by'+"  "+str(correction_value))
            window2['-OUTPUT5-'].update("Error")
            if (correction_value<0):
                progress_bar1.UpdateBar(50)
                progress_bar2.UpdateBar(abs(correction_value))
                if (abs(correction_value)<10):
                    window2['-OUTPUT6-'].update("slight Increase in Pitch")
                else:
                    window2['-OUTPUT6-'].update("high Increase in Pitch")   
            elif (correction_value==0):
                progress_bar1.UpdateBar(50)
                progress_bar2.UpdateBar(0)
                window2['-OUTPUT6-'].update("Correct Pitch")
            else:
                progress_bar1.UpdateBar(50-correction_value)
                progress_bar2.UpdateBar(0)
                if (abs(correction_value)<10):
                    window2['-OUTPUT6-'].update("slight Decrease in Pitch")
                else:
                    window2['-OUTPUT6-'].update("high Decrease in Pitch")  
window2.close()