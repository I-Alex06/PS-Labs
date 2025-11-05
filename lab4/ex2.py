import numpy as np
import matplotlib.pyplot as plt
import math

fig,axs=plt.subplots(4)
fig.suptitle("Semnale")

    
def cos(t,f):
    return np.cos(2*np.pi*f*t)
time=np.arange(0,1,1/10000)
time1=np.linspace(0,1,5)
axs[0].plot(time,cos(time,21))
axs[1].plot(time,cos(time,21))
axs[1].stem(time1,cos(time1,21))

axs[2].plot(time,cos(time,11))
axs[2].stem(time1,cos(time1,11))

axs[3].plot(time,cos(time,1))
axs[3].stem(time1,cos(time1,1))

fig.show()
plt.savefig('lab4/ex2.pdf')
plt.show()

