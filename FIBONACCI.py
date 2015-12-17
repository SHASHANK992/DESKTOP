x=input("ENTER THE LENGTH OF SEQUENCE:")
x = int(x)
a = 0
b = 1
print(a)
print(b)
for i in range(0,x):
    c=a+b
    a=b
    b=c
    print(c)

