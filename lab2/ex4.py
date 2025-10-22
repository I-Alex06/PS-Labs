import numpy as np
import matplotlib.pyplot as pl

fig,axs=pl.subplots(3)
fig.suptitle("Semnale")
for ax in axs:
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")

#sin
def b(t):
    return np.sin(12* np.pi * t)
time=np.arange(0,1,0.0001)
btime=b(time)
axs[0].plot(time,btime)


#sawtooth
def c(t):
    f=time[-1]/6
    return 2*(t/f-np.floor(1/2+t/f))
ctime=c(time)
axs[1].plot(time,ctime)

#combinatie
axs[2].plot(time,btime+ctime)

fig.show()
pl.show()
