import types # This is used to determine if you have function type

def task1():
    return lambda x,y,z: x+y+z

def task2(size, default):
    return [[(default if i!= x else 0) for i in range(size)] for x in range(size)]
    """
    Return a list of a SIZE x SIZE list of lists, that has all default values, 
    except for the diagonal being all zeroes.

    Example:
    task2(3, -1) 

    Produces (formatted to be readable)

    [
     [0, -1, -1],
     [-1, 0, -1],
     [-1, -1, 0]
    ]

    This must be done in form of a list comprehension. 
    
    NOTE: This will be the harder of all the tasks. 
    You might have to refer to some slides. 
    Or come to the lab office hours to get some help visualizing this. 
    """

def task3(list1, list2):
    
    listX = map(lambda x,y: x+y, list1, list2)
    listY = [i + 1000 for i in listX]
    retList = map(lambda a: a, listY) #convert to a map object to return
    return retList
    """
    Using a lambda function (preferably calling from earlier), add the lists together utilizing map 
    Another stipulation is you have to add 1000 to each of them. You must accomplish this with a list comprehension.
    Returns a map object. 

    You can't assume which list will be the max length between the two.

    Example:
    task3([1, 2, 3, 4], [5, 6, 7, 8, 9]) -> map object
    printing above map object as a list in testing -> [1006, 1008, 1010, 1012]
    """
    pass


def listPrinter(lst):
    """
    Do not modify, as this will print lists to be readable
    """
    print("[")
    for l in range(len(lst)):
        print(" " + str(lst[l]) + "," * (l != (len(lst) -1)))
    print("]\n")


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Task 1")
    if isinstance(task1(), types.FunctionType):
        print(task1()(*values[0:3]))
        print(task1()(*values[3:6]))
        print(task1()(*values[6:9]))
    else:
        print("Task 1 is not returning a lambda function")
        print("Is returning: ", type(task1()))
    print()
    
    print("Task 2")
    if isinstance(task2(3, -1), list):
        listPrinter(task2(3, -1))
        listPrinter(task2(5, 100))
    else:
        print("Task 2 is not return a list")
        print("Is return: ", type(task2(3, -1)))
    
    print()
    print("Task 3")
    if isinstance(task3([1],[1]), type(map(lambda x: x, [1]))):
        LISTS1 = [
            [1, 2, 3, 4],
            [-1, -1, -1, -1, -1, -1, -1],
            [200, -2045, 10, 8, 2]
        ]
        LISTS2 = [
            [5, 6, 7, 8, 9],
            [-2, -3, -4, -5, -6, -7, -8],
            [12, 4]
        ]
        for i in range(len(LISTS1)):
            print(list(task3(LISTS1[i], LISTS2[i])))
    else:
        print("Task 3 is not return a map object")
        if isinstance(task3([1], [1]), list):
            print("You should not convert it to a list before returning")
        else:
            print("You are returning: " + str(type(task3([1], [1]))))
        

