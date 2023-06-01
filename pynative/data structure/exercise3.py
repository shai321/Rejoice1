list1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
length=len(list1)
l=int(length/3)
start=0
end=l
for i in range(3):
    # sliced=slice(start,end)
    list2=list1[start:end]
    print(i+1,list2)
    print("reversed",list(reversed(list2)))
    start=end
    end+=l