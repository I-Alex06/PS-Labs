import numpy as np
import matplotlib.pyplot as plt
fig,axs=plt.subplots(4)
N=1000

trend=np.array([1/500*x**2 for x in np.linspace(0,100,N)])
frec=10
seasonal=np.array([2*np.cos(2*frec* np.pi * t + 0) +3*np.sin(3*2*frec* np.pi * t + 0) for t in np.linspace(0,1,N)])
noise=np.random.normal(0,1,N)
time_series=trend+seasonal+noise

axs[0].plot(time_series)
axs[1].plot(trend)
axs[2].plot(seasonal)
axs[3].plot(noise)

fig.show()
plt.savefig('lab8/a.pdf')
plt.show()
