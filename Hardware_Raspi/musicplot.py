# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:24:37 2020

@author: abhin
"""

import PySimpleGUI as sg
import pygame
from speedchange import speed
sg.theme('TealMono')
class Music:

    def __init__(self, file):
        self.pitchalpa = file


        self.layout = [[sg.Radio('Violin','num',key='violin'),sg.Radio('Veena','num',key='veena'),sg.Radio('Flute','num',key='Flute')],
                       [sg.Text(size=(10,1),font="Courier", key='-OUTPUT1-'),sg.Text("volume",font="Courier"),sg.Slider((0,100),100,resolution=1,orientation="h",key="Speed")],
            [sg.Button('Slow', button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename="rwd.png", image_size=(75, 75), image_subsample=2, border_width=0),sg.Button('Play', button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename="play.png", image_size=(75, 75), image_subsample=2, border_width=0), 
             sg.Button('Pause', button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename="pause.png", image_size=(75, 75), image_subsample=2, border_width=0),
             sg.Button('Stop', button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename="stop1.png", image_size=(75, 75), image_subsample=2, border_width=0),
             sg.Button('Fast', button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename="fwd.png", image_size=(75, 75), image_subsample=2, border_width=0)]
        ]
        self.window = sg.Window('Digital Tanpura', self.layout)
    def sound(self):
        print(self.pitchalpa)
        frequency=1.0
        count=1
        pygame.init()
        event, values = self.window.read()
        while True:
            
            try:
                while ((values['violin']==False)&(values['veena']==False)&(values['Flute']==False)):
                    sg.popup_ok('Choose Instrument ')
                    event, values = self.window.read()
            except :
                if TypeError:
                    pygame.mixer.music.stop()
                    break
            else:
            
                
                if (values['violin']):
                    self.path="WAV/Violin "
                elif (values['veena']):
                    self.path="WAV/Veena "
                elif(values['Flute']):
                    self.path="WAV/Flute "
                if event in ('Quit',sg.WIN_CLOSED,None):
                    pygame.mixer.music.stop()
                    
                    self.window.close()
                
                elif event == 'Play':
                    
                    self.window['-OUTPUT1-'].update(frequency)
                    
                    frequency=1
                    pygame.mixer.init()
            
                    pygame.mixer.music.load(self.path+str(self.pitchalpa)+".wav")
                    
                    pygame.mixer.music.play(-1)
                    self.window['-OUTPUT1-'].update(frequency)
                    
                    
                elif event=='Slow':
                    frequency=frequency/2
                    pygame.mixer.music.load(self.path+str(self.pitchalpa)+".wav")
                    
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.stop()
                    
                    speed(self.path+str(self.pitchalpa)+".wav",frequency)
                    
                    pygame.mixer.init()
            
                    pygame.mixer.music.load("changed.wav")
                    
                    pygame.mixer.music.play(-1)
                    self.window['-OUTPUT1-'].update(frequency)
                    
                elif event=='Fast':
                    frequency=frequency*2
                    pygame.mixer.music.load(self.path+str(self.pitchalpa)+".wav")
                    
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.stop()
                    
                    speed(self.path+str(self.pitchalpa)+".wav",frequency)
                    
                    pygame.mixer.init()
            
                    pygame.mixer.music.load("changed.wav")
                    
                    pygame.mixer.music.play(-1)
                    self.window['-OUTPUT1-'].update(frequency)
                    
                elif event== 'Pause':
                    if (count%2==1):
                        pygame.mixer.music.pause()
                        count+=1
                    else:
                        pygame.mixer.music.unpause()
                        count-=1
                elif event== 'Stop':
                    pygame.mixer.music.stop()
                    break
                try:
                    pygame.mixer.music.set_volume(float(values['Speed'])/100)
                except TypeError:
                    pygame.mixer.music.stop()
                    break
            event, values = self.window.read(timeout=2)
        self.window.close()
                
                
        