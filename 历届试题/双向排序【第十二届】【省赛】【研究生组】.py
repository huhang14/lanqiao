def down(l):
    a=sorted(l,reverse=True)
    return a

def up(l):
    a=sorted(l)
    return a

n,m=map(int,input().split())
l=list(range(1,n+1))
for i in range(m):
    p,q=map(int,input().split())
    if p==0:
        l=down(l[:q])+l[q:]
    elif p==1:
        l=l[:q-1]+up(l[q-1:])
for x in l:
    print(x, end=' ')
