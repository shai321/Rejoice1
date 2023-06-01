set1 = {27, 43, 34}
set2 = {34, 93, 22, 27, 43, 53, 48}
print("First set is subset of second set",set1.issubset(set2))
print("second set is subset of first set",set2.issubset(set1))

print("\nFirst set is Super set of second set",set1.issuperset(set2))
print("second set is Super set of first set",set2.issuperset(set1))
print()

if set1.issubset(set2):
    set1.clear()
if set2.issubset(set1):
    set2.clear()
print(set1)
print(set2)
