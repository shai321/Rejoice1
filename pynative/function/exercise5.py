def outer(a,b):
    def addition(a,b):
        return a+b
    add=addition(a,b)
    return add+5
res=outer(3,5)
print(res)