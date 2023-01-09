def add(a,b):
    # return a+b
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError("OOps you are passing wrong data type to function")    

print(add('2','3'))    