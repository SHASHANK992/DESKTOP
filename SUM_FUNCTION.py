def sum_two_numbers(a,b):
    sum=0
    sum = a + b
    return sum


def subtract_two_numbers(a,b):
    subtract  = 0
    if a>b:
        subtract = a-b
    elif a<b:
        subtract = b-a
    else:
        subtract = 0

    return subtract

def multiply_two_numbers(a,b):
    multiply = 1
    multiply = multiply * a * b
    return multiply

def division_two_numbers(a,b):
    division = 1
    if (b != 0):
        division = a/b
        return division

def log_two_numers(a,b):
    log = 1
    if (b != 0):
        log = alogb


a = int(input("ENTER THE FIRST NUMBER:"))
b = int(input("ENETER THE SECOND NUMBER:"))
c=0
c = int(c)

c = sum_two_numbers(a,b)
print("%d" %c)

c = subtract_two_numbers(a,b)
print("%d" %c)

c = multiply_two_numbers(a,b)
print("%d" %c)

c = division_two_numbers(a,b)
print("%d" %c)
