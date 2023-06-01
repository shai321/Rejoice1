number=5
start=2
sum=0
for i in range(number):
    print(start,end=" + ")
    sum+=start
    start=start*10+2
print("\n",sum)