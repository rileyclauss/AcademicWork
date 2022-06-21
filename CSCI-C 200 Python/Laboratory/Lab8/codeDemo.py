lst = [(2, 4), (1456, 13), (12, 7), (1456, 4), (23, 3), (14, 18), (1456, 4)]
values = [6, 7, 18, 20]
strings = [
    "We are looking for an orange telephone pole that loves lasagna flavored electricity",
    "Welcome to L200, where we will introduce you to electrity that has the flavor of lasagna",
    "This bad boy can fit so much lasagna in it",
    "Honey, where is my super suit"
]
vowels = [
    "aeiouAEIOU",
    "1234567890",
    "stuv",
    "AFKPUZ"
]


def stringChecker(string, search):
    total = 0
    for s in string:
        if s in search:
            total += 1
    return total



def ternaryPractice():
    print("Ternary Practice")
    print("First Ternary")

    for x in values:
        result = "young" if x <18 else "old"
        print("x = {}, Output: {}".format(x,result))
    print()
    print("Second Ternary")
    myLamb = lambda x, y: x % y

    for i,j in lst:
        print("x, y = {},{}   Output: {}".format(i, j, myLamb(i, j)))

def lcPractice():
    print("List Comprehension practice")
    first = [x for x in range(10)]
    print(first)

    second = [x for x in strings if "pole" in x]
    print(second)

    third = [[0 for x in range(3)] for y in range(3)]
    print(third)

def mapping():
    print("Mapping Practice")
    m1 = map(stringChecker, strings, vowels)
    print(list(m1))
    print()
    myLamb = lambda t: t[0] + t[1]
    m2 = map(myLamb, lst)
    print(list(m2))

def filtering():
    print("Filtering Practice")
    myLamb = lambda t:t[0] + t[1] > 50
    f1 = filter(myLamb, lst)
    print(list(f1))
    print()
    checker = lambda xtra: "200" in xtra
    f2 = filter(checker, strings)
    print(list(f2))



ternaryPractice()
print()
lcPractice()
print()
mapping()
print()
filtering()