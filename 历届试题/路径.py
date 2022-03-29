import math

def gbs(a,b):
    gy=math.gcd(a,b)
    return a*b/gy
l=[float('inf')]*2022
l[1]=0
for i in range(1,2022):
    for j in range(i+1,i+22):
        if j>2021:
            break
        l[j]=min(l[j],l[i]+gbs(i,j))
print("{:.0f}".format(l[2021]))
