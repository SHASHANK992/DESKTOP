filler = ("string", "filled", "by a", "tuple")

for i in range (0,4):
    print (" The %d th element of tuple A is : %s" %(i, filler[i]))


for i in range (4):
    print (" The %d th element of tuple A is : %s" %(i, filler[i]))


for key in filler:
    print ("  %s" %key)
