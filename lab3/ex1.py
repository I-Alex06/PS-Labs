import numpy as np
import matplotlib.pyplot as plt
import math
n=8

f8 = [[math.e**(-2j*math.pi*m*k/n) for k in range(n)] for m in range(n)]
f8= np.array(f8)
# print(f8)
fig,axs=plt.subplots(2,8)
fig.suptitle("Semnale")

for i in range(len(f8)):
    axs[0][i].stem(np.real(f8[i]))
    axs[1][i].stem(np.imag(f8[i]))
    
    #axs[i].plot(np.real(f8[i]),np.imag(f8[i]))

# verificam daca este unitara
f8_test =np.conj(np.transpose(f8)) @ f8

# print(np.real(f8))
# print(np.imag(f8))
print(np.allclose(f8_test, n*np.identity(n)))
# print(f8_test)


# def sin(t):
#     return 2*np.sin(20* np.pi * t + np.pi/2)
# def cos(t):
#     return 2*np.cos(20* np.pi * t + 0)

# time=np.arange(0,1,0.0001)

# axs[0].plot(time,sin(time))
# axs[1].plot(time,cos(time))

fig.show()
plt.savefig('ex1.pdf')
plt.show()

