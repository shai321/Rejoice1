numbers = [12, 75, 150, 180, 145, 525, 50]
a=[]
for i in numbers:
    if 500<i:
        break
    elif 150<i:
        continue
    elif i%5==0:
        a.append(i)
print(a)
