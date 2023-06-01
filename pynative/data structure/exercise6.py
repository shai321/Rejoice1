set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
a=set1.intersection(set2)
for i in a:
    set1.remove(i)
print(a)
print(set1)