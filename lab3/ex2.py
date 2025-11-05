import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.collections import LineCollection

fig,axs=plt.subplots(1,2)
fig.suptitle("FIG 1")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("Amplitude")
axs[1].set_xlabel("Real")
axs[1].set_ylabel("Imaginar")
axs[1].set_aspect('equal')


f=10
def sin(t):
    return 1*np.sin(2*f* np.pi * t +0)


time=np.arange(0,1,0.0001)
def z(w):
    return np.array([sin(time[n])* math.e**(-2j*math.pi*time[n]*w) for n in range(len(time))])
sintime=sin(time)
distance = np.sqrt(time**2+sintime**2)
#distance = abs(sintime)
xy = np.reshape(np.transpose(np.array([time,sintime])),(-1,1,2))
lines=np.concat([xy[:-1],xy[1:]],axis=1)
lc = LineCollection(lines, cmap='viridis')
lc.set_array(distance)
axs[0].add_collection(lc)
axs[0].autoscale()
#axs[0].plot(time,sintime)

imagi=z(1)
distance = np.sqrt(np.real(imagi)**2+np.imag(imagi)**2)
xy = np.reshape(np.transpose(np.array([np.real(imagi),np.imag(imagi)])),(-1,1,2))
lines=np.concat([xy[:-1],xy[1:]],axis=1)
lc = LineCollection(lines, cmap='viridis')
lc.set_array(distance)
axs[1].add_collection(lc)
axs[1].autoscale()

fig.tight_layout()
fig.show()
plt.savefig('ex2_1.pdf')
plt.show()


fig,axs=plt.subplots(2,2)
fig.suptitle("FIG 2")
for ax in axs.flatten():
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")
    ax.set_aspect('equal')

imagi=z(1)
distance = np.sqrt(np.real(imagi)**2+np.imag(imagi)**2)
xy = np.reshape(np.transpose(np.array([np.real(imagi),np.imag(imagi)])),(-1,1,2))
lines=np.concat([xy[:-1],xy[1:]],axis=1)
lc = LineCollection(lines, cmap='viridis')
lc.set_array(distance)
axs[0][0].add_collection(lc)
axs[0][0].autoscale()
#axs[0][0].plot(np.real(imagi),np.imag(imagi))
imagi=z(3)
distance = np.sqrt(np.real(imagi)**2+np.imag(imagi)**2)
xy = np.reshape(np.transpose(np.array([np.real(imagi),np.imag(imagi)])),(-1,1,2))
lines=np.concat([xy[:-1],xy[1:]],axis=1)
lc = LineCollection(lines, cmap='viridis')
lc.set_array(distance)
axs[0][1].add_collection(lc)
axs[0][1].autoscale()
# axs[0][1].plot(np.real(imagi),np.imag(imagi))
imagi=z(f)
distance = np.sqrt(np.real(imagi)**2+np.imag(imagi)**2)
xy = np.reshape(np.transpose(np.array([np.real(imagi),np.imag(imagi)])),(-1,1,2))
lines=np.concat([xy[:-1],xy[1:]],axis=1)
lc = LineCollection(lines, cmap='viridis')
lc.set_array(distance)
axs[1][0].add_collection(lc)
axs[1][0].autoscale()
# axs[1][0].plot(np.real(imagi),np.imag(imagi))
imagi=z(15)
distance = np.sqrt(np.real(imagi)**2+np.imag(imagi)**2)
xy = np.reshape(np.transpose(np.array([np.real(imagi),np.imag(imagi)])),(-1,1,2))
lines=np.concat([xy[:-1],xy[1:]],axis=1)
lc = LineCollection(lines, cmap='viridis')
lc.set_array(distance)
axs[1][1].add_collection(lc)
axs[1][1].autoscale()
# axs[1][1].plot(np.real(imagi),np.imag(imagi))

fig.tight_layout()
fig.show()
plt.savefig('ex2_2.pdf')
plt.show()