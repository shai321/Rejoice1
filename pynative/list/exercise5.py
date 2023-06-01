list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2=list2[::-1]
for i,j in zip(list1,list2):
    print(i,j)