def binary(number):

    i=0
    t=0
    t = int(t)
    i = int(i)
    k=0
    array = []
    t = number

    for i in array:
        array[i]=t%2
        t = int(t/2)
        k = k+1

    return array


def display(array):
    for i in reversed(array):
        print(array[i])

    display(binary)

    return 0

binary(input('Enter Decimal for Binary conversion:'))
