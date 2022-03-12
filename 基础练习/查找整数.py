n=int(input())
l=[]
for i in input().split():
    l.append(i)
a=input()
if a in l:
    for i in range(n):
        if l[i]==a:
            print(i+1)
            break
else:
    print(-1)
