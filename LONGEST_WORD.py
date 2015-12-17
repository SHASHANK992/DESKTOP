def LongestWord(sen):
    string = sen.split()
    string.sort()

    counter = []
    for i in range(0,1):
        print(string[len(string)-1:])

LongestWord(input("ENTER THE SENTENCE:"))
