import os
import sys

str=input()
l=[0]*26

for i in str:
    l[ord(i)-97]+=1
print(chr(l.index(max(l))+97))
print(max(l))
