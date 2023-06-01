sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
list1=[]
for i in sample_list:
    if i not in list1:
        list1.append(i)
print(list1)
print(tuple(list1))
print("max value: ",max(list1))
print("min value: ",min(list1))