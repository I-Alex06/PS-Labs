import numpy as np
import matplotlib.pyplot as plt
import math
import time
nl=[128*2**i for i in range(0,7)]
print(nl)


matrix = [np.array([[math.e**(-2j*math.pi*m*k/n) for k in range(n)] for m in range(n)]) for n in nl]
t=[np.linspace(0,1,n) for n in nl]

def dft(index):
    return matrix[index] @ t[index]


def fft(t):
    n=len(t)
    if n<=1:
        return t
    wn = math.e**(-2j*math.pi/n)
    w=1
    t_even=fft(t[::2])
    t_odd=fft(t[1::2])
    y=[0]*n
    for i in range(n//2):
        y[i]=t_even[i]     +  w*t_odd[i]
        y[i+n//2]=t_even[i] -  w*t_odd[i]
        w=w*wn
    return y

times_dft=[]
times_fft=[]
times_npfft=[]

print("Enter loop")
for i in range(len(nl)):
    print(i)
    print('DFT')
    start=time.perf_counter()
    rdft=dft(i)
    stop=time.perf_counter()
    times_dft.append(stop-start)
    print("FFT")
    start=time.perf_counter()
    rfft=fft(t[i])
    stop=time.perf_counter()
    times_fft.append(stop-start)
    print("NP FFT")
    start=time.perf_counter()
    rnpfft=np.fft.fft(t[i])
    stop=time.perf_counter()
    times_npfft.append(stop-start)
    
    if not np.allclose(rdft, rfft):
        print("Wrong 1")
        break
    if not np.allclose(rnpfft, rfft):
        print("Wrong 2")
        break
    
print("Exit loop")
plt.plot(nl, list(map(math.log10,times_dft)),'r',)
plt.plot(nl, list(map(math.log10,times_fft)),'g')
plt.plot(nl, list(map(math.log10,times_npfft)),'b')
plt.legend(['DFT','FFT','NP FFT'])

plt.savefig('lab4/ex1.pdf')
plt.show()