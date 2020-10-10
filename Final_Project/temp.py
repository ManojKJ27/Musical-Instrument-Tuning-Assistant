# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import parselmouth

import numpy as np
# import matplotlib.pyplot as plt
import time

tick = time.time()
while (time.time()-tick < 1):
    snd = parselmouth.Sound("/Users/manojjagannath/Desktop/PROJECT2/Veena/Sa_E.wav")
# plt.figure()
# plt.plot(snd.xs(), snd.values.T)
# plt.xlim([snd.xmin, snd.xmax])
# plt.xlabel("time [s]")
# plt.ylabel("amplitude")
# plt.show() # or plt.savefig("sound.png"), or plt.savefig("sound.pdf")

# def draw_spectrogram(spectrogram, dynamic_range=70):
#     X, Y = spectrogram.x_grid(), spectrogram.y_grid()
#     sg_db = 10 * np.log10(spectrogram.values)
#     plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='afmhot')
#     plt.ylim([spectrogram.ymin, spectrogram.ymax])
#     plt.xlabel("time [s]")
#     plt.ylabel("frequency [Hz]")

# def draw_intensity(intensity):
#     plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='w')
#     plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
#     plt.grid(False)
#     plt.ylim(0)
#     plt.ylabel("intensity [dB]")


    def draw_pitch(pitch):
    # Extract selected pitch contour, and
    # replace unvoiced samples by NaN to not plot
        pitch_values = pitch.selected_array['frequency']
        
        
        pitch_values[pitch_values==0] = np.nan
        print(np.mean(pitch_values))
        # print(len(pitch_values))
        # plt.plot(pitch.xs(), pitch_values)#, 'o', markersize=5, color='w')
        # plt.plot(pitch.xs(), pitch_values)#, 'o', markersize=2)
    # plt.grid(False)
    # plt.ylim(0, pitch.ceiling)
        # plt.ylabel("fundamental frequency [Hz]")

    pitch = snd.to_pitch()
# intensity = snd.to_intensity()
# spectrogram = snd.to_spectrogram()
    # plt.figure()
# draw_spectrogram(spectrogram)
# plt.twinx()
# draw_intensity(intensity)
    draw_pitch(pitch)
    # plt.xlim([snd.xmin, snd.xmax])
    # plt.show() # or plt.savefig("spectrogram.pdf")




