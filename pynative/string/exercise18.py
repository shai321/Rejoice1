import string
str1 = '/*Jon is @developer & musician!!'
symbol="#"
for i in string.punctuation:
    str1=str1.replace(i,symbol)
print(str1)