roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# roll=[i for i in roll_number if i in sample_dict.values()]
# print(roll)
roll=[i for i in sample_dict.values() if i in roll_number]
print(roll)