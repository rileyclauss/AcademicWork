"""
This file will be used for practicing with exceptions
"""


# arithmetic errors
def my_divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Incompatible types.")
    
    
# value errors
def my_int(x):
    """
    Convert the given number into an integer
    if the given value is not an integer then return 
    a string (specifically, the input)
    """
    try:
        return int(x)
    except ValueError:
        print("Cannot convert this to an int.")

# type errors
def my_concat(x,y):
    """
    Attempt to concatenated x and y and if they are 
    incompatible types return a string specifying so
    """
    try:
        return x + y
    except TypeError:
        print("Incompatible types.")

def my_sum(x):
    """
    Add up all the values in a list together if there
    exists a non-numeric type in the list then pass
    over it.
    list -> sum
    """
    sumVar = 0
    for i in x:
        try:
            sumVar += i
        except TypeError as err:
            print(err)
    return sumVar



# lookup errors
def my_remove(myList,y):
    """
    Remove y from myList. If y is not present then 
    return a string saying as such
    """
    try:
        myList.remove(y)
    except ValueError as err:
        print(err)

def dict_remove(dictionary,key):
    """
    Remove key from dictionary. If key is not present
    then  return a string saying as such
    """
    try:
        del dictionary[key]
    except KeyError as err:
        print(err)
