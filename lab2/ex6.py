import numpy as np
import matplotlib.pyplot as pl

fig,axs=pl.subplots(3)
fig.suptitle("Semnale")
for ax in axs:
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")

time=np.arange(0,1,1/10000)

def a(t):
    return np.sin(10000* np.pi * t)
axs[0].plot(time,a(time))
def b(t):
    return np.sin(5000* np.pi * t)

axs[1].plot(time,b(time))
def c(t):
    return np.sin(0* np.pi * t)

axs[2].plot(time,c(time))

#b pare uniform
#c este constant zero
fig.show()
pl.savefig('ex6.pdf')

pl.show()
