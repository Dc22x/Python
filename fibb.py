def fibb(a,b):
    for i in range(0, 10):
        yield a
        a,b = b , a+b
        
a = 0
b= 1
fibbonaci = fibb(a,b)
list(fibbonaci)



