import numpy as np
import matplotlib.pyplot as pl

fig,axs=pl.subplots(6)
fig.suptitle("Semnale")
for ax in axs:
    if ax !=axs[4] and ax !=axs[5]:
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
def a(t):
    return np.sin(800* np.pi * t)
time=np.arange(0,1,0.0001)
time2=np.linspace(0,1,1600)
#axs[0].plot(time[0:int(10*(len(time)/len(time2)))],a(time)[0:int(10*(len(time)/len(time2)))])
#axs[0].stem(time2[0:10],a(time2)[0:10])
axs[0].plot(time,a(time))
axs[0].stem(time2,a(time2))

def b(t):
    return np.sin(1600* np.pi * t)
time=np.arange(0,3,0.0001)
axs[1].plot(time,b(time))

time=np.arange(0,1,0.0001)
#axs[2].plot(time,np.mod(time*10000,240)/240)
def c(t):
    f=time[-1]/240
    return 2*(t/f-np.floor(1/2+t/f))
axs[2].plot(time,c(time))

def d(t):
    return int(np.sign(np.sin(600* np.pi * t +0)))

dtime=[d(t) for t in time]
dtime[0]=dtime[1]
axs[3].plot(time,dtime)

#e
arr=np.random.rand(128,128)
axs[4].imshow(arr)

#f
arr2=np.zeros((128,128))
color=np.linspace(0,1,255)
for i in range(len(arr2)):
    for j in range(len(arr2[0])):
        arr2[i][j]=color[i+j]

axs[5].imshow(arr2)

fig.show()
pl.show()
