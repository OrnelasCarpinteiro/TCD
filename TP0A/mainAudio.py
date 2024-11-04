import numpy as np
import sounddevice as sd
from scipy.io import wavfile

#1
filename = '/Users/PC/Desktop/TCD/Repositório da disciplina - dkqmekli/TP0/drumploop.wav'
[fs, data] = wavfile.read(filename)

#2 print the table
print('Audio Size:', data.shape, '\nSampling Frequency:',fs)

#3 play the audio
sd.play(data,fs)
sd.wait()