#wap to print the pattern number of squares starting from 1.
n=int(input())
for row in range(n):
    for col in range(n):
        print(col+1,end=' ')
    print()
