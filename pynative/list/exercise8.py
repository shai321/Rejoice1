list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = [1]
list1[2][1][2].append(sub_list)
print(list1)

# a = [1,2,3]
# b = [1,2,3]
# for i in b:
#     a.append(i)
# print(a)
