import numpy as np
from tabulate import tabulate
interval=['80-85','85-90','90-95','95-100','100-105','105-110','110-115']
frequency =[33,27,85,155,110,45,15]
final=zip(interval,frequency)
print(tabulate(final,headers=['Interval','Frequency'],tablefmt='pretty'))
i=frequency.index(np.max(frequency))
l=int(interval[i].split('-')[0])
h=int(interval[i].split('-')[1])-int(interval[i].split('-')[0])
f1=frequency[i]
f0=frequency[i-1]
f2=frequency[i+1]
mode=(l+h)*(f1-f2)/(2*f1-f0-f2)

print(f'''Here l={l}
      f1={f1}
      f2={f2}
      f0={f0}
      H ={h}
      ''')
print('Hence mode is ',mode)