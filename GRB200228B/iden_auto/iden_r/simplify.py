a=open('test.csv','r')
f=a.readlines()
a.close()
list=[]
for i in range(len(f)):
    f[i]=f[i].strip('/n').split(',')
    sublist=[]
    sublist.append(f[i][23])
    sublist.append(f[i][24])
    sublist.append(f[i][61])
    sublist.append(f[i][62])
    sublist.append(f[i][67])
    sublist.append(f[i][68])
    sublist.append(f[i][71])
    sublist.append(f[i][72])
    list.append(sublist)

b=open('simple_list.csv','w+')
for item in list:
    b.write(','.join(item)+'\n')

b.close()
