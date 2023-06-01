number=int(input("Enter the any anuber : "))
pre=0
sum=0
for i in range(0,number):
    sum=pre+i
    print(f"current number {i} + previous number {pre} = {sum}")
    pre=i