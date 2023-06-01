str1 = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
str2=[]
for i in str1:
    if i:
        str2.append(i)
print(str2)