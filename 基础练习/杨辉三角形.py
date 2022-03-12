n=int(input())
l=[1]
if n==1:
    print(1)
else:
    print(1)
    for i in range(n-1):
        l=[1]+[l[n]+l[n+1] for n in range(len(l)-1)]+[1]
        for x in l:
            print(x,end=' ')
        print()
