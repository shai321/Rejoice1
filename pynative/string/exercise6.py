s1 = "Abc"
s2 = "Xyz"
s1_length=len(s1)
s2_length=len(s2)
length=s1_length if s1_length>s2_length else s2_length
s2=s2[::-1]
res=""

for i in range(length):
    if i<s1_length:
        res=res+s1[i]
    if i<s2_length:
        res=res+s2[i]
print(res)