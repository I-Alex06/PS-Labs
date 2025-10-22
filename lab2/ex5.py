import numpy as np
import matplotlib.pyplot as pl
import sounddevice as sd
import scipy.io.wavfile as wav


fs=44100
time=np.arange(0,1,0.0001)
def cos(t,frec):
    return 1*np.cos(2*frec* np.pi * t + 0)

signal1=cos(time,100)
signal2=cos(time,1000)
signal3=np.concatenate((signal1,signal2))
print(len(signal1),len(signal2),len(signal3))
sd.play(signal3,fs)
sd.wait()
#al doilea beep are o frecventa mai ridicata si pare mai scurt