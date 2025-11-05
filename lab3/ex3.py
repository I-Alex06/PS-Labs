import numpy as np
import matplotlib.pyplot as plt
import math

fig,axs=plt.subplots(1,2)
fig.suptitle("FIG 3")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("x(t)")
axs[1].set_xlabel("Frecventa")
axs[1].set_ylabel("|X(w)|")
# axs[1].set_aspect('equal')



def semnal(t):
    return 3*np.cos(2*23* np.pi * t +0)+0.5*np.cos(2*7* np.pi * t +0)+1*np.cos(2*60* np.pi * t +0)

def dft(w):
    return np.array([semnal(time[n]) * math.e**(-2j*math.pi*n*w/nn) for n in range(nn)])

time=np.arange(0,1,0.0001)
semnal1=semnal(time)
axs[0].plot(time,semnal1)
nn=len(time)
frec=np.arange(0,61,1)
m=np.array([np.abs(np.sum(dft(w))) for w in frec])
m=2*m/nn
axs[1].stem(frec,m)


fig.tight_layout()
fig.show()
plt.savefig('ex3.pdf')
plt.show()
