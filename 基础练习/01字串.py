n,m=map(int,input().split())
str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str1=str[:m]
print(str1)
for i in range(1,n):
    print(str(list(reversed(str1[:i]))))
