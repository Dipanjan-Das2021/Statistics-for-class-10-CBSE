from tabulate import tabulate
interval =['0-10','10-20','20-30','30-40','40-50','50-60','60-70']
frequency =[105,222,220,138,102,113,100]
xi=[]
xifi=[]
for i in range (len(frequency)):
    a=1/2*(int(interval[i].split('-')[0])+int(interval[i].split('-')[1]))
    xi.append(a)
    xifi.append(a*frequency[i])
final=list(zip(interval,frequency,xi,xifi))
print(tabulate(final ,headers=['Interval','Frequency','class mark','Summation(XiFi)'],tablefmt='pipe'))
mean=(sum(xifi))/(sum(frequency))
print('The mean of the data is : ',mean)