str1="jamse"
str2="shai"
l=len(str1)
m=int(l/2)
res=str1[:m:]+str2+str1[m:]
print(res)