from pydub import AudioSegment
def converttomp3(filename):
	sound = AudioSegment.from_wav(filename+'.wav')

	sound.export(filename+'.mp3', format='mp3')