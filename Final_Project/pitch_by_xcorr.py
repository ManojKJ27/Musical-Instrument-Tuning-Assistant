#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:54:33 2020

@author: manojjagannath
"""

import matplotlib.pyplot as plt
# from math import floor
# from numpy import mean,fft,conj,array
# from numpy import abs as npabs
import librosa

def pitch_by_xcorr(data):

    # freqs = fft.rfft(data)
    # autocorr = fft.irfft(freqs * conj(freqs))
    # data = array(data,dtype=float)
    # lags,c,line,b = plt.acorr(data)
    # plt.plot(lags,c)
    # plt.show()
    sr = 44000
    r = librosa.autocorrelate(data)
    midi_hi = 120.0
    midi_lo = 12.0
    f_hi = librosa.midi_to_hz(midi_hi)
    f_lo = librosa.midi_to_hz(midi_lo)
    t_lo = sr/f_hi
    t_hi = sr/f_lo
    r[:int(t_lo)] = 0
    r[int(t_hi):] = 0
    # r[:1] = 0
    plt.figure(figsize=(14, 5))
    t_max = r.argmax()
    # print(t_max)
    pitch_estimate = float(44100)/t_max
    # plt.plot(r)
    # plt.show()
    return pitch_estimate