'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''

n=int(input())
star=1
for row in range(1,n+1):
    for str in range(1,star+1):
        print('*',end=' ')
    print()
    star+=1
