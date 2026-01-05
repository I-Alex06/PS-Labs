import numpy as np
import matplotlib.pyplot as plt
N=1000

trend=np.array([1/500*x**2 for x in np.linspace(0,100,N)])
frec=10
seasonal=np.array([2*np.cos(2*frec* np.pi * t + 0) +3*np.sin(3*2*frec* np.pi * t + 0) for t in np.linspace(0,1,N)])
noise=np.random.normal(0,1,N)
time_series=trend+seasonal+noise

cor1=np.correlate(time_series,time_series,mode='full')
#cor1=cor1[cor1.size//2:]
# p=2
# cor2=[]
# for i in range(N):
#     s=0
#     for j in range(N-p):
#         s+=time_series[j]*time_series[j-i]
#     cor2.append(s)
# cor2=np.array(cor2)


p=2
ym=np.array([[time_series[i-j-1] for j in range(p)] for i in range(p,N)])
theta=ym.T @ ym
gama=theta[:,0]
# print(gama)
plt.plot(cor1)
plt.savefig('lab8/b.pdf')
plt.show()

