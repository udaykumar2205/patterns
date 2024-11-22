n=int(input())
star=1
dummy=1
for row in range(1,n+1):
    for star in range(1,star+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    star+=1
