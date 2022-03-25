n=int(input())
l=[0]*n
for i in range(n):
    l[i]=int(input())
print(max(l))
print(min(l))
print("{:.2f}".format(sum(l)/n))
