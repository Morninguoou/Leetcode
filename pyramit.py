myInput = int(input())
n = 1
space = myInput -1
for i in range(myInput):
    for j in range(space,0,-1):
        print(" ",end="")
    for k in range(n):
        print("*",end="")
    print()
    space -=1
    n += 2
n -= 2
space += 1
for l in range(myInput-1):
    space += 1
    n -= 2
    for h in range(space):
        print(" ",end="")
    for m in range(n):
        print("*",end="")
    print()