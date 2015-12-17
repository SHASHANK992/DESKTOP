def FirstFactorial(num):
    value = 1
    for i in range(1,num+1):
        value = value * i
    return value

value = 1
fact = input("Enter Value for Factorial:")
fact = int(fact)

print(FirstFactorial(fact))
