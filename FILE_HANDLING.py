import os

def make_new_text_file():
    #if os.path.isfile('test.txt'):
     #   print("This file already exists.")
    #else:
        obj = open('test.txt', 'w')
        for i in range(-10000, 10000):
            text = str(i)
            obj.write("  ")
            obj.write(text)
            obj.write("  ")

def read_the_file():
    obj = open('test.txt', 'r')
    text = obj.read()
    print(text)

make_new_text_file()
read_the_file()
