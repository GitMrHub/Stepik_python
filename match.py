a = int(input())
b=[[i for i in input().split(';')]for j in range(a) ]
c = dict()
for i in b:
    if i[0] not in c.keys():
        c[i[0]]=[]
    if i[2] not in c.keys():
        c[i[2]]=[]
    if i[1] < i[3]:
        c[i[0]].append('l')
        c[i[2]].append('w')
    elif i[1] == i[3]:
        c[i[0]].append('p')
        c[i[2]].append('p')
    else:
        c[i[0]].append('w')
        c[i[2]].append('l')
for key in c.keys():
    print(key + ":"  + str(len(c[key])), end = " ")
    w=0
    p=0
    l=0
    for x in c[key]:
        if x =='w':
            w+=1
        if x =='p':
            p+=1
        if x =='l':
            l+=1
    print( w , p ,l, w*3 + p )
