def sha_runs_on_coke(parameter1, parameter2):
    sum = parameter1 + parameter2
    print(sum)
    if(parameter1 > parameter2):
        difference = parameter1 - parameter2
    else:
        difference = parameter2 - parameter1

    print(difference)

    multiplication = parameter1 * parameter2
    print(multiplication)

    if(parameter2 != 0):
        division = parameter1 / parameter2
    elif(parameter2 == 0 ):
        division = 'NOT DEFINED'

    print(division)



x = input("ENTER THE FIRST VALUE:")
y = input("ENTER THE SECOND VALUE:")

x = float(x)
y = float(y)

sha_runs_on_coke(x,y)











