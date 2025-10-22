import numpy as np
import matplotlib.pyplot as pl

fig,axs=pl.subplots(3)
fig.suptitle("Semnale")
for ax in axs:
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")

time=np.arange(0,1,1/10000)

def a(t):
    return np.sin(2000* np.pi * t)
atime=a(time)
axs[0].plot(time,atime)
btime=[atime[i] for i in range(0,len(atime),4)]
time2=[time[i] for i in range(0,len(time),4)]

axs[1].plot(time2,btime)
ctime=[atime[i] for i in range(1,len(atime),4)]
time3=[time[i] for i in range(1,len(time),4)]

axs[2].plot(time3,ctime)

#difera frecventa de esantionare


fig.show()
pl.savefig('ex7.pdf')

pl.show()
