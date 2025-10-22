import numpy as np
import matplotlib.pyplot as plt


fig,axs=plt.subplots(4,2)
fig.suptitle("Semnale")

def cos_noise(t,faza,snr):
    time2=cos(t,faza)
    ceva=( (np.linalg.norm(time2)**2) / (np.linalg.norm(z)**2*snr) )**0.5
    time3=time2+ceva*z
    return time3
def cos(t,faza):
    return 1*np.cos(10* np.pi * t + faza)

time=np.arange(0,1,0.0001)
z=np.random.normal(size=len(time))
# print(z)
# print(time)

axs[0][0].plot(time,cos(time,0))
axs[0][1].plot(time,cos(time,np.pi/2))
axs[1][0].plot(time,cos(time,np.pi))
axs[1][1].plot(time,cos(time,3*np.pi/2))

axs[2][0].plot(time,cos_noise(time,0,0.1))
axs[2][1].plot(time,cos_noise(time,0,1))
axs[3][0].plot(time,cos_noise(time,0,10))
axs[3][1].plot(time,cos_noise(time,0,100))

fig.show()
plt.show()