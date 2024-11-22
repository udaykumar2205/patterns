n=int(input())
space=n-1
star=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print('',end=' ')
    for str in range(1,star+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    space-=1
    star+=1
