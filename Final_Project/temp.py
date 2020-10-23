# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import parselmouth

# import numpy as np
# # import matplotlib.pyplot as plt
# import time

# tick = time.time()
# while (time.time()-tick < 1):
#     snd = parselmouth.Sound("/Users/manojjagannath/Desktop/PROJECT2/Veena/Sa_E.wav")
# # plt.figure()
# # plt.plot(snd.xs(), snd.values.T)
# # plt.xlim([snd.xmin, snd.xmax])
# # plt.xlabel("time [s]")
# # plt.ylabel("amplitude")
# # plt.show() # or plt.savefig("sound.png"), or plt.savefig("sound.pdf")

# # def draw_spectrogram(spectrogram, dynamic_range=70):
# #     X, Y = spectrogram.x_grid(), spectrogram.y_grid()
# #     sg_db = 10 * np.log10(spectrogram.values)
# #     plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='afmhot')
# #     plt.ylim([spectrogram.ymin, spectrogram.ymax])
# #     plt.xlabel("time [s]")
# #     plt.ylabel("frequency [Hz]")

# # def draw_intensity(intensity):
# #     plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='w')
# #     plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
# #     plt.grid(False)
# #     plt.ylim(0)
# #     plt.ylabel("intensity [dB]")


#     def draw_pitch(pitch):
#     # Extract selected pitch contour, and
#     # replace unvoiced samples by NaN to not plot
#         pitch_values = pitch.selected_array['frequency']
        
        
#         pitch_values[pitch_values==0] = np.nan
#         print(np.mean(pitch_values))
#         # print(len(pitch_values))
#         # plt.plot(pitch.xs(), pitch_values)#, 'o', markersize=5, color='w')
#         # plt.plot(pitch.xs(), pitch_values)#, 'o', markersize=2)
#     # plt.grid(False)
#     # plt.ylim(0, pitch.ceiling)
#         # plt.ylabel("fundamental frequency [Hz]")

#     pitch = snd.to_pitch()
# # intensity = snd.to_intensity()
# # spectrogram = snd.to_spectrogram()
#     # plt.figure()
# # draw_spectrogram(spectrogram)
# # plt.twinx()
# # draw_intensity(intensity)
#     draw_pitch(pitch)
#     # plt.xlim([snd.xmin, snd.xmax])
#     # plt.show() # or plt.savefig("spectrogram.pdf")

import parselmouth
import matplotlib.pyplot as plt
from numpy import mean, log, std
from numpy import abs as npabs
from denoise import denoise
from collections import Counter
from math import floor
from record import record
# from SNR import snr
from denoise_classic import denoise_classic
from scipy.io import wavfile as wv
import numpy as np
from scipy.signal import periodogram as pdgm
# import sounddevice as sd
# from scipy.io.wavfile import write

# tick = time() 
# i = 0
def pitch():
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
    
# fs = 44100  # this is the sampling frequency
# seconds = 1  # Duration of recording
 
# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# print("Listening")
# sd.wait()  # Wait until recording is finished
# print("Processing")

# write('recorded.wav', fs, myrecording)  # Save as WAV file

    record(2)
    fs, data = wv.read('recorded.wav')
    # freqs = np.fft.rfft(data)
    # autocorr = np.fft.irfft(freqs * np.conj(freqs))
    # data = np.array(data,dtype=float)
    # lags,c,line,b = plt.acorr(data)
    # plt.plot(freqs)
    # plt.plot(lags,c)
    f,pxx = pdgm(data,fs)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD')
    plt.ylim([1e-1,1e5])
    plt.xlim([0,5000])
    plt.plot(f,pxx)
    plt.show()
    # wv.write('recorded.wav',fs,np.array(data))
    audio = parselmouth.Sound("recorded.wav")
    # plt.plot(audio.values.T)
    # plt.show()
    # audio = denoise_classic(audio.values.T,10,1e-5)
    # print(mean(npabs(audio)))
    if (mean(npabs(audio.values.T))>1e-5):
    
    # print(audio)
# """    
# audio = parselmouth.Sound("/Users/manojjagannath/Desktop/PROJECT2/Veena/Sa_E.wav")
    # audio_snr = snr(audio,1,0)
    # print("SNR : ",audio_snr[0])
    # print("SNR (dB) : ",-20 * log(npabs(audio_snr[0])))

        pitch = audio.to_pitch()

        output = 0
        result = 0
        output = draw_pitch(pitch)
    # print("Output : ",output)
        result = denoise(output,1,20,520)
        for i in range(0,len(result)) : 
                result[i] = floor(result[i])
    # print("Result : ",result)
    
    # checknan = 0
    # for i in result:
    #     if (isnan(i)):
    #         checknan += 1
    # print("Checknan : ",checknan)
        cnt = Counter(result)
        keys = []
        values = []
        for key in cnt :
            keys.append(key)
            values.append(cnt[key])
        
    # print("Frequency : ", keys)
    # print("Occurances : ", values)
    # print("Max value : ",max(values))
    
        if(len(values) and max(values)>1):
        # print("Standard Deviation : ",std(result))
        # if(std(result)<10):
        #     pitch_mean = mean(result)
        # else:
        #     pitch_mean = 0
            pitch_count = keys[values.index(max(values))]
        # print("Pitch : ",pitch_mean)
            print("Pitch : ",pitch_count)
        # print ("ERROR : ",npabs(pitch_mean-pitch_count))
        else :
            print()


# """

