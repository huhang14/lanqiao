for i in range(100,1000):
    x=i//100
    y=i%100//10
    z=i%10
    if sum([pow(x,3),pow(y,3),pow(z,3)])==i:
        print(i)
