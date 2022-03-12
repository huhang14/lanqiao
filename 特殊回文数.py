n=int(input())
l=[]
for i in range(100,1000):
    x=i//100
    y=i%100//10
    z=i%10
    if sum([2*x,2*y,z])==n:
        l.append(str(i)+str(y)+str(x))
    if sum([2*x,2*y,2*z])==n:
        l.append(str(i)+str(z)+str(y)+str(x))
l=sorted(map(int,l))
for item in l:
    print(item)
