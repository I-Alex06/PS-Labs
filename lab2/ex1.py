import numpy as np
import matplotlib.pyplot as plt


fig,axs=plt.subplots(2)
fig.suptitle("Semnale")

def sin(t):
    return 2*np.sin(20* np.pi * t + np.pi/2)
def cos(t):
    return 2*np.cos(20* np.pi * t + 0)

time=np.arange(0,1,0.0001)

axs[0].plot(time,sin(time))
axs[1].plot(time,cos(time))

fig.show()
plt.show()