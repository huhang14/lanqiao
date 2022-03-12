a=1
b=1
n=int(input())
for i in range(n-1):
    a,b=b,(a+b)%10007
print(a)
