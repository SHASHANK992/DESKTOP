x = input("ENTER THE FIRST VALUE:")
y = input('ENTER THE SECOND VALUE:')
x = float(x)
y = float(y)


if (x != 0):
    Divide_1 = y/x
else:
    print ("Divide by zero error. Please enter a different vlaue for x.")

if (y != 0):
    Divide_2 = x/y
else:
    print ("Divide by zero error. Please enter a different vlaue for y.")

Divide_1 = float(Divide_1)
Divide_2 = float(Divide_2)

print("When X is divided by Y, we obtain %f" %Divide_2)
print("When Y is divided by X, we obtain %f" %Divide_1)

