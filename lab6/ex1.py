import numpy as np
import matplotlib.pyplot as plt
import math

B=1
time=np.arange(-3,3,1/1000)
fs=[1,1.5,2,4]
ts=[1/f for f in fs]


fig,axs=plt.subplots(2,2)
fig.suptitle("FIG 3")

def x(t):
    return np.sinc(B*t)**2
def x2(t,ts,xn):
    ret=0
    for n in range(len(xn)):
        ret+=xn[n]*np.sinc((t-n*ts)/ts)
    return ret


for i in range(len(axs)):
    for j in range(len(axs[i])):
        axs[i][j].set_xlabel("t[s]")
        axs[i][j].set_ylabel("Amplitude")
        axs[i][j].plot(time,x(time))

for i in range(len(fs)):
    row=i//len(axs)
    col=i%len(axs[row])
    axs[row][col].set_title(f"Fs={fs[i]} Hz")
    samples=np.arange(-3,3,ts[i])
    if 0 not in samples:
        samples=np.append(samples,0)
        samples=np.sort(samples)
    xn=x(samples)
    axs[row][col].stem(samples,xn)
    axs[row][col].plot(time,x2(time,ts[i],xn),'g--')
    






fig.tight_layout()
fig.show()
plt.savefig('lab6/ex3.pdf')
plt.show()
