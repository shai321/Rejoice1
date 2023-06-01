string = "Emma is good developer. Emma is a writer"
# print(string.count("Emma"))
a=0
for i in string.split():
    if i=="Emma":
        a+=1
print(a)

