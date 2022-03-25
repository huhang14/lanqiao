count=0
for num in range(1,2021):
    for i in str(num):
        count+=i.count('2')
print(count)
