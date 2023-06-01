str1 = "/*Jon is @developer & musician"
str2=[]
for i in str1:
    if i.isalpha() or i==" ":
        str2.append(i)
a="".join(str2)
print(a)