def reverse_str(s):
    retS = ""
    for i in range(len(s), 0, -1):
        retS += s[i-1]
    return retS

def reverse_str_while(s):
    length = len(s) - 1
    retS = ""
    while length >= 0:
        retS += s[length]
        length -= 1
    return retS

def reverse_str_tail(s,a=''):
    if s == "":
        return a
    else:
        return reverse_str_tail(s[:-1], a=a+s[-1])

def is_palin(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palin(s[1:-1])

if __name__ == "__main__":
    print("Sum of Squares Practice")
    indicies = ["hello","qwerty","racecar","","!@#$%^&*()"]
    answers  = ["olleh","ytrewq","racecar","",")(*&^%$#@!"]
    functions = [reverse_str, reverse_str_while, reverse_str_tail]

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

    indicies = ["hello", "racecar", "madam", "davinci", "deleveled", "hellokitty", "evitative", "kayak", ""]
    answers  = [False,   True,      True,    False,     True,        False,        True,        True,    True]

    if is_palin(indicies[0]) != None:
        print("="*5, "Testing: "+func.__name__+"()", "="*5)
        print("Our Inputs:", indicies)
        print("Your Outputs:")
        for i in range(len(indicies)):
            result = is_palin(indicies[i])
            correct = int(bool(result == answers[i]))
            print("  {0}({1}) == {2} \t{3}".format(is_palin.__name__, indicies[i], result, ("WRONG", "RIGHT")[correct]))
        print("\n\n")