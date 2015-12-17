#!/usr/bin/env python
"""
Time Duration: 2 hours

Purpose:
        MadMachines.io Interview basic test for python
        Our company loves PEP-8 and Make sure you save space while writing code(Less lines of code)
        You can use as many as open-source or built in modules to complete the tasks
        
        Every function has a tag #SHORTEST_CODE which is the minimum number of code lines to complete the task,
        Total marks are:
        There is a penalty of .5 marks for every line in addition to SHORTEST_CODE 
        and bonus of 2 marks for every line less than SHORTEST_CODE

        Blank lines will not be counted either for bonus or for penalty, you can use as many blank lines as you
        wish to improve the readability of the code
"""
import itertools
import random


def Merge_list(__list):
    def flatten(container):
                for i in container:
                    if isinstance(i, list) or isinstance(i, tuple):
                        for j in flatten(i):
                            yield j
                    else:
                        yield i

    return list(flatten(__list))


"""merged_list = list((itertools.chain.from_iterable(__list)))
    return merged_list"""



def edit_list(__list):
        
        ##Highly doubtful about this code.
            
          def uniqueid(sentence):
            review_id = random.randrange(1000,9999)
            while True:
                yield review_id
                review_id += 1

            unique_sequence = uniqueid()
            id = []
            for i in range(0, len(__list)):
                id[i] = uniqueid(__list[i])
            return review_id


def update_edit_list(__list):
        
        ##Highly doubtful about this code.
          def uniqueid(sentence):
            another_id_id = random.randrange(1000,9999)
            while True:
                yield another_id_id
                another_id_id += 1

            unique_sequence = uniqueid()
            id = []
            for i in range(0, len(__list)):
                id[i] = uniqueid(__list[i])
            return id


def sort_list(__list):
        

        __list = __list.sort()
        return __list


def combine_tuples(__list):
        
        ##I AM HIGHLY DOUBTFUL ABOUT THIS CODE RATHER I KNOW IT ISNT CORRECT. JUST TRYING OUT. I AM A BEGINNER AFTERALL!
        list1 = []
        list2 = []
        list3 = []
        for i in __list:
            list1.append(i[0])
            list1.sort()
            list2.append(i[1])
            list2.sort()
        #list3 = zip(list1, list2)
        list3 = list1 + list2
        list4 = zip(list1, list2)
        return list3, list4


def make_decorator(*args, **kwargs):
        """
        SHORTEST_CODE: 9 Line
        It has another function in it, called as for_decoration, you have to build a decorator on it, to
        print its agrs and kwargs
        """

        def for_decoration(*args, **kwargs):
            result = ' '
            result = args+kwargs
            print(result)
        pass
        for_decoration(*args, **kwargs)

        
        def do_decoration():
            ##I DONT KNOW WHAT THIS IS FOR. YOU HAVE NOT MENTIONED THE USE OF THIS.
            pass



def reverse_list(__list):
        __list = __list[::-1]
        return __list


def custom_error(__list):
        
        ##Your code here
        try:
            x = int(input("Enter the index position to be checked:"))
            __list[x]
    
        except IndexError:
            message = "I can neglect ignorance, but not stupidity"
            print(message)
        

"""
f = [(1,0),(2,4),(3,7),(6,4)]
print(combine_tuples(f))
"""
"""custom_error(f)

print(reverse_list(f))"""

#make_decorator('hello', 'sir')

f = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [[[20, 21, 22], [29, 30]], [101, 102, 103]]]

print(Merge_list(f))

