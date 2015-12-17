"""Write a python program that will take the following list of words as input and output a dictionary with a the frequency of each word:

words = ['apple', 'apple', 'banana', 'banana', 'banana', 'pear', 'banana', 'pear', 'pear', 'pear', 'pear', 'pear']"""

def frequency(list):
    store = {}
    counter = 0
    for i in range(0, len(list)-1):
        while list[i] == list[i+1]:
            counter += 1
        if list[i] != list[i+1]:
            dict2 = {list[i]: counter}
            store.update(dict2)
    print(store)



words = ['apple', 'apple', 'banana', 'banana', 'banana', 'pear', 'banana', 'pear', 'pear', 'pear', 'pear', 'pear']
frequency(words)


