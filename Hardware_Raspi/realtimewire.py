import pyaudio
import wave
import urllib.request
import struct
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time

# Callback function---------------------------------
def callback(indata, outdata, frames, time, status):

    outdata[:] = indata
#---------------------------------------------------

# Parameters ----------------------------------------------
def realwire():
	Window_Size = 22050 # Point
	FORMAT_D = pyaudio.paFloat32; FORMAT_W = pyaudio.paInt32
	CHANNELS = 1 # Mono
	Sample_Rate = 22050# Hz
	dT = 1/Sample_Rate
	#-----------------------------------------------------------

	p = pyaudio.PyAudio()

	stream_D = p.open(format=FORMAT_D,
		            channels=CHANNELS,
		            rate=Sample_Rate,
		            input=True,
		            frames_per_buffer=Window_Size)


	print("* recording")

	frames = []
	start=time.time()
	data_D = stream_D.read(Window_Size)
	#reading data from microphone
	decoded = np.fromstring(data_D, 'float32') # decoding the read audio
	end=time.time()

	sd.play(decoded,22050)	# Playing the audio
	print(end-start,"\n") #Printing time to check the latency
	stream_D.stop_stream()
	stream_D.close()
	p.terminate()

#-------------------------------------------