n,m=map(int,input().split())
str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    s=str[1:i+1][::-1]+str[:m-i]
    print(s[0:m])
