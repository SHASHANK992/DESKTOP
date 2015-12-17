def bubble_sort(list):
    for i in range(0, len(list)-1):
        for j in range(i+1, len(list)):
            if list[i]>list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list




def insertion_sort(list):
   for i in range(1,len(list)):

     currentvalue = list[i]
     position = i

     while position>0 and list[position-1]>currentvalue:
         list[position] = list[position-1]
         position = position-1

     list[position]=currentvalue
   return list




my_list = [100, 324, 453, 131, 43, 273, 456, 345, 287, 674, 475, 232, 241, 3423, 34, 43, 345, 134, 235, 76, 657, 674, \
           2423, 10789, 3423, 1134, 141241, 124, 441, 12241, 124, 21, 214, 123, 142, 23, 12, 3, 12, 1, 4134314, 14]
print(bubble_sort(my_list))

print(insertion_sort(my_list))
