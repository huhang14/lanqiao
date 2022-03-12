n=int(input())
l=[]
for i in input().split():
    l.append(i)
list=list(map(int,l))
print(max(list))
print(min(list))
print(sum(list))
