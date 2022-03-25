n=int(input())
l=[0]*n
pass_num=0
good_num=0

for i in range(n):
    grade=int(input())
    l[i]=grade
    if grade>=60:
        pass_num+=1
    if grade>=85:
        good_num+=1
        
print("{:.0%}".format(pass_num/n))
print("{:.0%}".format(good_num/n))
