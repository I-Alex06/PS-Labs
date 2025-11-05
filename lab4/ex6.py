import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
rate,data = wavfile.read('lab4/aud.wav')
n=len(data)
l=[data[i:i+n//100] for i in range(0,n-n//100,n//200)]
fft1=[np.abs(np.fft.fft(l[i])) for i in range(len(l))]
fft1=np.array(fft1).T
fft1=fft1[:n//100//2, :]
fftdb=20*np.log10(fft1+1e-10)


plt.figure(figsize=(10,6))
plt.imshow(fftdb, cmap='viridis',aspect='auto',origin='lower',extent=[0,n/rate,0,rate/2])
plt.colorbar()
plt.tight_layout()
plt.savefig('lab4/ex6.pdf')
plt.show()