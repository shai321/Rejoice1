str1 = "P@#yn26at^&i5ve"
digit=0
char=0
symbol=0
for i in str1:
    if i.isdecimal():
        digit+=1
    elif i.isalpha():
        char+=1
    else:
        symbol+=1
print(f"digit={digit}\nchar={char}\nsymbol={symbol}")
