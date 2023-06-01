list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
a=[i for i in list1 if i%2!=0]
b=[j for j in list2 if j%2==0]
print(a+b)

