import numpy as np
import matplotlib.pyplot as pl
start=0
end=0.03
step=0.0005
# end=0.05
# step=0.0001

time=np.arange(start,end,step)
#print(axr)
def x(t):
    return np.cos(520* np.pi * t + np.pi/3)
def y(t):
    return np.cos(280* np.pi * t - np.pi/3)
def z(t):
    return np.cos(120* np.pi * t + np.pi/3)
fig,axs=pl.subplots(3)
for ax in axs:
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
fig.suptitle("Semnale")
axs[0].plot(time,x(time))
axs[1].plot(time,y(time))
axs[2].plot(time,z(time))
esant=np.arange(start,end,1/200)
axs[0].stem(esant,x(esant))
axs[1].stem(esant,y(esant))
axs[2].stem(esant,z(esant))

fig.show()
pl.show()
