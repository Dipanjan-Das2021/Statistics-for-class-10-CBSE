from tabulate import tabulate
import numpy as np
interval =['20-30','30-40','40-50','50-60','60-70','70-80','80-90']
frequency =[5,15,25,20,7,8,10]
cf=[]
def cumulative (frequency,cf):
    a=0
    for i in range(len(frequency)):
        a=a+frequency[i]
        cf.append(a)
cumulative(frequency,cf)
final = list(zip(interval,frequency,cf))
recurse=0
n=np.sum(frequency)
for i in range (len(frequency)):
    if( cf[i]>n/2) & (recurse==0):
        newf=frequency[i]
        newcf=cf[i-1] if i>0 else 0
        l=int(interval[i].split('-')[0])
        h=int(interval[i].split('-')[1])-int(interval[i].split('-')[0])
        recurse=1
print(tabulate(final,headers=['Interval','Frequency','Cumulative Frequency'],tablefmt='pretty'))
print(f'''Here l={l}
      cumulative frequency={newcf}
      frequency={newf}
      h={h}
      N={n}
      ''')
print('So, Median =',l+(h*(n/2-newcf)/newf))


