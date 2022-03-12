list=[]
for i in range(10,100):
    x=i//10
    y=i%10
    list.append(int(str(x)+str(y)+str(y)+str(x)))
for x in list:
    print(x)
