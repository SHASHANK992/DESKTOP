largest = None
smallest = None
num = 100*[9999]
def bubble_sort(list):
    for i in range(0, len(list)-1):
        for j in range(i+1, len(list)):
            if list[i]>list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list
i=0
while True:
    try:
        x= input("Enter a number: ")
        if(x != "done"):
            num[i]=int(x)
        if x == "done" :
            print("Invalid input")
            break
    except:

        print("Invalid input")

    i=i+1

num = bubble_sort(num)
smallest = str(num[0])
largest = str(num[i-1])
print ("Maximum is "+largest)
print("Minimum is "+smallest)
