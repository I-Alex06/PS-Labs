import numpy as np
import matplotlib.pyplot as plt
import math
import csv
import datetime

#a)
# 1/h = 1/3600 Hz
fs=1/3600
# b)
with open('lab5/Train.csv','r') as f:
    r=csv.reader(f)
    header=next(r)
    data=list(r)
ids=np.array([int(row[0]) for row in data])
times=np.array([datetime.datetime.strptime(row[1], '%d-%m-%Y %H:%M').timestamp() for row in data])
counts=np.array([int(row[2]) for row in data])
print(f"b) {datetime.timedelta(seconds=times[-1]-times[0])}")
x=np.fft.fft(counts)
N=len(x)

frec=fs*np.linspace(0,N/2,N//2)/N
print(f"c) {max(frec)}")
print(fs/2)

xm=np.abs(x/N)[:N//2]

plt.stem(frec,xm)
plt.show()


if np.allclose(np.mean(counts),0):
    print("e) Nu are comp cont")
else:
    x2=np.fft.fft(counts-np.mean(counts))
    print(f"e) Eliminata: {np.allclose(x2[0],0)}")
    
#FFFFFF
#fenomene se refera la perioada de timp ex: zilnic,saptamanal,ore de varf, lunii mai aglomerate

#GGGGGG

#HHHHHHH
#nu stii date, poti doar estima dupa frecventa(fenomene periodice, vezi f)  )

#IIIII