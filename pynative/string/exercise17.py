str1 = "Emma25 is Data scientist50 and AI Expert"
for i in str1.split():
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        print(i)