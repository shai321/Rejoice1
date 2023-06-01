l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l11=[]
l22=[]
for i in range(len(l1)):
    if i%2!=0:
        l11.append(l1[i])
for i in range(len(l2)):
    if i%2==0:
        l22.append(l2[i])
print("Element at odd-index positions from list one")
print(l11)
print("Element at even-index positions from list one")
print(l22)
print("\nPrinting Final third list")
print(l11+l22)
