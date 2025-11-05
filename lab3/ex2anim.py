import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.collections import LineCollection
from matplotlib.animation import FuncAnimation
import ffmpeg

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

imagi=z(1)
axs[0].set_xlim(0,1)
axs[0].set_ylim(-1,1)
axs[1].set_xlim(min(np.real(imagi))*1.1,max(np.real(imagi))*1.1)
axs[1].set_ylim(min(np.imag(imagi))*1.1,max(np.imag(imagi))*1.1)
pas=20
indexs = np.arange(0,len(imagi),pas)
lc = [LineCollection([],cmap='viridis') for _ in range(2)]
axs[0].add_collection(lc[0])
axs[1].add_collection(lc[1])

curr_point=[axs[i].plot([],[],'ko')[0] for i in range(2)]

distance1 = np.sqrt(time**2+sintime**2)
distance2 = np.sqrt(np.real(imagi)**2+np.imag(imagi)**2)
lc[0].set_array(distance1)
lc[1].set_array(distance2)
def init():
    for l in lc:
        l.set_segments([])
    for p in curr_point:
        p.set_data([],[])
    return lc+curr_point
def animate(frame):
    ind=indexs[frame]
    
    if ind>0:
        t_slice = time[:ind]
        s_slice = sintime[:ind]
        xy = np.reshape(np.transpose(np.array([t_slice,s_slice])),(-1,1,2))
        lines=np.concat([xy[:-1],xy[1:]],axis=1)
        lc[0].set_segments(lines)
    curr_point[0].set_data([time[ind]],[sintime[ind]])
    
    if ind>0:
        imagi_slice = imagi[:ind]
        xy = np.reshape(np.transpose(np.array([np.real(imagi_slice),np.imag(imagi_slice)])),(-1,1,2))
        lines=np.concat([xy[:-1],xy[1:]],axis=1)
        lc[1].set_segments(lines)
    curr_point[1].set_data([np.real(imagi[ind])],[np.imag(imagi[ind])])
    return lc+curr_point
anim = FuncAnimation(fig, animate, init_func=init, frames=len(indexs), interval = 1, blit=True)


plt.tight_layout()
plt.show()
anim.save('ex2_1_anim.gif', writer='pillow', fps=30)
print("DONE SAVE")

fig,axs=plt.subplots(2,2)
fig.suptitle("FIG 2")
for ax in axs.flatten():
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")
    ax.set_aspect('equal')


lc = [LineCollection([],cmap='viridis') for _ in range(4)]
axs[0][0].add_collection(lc[0])
axs[0][1].add_collection(lc[1])
axs[1][0].add_collection(lc[2])
axs[1][1].add_collection(lc[3])
curr_point=[axs[i][j].plot([],[],'ko')[0] for i in range(2) for j in range(2)]


imagi=z(1)
axs[0][0].set_xlim(min(np.real(imagi))*1.1,max(np.real(imagi))*1.1)
axs[0][0].set_ylim(min(np.imag(imagi))*1.1,max(np.imag(imagi))*1.1)
distance = np.sqrt(np.real(imagi)**2+np.imag(imagi)**2)
lc[0].set_array(distance)
#axs[0][0].plot(np.real(imagi),np.imag(imagi))
imagi=z(3)
axs[0][1].set_xlim(min(np.real(imagi))*1.1,max(np.real(imagi))*1.1)
axs[0][1].set_ylim(min(np.imag(imagi))*1.1,max(np.imag(imagi))*1.1)
distance = np.sqrt(np.real(imagi)**2+np.imag(imagi)**2)
lc[1].set_array(distance)
# axs[0][1].plot(np.real(imagi),np.imag(imagi))
imagi=z(f)
axs[1][0].set_xlim(min(np.real(imagi))*1.1,max(np.real(imagi))*1.1)
axs[1][0].set_ylim(min(np.imag(imagi))*1.1,0.1)
distance = np.sqrt(np.real(imagi)**2+np.imag(imagi)**2)
lc[2].set_array(distance)
# axs[1][0].plot(np.real(imagi),np.imag(imagi))
imagi=z(15)
axs[1][1].set_xlim(min(np.real(imagi))*1.1,max(np.real(imagi))*1.1)
axs[1][1].set_ylim(min(np.imag(imagi))*1.1,max(np.imag(imagi))*1.1)
distance = np.sqrt(np.real(imagi)**2+np.imag(imagi)**2)
lc[3].set_array(distance)
# axs[1][1].plot(np.real(imagi),np.imag(imagi))

def animate2(frame):
    ind=indexs[frame]
    for i, w in enumerate([1,3,f,15]):
        imagi=z(w)
        if ind>0:
            imagi_slice = imagi[:ind]
            xy = np.reshape(np.transpose(np.array([np.real(imagi_slice),np.imag(imagi_slice)])),(-1,1,2))
            lines=np.concat([xy[:-1],xy[1:]],axis=1)
            lc[i].set_segments(lines)
        curr_point[i].set_data([np.real(imagi[ind])],[np.imag(imagi[ind])])
anim = FuncAnimation(fig, animate2, init_func=init, frames=len(indexs), interval = 1)

plt.tight_layout()
plt.show()
anim.save('ex2_2_anim.gif', writer='pillow', fps=30)
print("DONE SAVE 2")
