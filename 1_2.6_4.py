b = [[]]
i = input()
k = 0
if i == "end":
    print(0)
while i != "end":
    if k == 0:
        b[0] = [int(i) for i in i.split()]
        k = 1
    else:
        b.append([int(i) for i in i.split()])
    i = input()
i=0
while i < len(b):
    j=0
    while j < len(b[0]):

        if i == len(b)-1 and j == len(b[0])-1:
            print(b[i - 1][j] + b[i + 1 - len(b)][j] + b[i][j - 1] + b[i][j + 1 - len(b[0])], end=" ")
        elif i == len(b)-1 and j != len(b[0])-1:
            print(b[i - 1][j] + b[i + 1 - len(b)][j] + b[i][j - 1] + b[i][j + 1], end=" ")
        elif i != len(b) - 1 and j == len(b[0])-1:
            print(b[i - 1][j] + b[i + 1][j] + b[i][j - 1] + b[i][j + 1 - len(b[0])], end=" ")
        else:
            print(b[i-1][j]+ b[i+1][j]+ b[i][j-1] + b[i][j+1], end = " ")
        j+=1
    print()
    i+=1
