"""
Sum of squares is where you add the squares of all numbers from 1 to n (inclusive).
You can also think of it as the sum of squares from n down to 1.
The function is very similar to factorial in how it is set up.
"""

def while_sos(n):
    result = 1
    while n > 1:
        result += n ** 2
        n -= 1
    return result

def sos(n):
    if n == 1:
        return 1
    else:
        return (n**2) + sos(n-1)

def tail_sos(n, a=1):
    if n == 1:
        return a
    else:
        return tail_sos(n-1, a=a+(n**2))

d = {}
def memo_sos(n):
    if n not in d.keys():
        if n<= 1:
            d[n] = 1
        else:
            d[n] = n**2 +  memo_sos(n-1)
    return d[n]

if __name__ == "__main__":
    print("Sum of Squares Practice")
    indicies = [1, 2, 3,  4,   5,   6,   10]
    answers  = [1, 5, 14, 30,  55,  91, 385]
    functions = [while_sos, sos, tail_sos, memo_sos]

    for func in functions:
        if func(indicies[0]) != None:
            print("="*5, "Testing: "+func.__name__+"()", "="*5)
            print("Our Inputs:", indicies)
            print("Your Outputs:")
            for i in range(len(indicies)):
                result = func(indicies[i])
                correct = int(bool(result == answers[i]))
                print("  {0}({1}) == {2} \t{3}".format(func.__name__, indicies[i], result, ("WRONG", "RIGHT")[correct]))
            print("\n\n")