speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
print(speed.values())
list1=[]
for i in speed.values():
    if i not in list1:
        list1.append(i)
print(list1)