n=int(input())
n=n//1000
hh=n//3600
hh=hh%24

n=n%3600
mm=n//60
ss=n%60
print("{:02}:{:02}:{:02}".format(hh,mm,ss))