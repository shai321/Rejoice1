sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]
# dict1={i:sample_dict[i] for i in keys}
# print(dict1)
a={}
for i in keys:
    a[i]=sample_dict[i]
print(a)