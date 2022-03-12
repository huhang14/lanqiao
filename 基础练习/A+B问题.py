x=5
y=3
i=1
mi=min(x,y)
ma=max(x,y)
d=ma-mi
while d!=mi:
    i=i+1
    d=max(d,mi)-min(d,mi)
    mi=min(d,mi)

print(i)
