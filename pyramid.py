#wap to print the pattern of pyramid.
n=int(input())
space=2*n-1
star=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for str in range(1,star+1):
        print('*',end=' ')
    print()
    space-=1
    star+=2
