def prime_check(input):
    half = input / 2
    half = int(half)
    flag = 156
    for i in range (2, half):
        if (flag == 0):
            return 156

        if (input%i != 0):
            flag = 1
        else:
            flag = flag * 0


    if (flag == 1):
        return input
    else:
        return 156




def enter_number():
    x = input("ENTER THE LIMITING NUMBER:")
    x = int(x)
    for i in range (0, x):
        catch = prime_check(i)
        if (catch != 156):
            obj= open("prime_write.txt",'w')
            text = str(catch)
            obj.write("  ")
            obj.write(text)
            obj.write("  ")


enter_number()



