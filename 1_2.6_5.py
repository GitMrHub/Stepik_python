a = int(input())
b = [[0 for i in range(a)] for i in range(a)]
l=0
i=1
n=0
while i < a**2:
    for m in range(l ,a-l-1):
        b[n][m] = i
        i+=1
    m = a-1-l
    for n in range(l, a-l-1):
        b[n][m] = i
        i+=1
    n = a-1-l
    for m in range(n, l, -1):
        b[n][m] = i
        i+=1
    m = l
    for n in range(n, l, -1):
        b[n][m] = i
        i+=1
    l += 1
    n = l

if a %2 ==1:
    b[a//2][a//2]=i

for n in range(a):
    for m in range(a):
        print(b[n][m], end = " ")
    print()
