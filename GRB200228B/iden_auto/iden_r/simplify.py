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
    list.append(sublist)

b=open('simple_list.csv','w+')
for item in list:
    b.write(','.join(item)+'\n')

b.close()
