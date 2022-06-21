from ExceptionPractice import *

def testing_func(theFunction,testCases,answers):
    print(f"~~~TESTING {theFunction.__name__}()~~~\n")
    for i in range(len(testCases)):
        result = theFunction(*testCases[i])
        if result is None:
            print("You caught the error!")
        elif result != answers[i]:
            print(f"Test {testCases[i]} Failed")
            print(f"Proper Solution = {answers[i]}")
            print(f"Your Solution = {result}")
    print()




if __name__ == "__main__":

    testCases = [(5,3),(2,4),(4,0)]
    answers = [5/3,2/4,None]
    testing_func(my_divide,testCases,answers)

    
    testCases = [("hel","lo"),(1,3),("hel",3)]
    answers = ["hello",4,None]
    testing_func(my_concat,testCases,answers)


    testCases = [('1',),('345',),("hello there",)]
    answers = [1,345,None]
    testing_func(my_int,testCases,answers)

    testCases = [([1,2,3,4,5],), ([1,2,3,4,"hello"],), ([1,2,{'hel':0},4,5],)]
    answers = [15,10,12]
    testing_func(my_sum,testCases,answers)

    testCases = [ ([1,2,3,4],4),
                  ([1,2,3,4],5),
                  (["hello","yes","there"],"yes"),
                  (["hello","there"],'yes')]
    answers = [ [1,2,3],
                None,
                ['hello','there'],
                None
                ]
    testing_func(my_remove,testCases,answers)

    testCases = [ ({"hello":0,"bye":1},"hello"),
                  ({"there":1,"yes":2},"key",),
                  ({"yes":3,"fun":2},"yes") ]
    answers = [ {"bye":1},
                None,
                {"fun":2}]
    testing_func(dict_remove,testCases,answers)