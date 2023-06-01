def even(n):
    c=[]
    for i in n:
        if i%2==0:
            c.append(i)
    return c
n=[2,3,4,5,6,7,8,9,10]
a=even(n)
print(a)