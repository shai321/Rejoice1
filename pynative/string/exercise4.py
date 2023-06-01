str1 = "PyNaTive"
l=[]
u=[]
for i in str1:
    if i.islower():
        l.append(i)
    else:
        u.append(i)
sort1="".join(l+u)

print(sort1)
