# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:22:40 2020

@author: abhin
"""

import pitch_estimate
from user_input import user_input
import PySimpleGUI as sg
from musicplot import Music as dt

#container.style['background-image'] = "url('/my_resources:logo.png')"
sg.theme('TealMono')
layout1 = [[sg.Image("timber.png")],
    [sg.Radio('Digital Tanpura','num',size=(13,2),font="Helvitica",key='option1'),sg.Radio('Pitch Detection','num',size=(15,2),font="Helvitica",key='option2'),sg.Text("Enter target Pitch",justification="right",size=(31,1))
          ,sg.Combo(["A","B","B#","C","C#","D","D#","E","F","F#","G","G#"], size=(20, 3), enable_events=True, key='combo')],
          [sg.Text("PITCH ANALYSIS",size=(73,1),font="Helvitica",justification="center")],
          [sg.Text(size=(40,1),font="Courier", key='-OUTPUT1-')],
          [sg.Text(size=(25,1),font="Courier", key='-OUTPUT2-'),sg.Text(size=(7,1),font="Courier",text_color="blue", key='-OUTPUT4-')],
#          [sg.Text(size=(40,1),font="Courier", key='-OUTPUT4-')],
          [sg.Text("Error",size=(7,1),font="Courier", key='-OUTPUT5-'),sg.ProgressBar(50, orientation='h',size=(20, 20),bar_color=("white","blue"),  key='progressbar1'),sg.ProgressBar(50, orientation='h',size=(20, 20),bar_color=("blue","white"),  key='progressbar2')],
          [sg.Text(size=(40,1),font="Courier", key='-OUTPUT6-',justification="right")],
          #[sg.Text(" "*50,size=(29,1)),sg.Text("|"+" "*52+"|"+" "*14+"|"+" "*11+"|"+" "*52+"|",justification='center')],
          #[sg.Text(" "*200,size=(30,1)),sg.Text("Low"+" "*23+" "+" "*25+"High",font="Courier",justification='center')],
          [sg.Text(size=(30,1)),sg.Button('Ok'),sg.Button('Resume/Pause'),sg.Button('stop'), sg.Quit(),
          sg.Text(size=(25,1),font="Courier",justification="right", key='-OUTPUT3-')]]

window1=sg.Window('Pitch Detection',layout1)
event1,values1=window1.read()
received_input=values1['combo']
if event1 in ('WIN_CLOSED','Quit','exit',None):
        window1.close()
        
targets=user_input(values1)
#window2=sg.Window('Pitch Analysis',layout2)
progress_bar1 = window1['progressbar1']
progress_bar2 = window1['progressbar2']

show_pitch,isittuned=True,False
#digitalT=dt(received_input)
while(1):
    #event1,values1=window1.read(timeout=1)
    if event1 in ('WIN_CLOSED','Quit','exit'):
        window1.close()
        break
    if (values1['option1']):
        
        digitalT=dt(values1['combo'])
        digitalT.sound()
        event1,values1=window1.read()
    elif(values1['option2']):
        window1['-OUTPUT3-'].update('Play',text_color="green")
        while(1):
            sg.theme('LightGreen7')
            event1,values1=window1.read(timeout=1)
            if event1 in ('stop','WIN_CLOSED'):
                    break
            elif (event1=='Resume/Pause'):
                window1['-OUTPUT3-'].update('Pause',text_color="yellow")
                show_pitch=not show_pitch
            if show_pitch:
                window1['-OUTPUT3-'].update('Play',text_color="green")
                pitch,target_pitch,target_str,isittuned,correction_value=pitch_estimate.pitch(targets)
                if(target_pitch==0):
                    pass
                
                elif(pitch==0):
                         window1['-OUTPUT1-'].update('target pitch from user:'+" "*5+values1['combo'])
                         window1['-OUTPUT2-'].update('detecting scilence')
                         #window1['-OUTPUT3-'].update(' ')
                         window1['-OUTPUT4-'].update(' ')
                         window1['-OUTPUT5-'].update("Error")
                         progress_bar1.UpdateBar(50+correction_value)
                         progress_bar2.UpdateBar(correction_value)
                         window1['-OUTPUT6-'].update("Correct Pitch")
                
                else:
                    window1['-OUTPUT1-'].update('target pitch from user:'+" "*5+values1['combo'])
                    window1['-OUTPUT2-'].update('Pitch of ur instrument :')
                    window1['-OUTPUT4-'].update(str(pitch))
                    #window1['-OUTPUT3-'].update('Target is'+target_str+' '+str(target_pitch))
                    #if (isittuned):
                    #    window1['-OUTPUT4-'].update('Playing at correct Pitch')
                    #else:
                    #    window1['-OUTPUT4-'].update('Correct the Pitch by'+"  "+str(correction_value))
                    window1['-OUTPUT5-'].update("Error")
                    if (correction_value<0):
                        progress_bar1.UpdateBar(50)
                        progress_bar2.UpdateBar(abs(correction_value))
                        if (abs(correction_value)<10):
                            window1['-OUTPUT6-'].update("slight Increase in Pitch")
                        else:
                            window1['-OUTPUT6-'].update("high Increase in Pitch")   
                    elif (correction_value==0):
                        progress_bar1.UpdateBar(50)
                        progress_bar2.UpdateBar(0)
                        window1['-OUTPUT6-'].update("Correct Pitch")
                    else:
                        progress_bar1.UpdateBar(50-correction_value)
                        progress_bar2.UpdateBar(0)
                        if (abs(correction_value)<10):
                            window1['-OUTPUT6-'].update("slight Decrease in Pitch")
                        else:
                            window1['-OUTPUT6-'].update("high Decrease in Pitch")
        
        #window2.close()
        window1['-OUTPUT3-'].update('Stop',text_color="red")
        event1,values1=window1.read()
    
        
