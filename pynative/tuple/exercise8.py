tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29),('e',34),('f',5))
tuple2=tuple(sorted(list(tuple1), key=lambda x:x[1]))
print(tuple2)