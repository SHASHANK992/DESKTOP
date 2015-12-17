def space_remover(string):
    """REMOVES UNWANTED SPACES THAT CAN AFFECT FACTORIAL CALCULATIONS FOR ARRANGEMENTS VARIABLE"""
    i=0
    for i in range(0, len(string)-1):
            if string[i]== " ":
                string = string[:i] + string[(i+1):]
    return string


def similar(string,pos):
    """COUNTS SIMILAR LETTERS THANT AFFECT FACTORIAL CALCULATIONS IN DENOMINATOR"""
    counter=0
    i=0
    pos = int(pos)
    string = str(string)

    for i in range(pos, len(string)):
        if(string[pos] == string[i]):
            counter+=1

    return counter


def factorial(num):
    """CALCULATES FACTORIAL OF  INTEGERS AND RETURNS CORRESPONDING VALUES"""
    fac = 1
    if num > 1:
        for i in range(1,num+1):
            fac = fac*i

    elif num==0:
        return 1
    else:
        return fac
    return fac




denom = 1
value = 1


string2 = input("\nENTER THE STRING FOR CALCULATING ARRANGEMENTS:\n")

string1 = space_remover(string2)
print(space_remover(string1))

recurrence_counter = []
for i in range(0, len(string1)):
    recurrence_counter.append(1)

for i in range(0, len(string1)):
    recurrence_counter[i]=similar(string1,i)

new = 1
for i in range(0, len(recurrence_counter)):
    denom = denom * recurrence_counter[i]


arrangements = 0
possible_arrangements = 0

arrangements = factorial(len(string1))
possible_arrangements = int(arrangements/denom)
print("\nDENOMINATOR IS: %d" %denom)
print("\nEND:%s" %recurrence_counter)
print("\nTOTAL POSSIBLE ARRANGEMENT:%s" %possible_arrangements)




