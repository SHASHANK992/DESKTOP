"""     NESTED LISTS ARE USED LIKE THIS      """
list=[]
for i in range(0,5):
    list.append([0]*5)
print(list)

""" SECOND METHOD:
# Creates a list containing 5 lists initialized to 0
Matrix = [[0 for x in range(5)] for x in range(5)]                   """

for i in range(0,5):
    for j in range(0,5):
        list[i][j]=100*(6-j)

print("                   ")
print(list)
print("                   ")
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

"""
for i in range(0,5):
    for j in range (0,5):
        print(list[i][j])
"""
