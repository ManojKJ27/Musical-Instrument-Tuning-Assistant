#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:47:49 2020

@author: manojjagannath
"""
import pyaudio
import wave
from scipy.io import wavfile as wv

def record(duration):
    # the file name output you want to record into
    filename = "recorded.wav"
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = duration
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                channels=channels,
                rate=sample_rate,
                input=True,
                output=True,
                frames_per_buffer=chunk)
    frames = []
    print("Listening...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk, exception_on_overflow = False)
    # if you want to hear your voice while recording
    # stream.write(data)
        frames.append(data)
    # print("Finished recording.")
# stop and close stream
    stream.stop_stream()
    stream.close()
# terminate pyaudio object
    p.terminate()
# save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()
    
    fs, data = wv.read('recorded.wav') # Read the recorded audio
    
    return fs, data