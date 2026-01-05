import numpy as np
import matplotlib.pyplot as plt
fig,axs=plt.subplots(3)
N=1000

trend=np.array([1/500*x**2 for x in np.linspace(0,100,N)])
frec=10
seasonal=np.array([2*np.cos(2*frec* np.pi * t + 0) +3*np.sin(3*2*frec* np.pi * t + 0) for t in np.linspace(0,1,N)])
noise=np.random.normal(0,1,N)
time_series=trend+seasonal+noise

# singur
alpha=0.3
ales=[]
ales.append(time_series[0])
for i in range(1,N):
    elem=0
    for j in range(i):
        elem+=(1-alpha)**j*time_series[i-j]+(1-alpha)**i*time_series[0]
    ales.append(alpha*elem)
calculat=[]
def get_s(alpha):
    s=[]
    s.append(time_series[0])
    for i in range(1,N):
        s_new=alpha*time_series[i]+(1-alpha)*s[i-1]
        s.append(s_new)
    return s
def get_val(alpha):
    s=get_s(alpha)
    val=0
    for i in range(N-2):
        val+=(s[i]-time_series[i+1])**2
    return val
def calc_alpha():
    min_alpha=0.01
    min_val=get_val(0.01)
    for a in np.arange(0.01,1,0.01):
        print(a)
        v=get_val(a)
        if v<min_val:
            min_val=v
            min_alpha=a
    return min_alpha

alpha=calc_alpha()
calculat=get_s(alpha)
print("\n\n\nalpha=",alpha)
axs[0].plot(time_series)

#
axs[1].plot(ales)
axs[2].plot(calculat)

fig.show()
plt.savefig('lab9/2_1.pdf')
plt.show()

# dubla
fig,axs=plt.subplots(3)


def get_x(alpha,beta,m):
    s=[]
    b=[]
    s.append(time_series[0])
    b.append(time_series[1]-time_series[0])
    
    for i in range(1,N):
        s_new=alpha*time_series[i]+(1-alpha)*(s[i-1]+b[i-1])
        s.append(s_new)
        b_new=beta*(s[i]-s[i-1])+(1-beta)*b[i-1]
        b.append(b_new)
    x=[]
    for i in range(m):
        x.append(time_series[i])
    for i in range(N-m):
        x.append(s[i]+m*b[i])
    return x
def get_val2(alpha,beta,m):
    s=get_x(alpha,beta,m)
    val=0
    for i in range(N-2):
        val+=(s[i]-time_series[i+1])**2
    return val
def calc_alpha_beta():
    min_alpha=0.0
    min_beta=0.0
    min_val=get_val2(0.0, 0.0, 1)
    for a in np.arange(0.0,1,0.01):
        for b in np.arange(0.0,1,0.01):
            v=get_val2(a,b,1)
            print(a,b,v)
            if v<min_val:
                min_val=v
                min_alpha=a
                min_beta=b
    return min_alpha,min_beta

alpha=0.3
beta=0.6
ales=get_x(alpha,beta,1)

alpha,beta=calc_alpha_beta()
calculat=get_x(alpha,beta,1)
print("\n\n\nalpha=",alpha," beta=",beta)


#
axs[0].plot(time_series)
axs[1].plot(ales)
axs[2].plot(calculat)

fig.show()
plt.savefig('lab9/2_2.pdf')
plt.show()