str1 = "PYnative29@#8496"
sum=0
count=0

for i in str1:
    if i.isdigit():
        sum+=int(i)
        count+=1
print(sum)
print(sum/count)
