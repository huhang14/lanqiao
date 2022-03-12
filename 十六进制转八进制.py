n=eval(input())
x=[0 for x in range(n)]
for i in range(n):
    x[i]=int(input(),16)
    x[i]=oct(x[i])
for a in x:
    print(a[2:], end='\n')
