x = input("ENTER THE FIRST VALUE:")
y = input("ENTER THE SECOND VALUE:")

x = float(x)
y = float(y)

remainder_1 = x%y
remainder_1 = float(remainder_1)
remainder_2 = y%x
remainder_2 = float(remainder_2)

print ('WHEN X IS DIVIDED BY Y, REMAINDER IS %f' %remainder_1)
print ('WHEN Y IS DIVIDED BY X, RMAINDER is %f' %remainder_2)
