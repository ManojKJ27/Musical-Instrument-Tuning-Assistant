#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:27:45 2020

@author: manojjagannath
"""
from time import time
tick = time() 
import parselmouth
# import matplotlib.pyplot as plt
import numpy as np
from denoise import denoise

import sounddevice as sd
from scipy.io.wavfile import write
from collections import Counter
from math import floor


# while (time.time()-tick < 1):
def snr(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

fs = 44100  # this is the sampling frequency
seconds = 1  # Duration of recording
 
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
print("Listening")
sd.wait()  # Wait until recording is finished
print("Processing")

write('audio.wav', fs, myrecording)  # Save as WAV file

audio = parselmouth.Sound("audio.wav")
# audio = parselmouth.Sound("/Users/manojjagannath/Desktop/PROJECT2/Veena/Sa_E.wav")
audio_snr = snr(audio,1,0)
print("SNR : ",audio_snr[0])
print("SNR (dB) : ",-20 * np.log(np.abs(audio_snr[0])))

def draw_pitch(pitch):
    # Extract selected pitch contour

        pitch_values = pitch.selected_array['frequency']
        
    # Plot the pitch contour
        # plt.plot(pitch.xs(), pitch_values)#, 'o', markersize=2)
        # plt.grid(False)
        # plt.ylim(0, pitch.ceiling)
        # plt.ylabel("fundamental frequency [Hz]")
        # plt.show()
        
        return pitch_values

pitch = audio.to_pitch()


output = draw_pitch(pitch)
result = denoise(output,1,20,320)

print("Pitch : ",np.mean(result))

for i in range(0,len(result)) : 
    result[i] = floor(result[i])
    
cnt = Counter(result)


tock = time() # Stop clock
print("Execution time : ",tock-tick)

