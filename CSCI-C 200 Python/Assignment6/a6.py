###########################################################################
# Introduction Code (As reference)
###########################################################################

def o(x,xlst):
    if xlst:
        return xlst[0] == x or o(x, xlst[1:])
    else:
        return False

def ol(x,xlst):
    def oh(xlst):
        if xlst:
            return xlst[0] == x or oh(xlst[1:])
        else:
            return False
    return oh(xlst)

if __name__ == "__main__":
    """ Demo introductory code """
    # print("~"*20 + "Introduction" + "~"*20 + "\n")
    # print(o(1,[1,2,3]))
    # print(o(4,[1,2,3]))
    # print(ol(1,[1,2,3]))
    # print(ol(4,[1,2,3]))
    # print("\n" * 3)


#f
def f(n):
    if n == 0:
        return 0
    else:
        return n + f(n-1)

if __name__ == "__main__":
    """ To show the recursion function 
    is really a summation """
    # print(f"f(5) = {f(5)}")
    # print(sum(range(6)))

#ft
def ft(n,v=0):
    if n == 0:
        return v
    else:
        return ft(n-1, v + n)



def f_a(n):
    return (1/2) * (n*(n+1))

if __name__ == "__main__":
    """ Demo tail recursion"""
    # print(f"ft(5) = {ft(5)}")
    # print(f_a(5))

from time import perf_counter

def f_loop(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

if __name__ == "__main__":
    """
    To showcase the inefficiany of f_loop
    """
    # big_number = 100000000

    # start = perf_counter()
    # f_a(big_number)
    # end = perf_counter()
    # print(f"Analytic took {end - start } seconds")

    # start = perf_counter()
    # f_loop(big_number)
    # end = perf_counter()
    # print(f"loop took {end - start } seconds")

###########################################################################
# Problem 1
###########################################################################
def F(n,m,p):
    if p == 0:
        return 100 + n - m
    else:
        return ((n*m) - p + F(n-3,m-2,p-1))

def Ft(n,m,p,v = 100):
    if p == 0:
        return v + n - m
    else:
        return Ft(n-3,m-2,p-1,(n*m - p + v))


def gsf_close(a,r,n):
    if r == 1:
        return 0
    else:
        return a * ((1-(r**n))/(1-r))

def gsf(a,r,n):
    sum = 0
    for i in range(0, n):
        sum += (r**i)
    return a * sum

def g(a,r,n):
    if n <= 0:
        return 0
    else:
        return a*(r**(n-1)) + g(a,r,n-1)

def B(n):
    if n == 0:
        return 5
    elif n == 1:
        return 10
    else:
        return (5*n) + B(n-1)

def Bt(n,v=0):
    if n == 0:
        return v + 5
    elif n == 1:
        return v + 10
    else:
        return Bt(n-1, (5*n)+v)


def x(n):
    if n == 0:
        return 3
    elif n%2:
        return 2*n + x(n-1)
    else:
        return 2*n + 1 + x(n-1)

def xt(n,v=3):
    if n == 0:
        return v
    elif n%2:
        return xt(n-1, 2*n + v)
    else:
        return xt(n-1, 2*n + 1 + v)



#LOOP
#INPUT any interable
#RETURN length
def length_l(x_iterable):
    lenSum = 0
    for i in x_iterable:
        lenSum += 1
    return lenSum
#RECURSIVE
#INPUT any iterable
#RETURN length

def length_r(x_iterable):

    if x_iterable:
        return 1 + length_r([x for x in range(1,len(x_iterable))])

    else: 
        return 0

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    # print("~"*20 + "Problem 1" + "~"*20 + "\n")
    # print("The next 3 lines are calls for F and Ft")
    #print(F(5,5,5),Ft(5,5,5))
    #print(F(1,2,3),Ft(1,2,3))
    #print(F(5,4,2),Ft(5,4,2))
    #print("The next 5 lines are calls for B and Bt")
    #for i in range(5):
    #   print(B(i), Bt(i))
    # print("The next 3 lines are for gsf, g, and gsf_close, respectively")
    #print(gsf(2,3,5))
    #print(g(2,3,5))
    #print(gsf_close(2,3,5))
    # print("The next 5 lines are for x and xt")
    #for i in range(5):
     #   print(x(i),xt(i))

    #xlst = [[1,2,3], "123", (1,2,3), {1,2,3}, {1:1, 2:2, 3:3}]
    #for i in xlst:
    #    print(f"Loop: {i} has length {length_l(i)}")
     #   print(f"Rec: {i} has length {length_r(i)}")

###########################################################################
# Problem 2
###########################################################################

d,c = "d","c"
def bk(xbook):
    debit = 0
    credit = 0
    for i in xbook:
        if i[0] == d:
            debit += i[1]
        else:
            credit += i[1]
    return debit == credit

#hint local recursive function might make this easier
def bkr(xbook, sum=0):
    if xbook:
        if xbook[0][0] == d:
            return bkr(xbook[1:], sum + xbook[0][1])
        else:
            return bkr(xbook[1:], sum - xbook[0][1])
    else:
        return not sum

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    # print("\n" * 3 + "~"*20 + "Problem 2" + "~"*20 + "\n")
    # d,c = "d","c"
    #xbook1 = [[d, 895],[c,7500],[d,339],[c,234],[d,6400],[d,100]]
    #xbook2 = [[d, 95],[c,500],[d,39],[c,234],[d,600],[d,10]]
    #print(bkr(xbook1))
    #print(bkr(xbook2))
    #print(bk(xbook1))
    #print(bk(xbook2))



###########################################################################
# Problem 3
###########################################################################


def div_9(x):
    if type(x) != int:
        return False
    def getSingleDigit(y):
        if y >= 10:
            temp = list(str(y))
            sumTot = 0
            for i in temp:
                sumTot += int(i)
            return getSingleDigit(sumTot)
        else:
            return y
    newX = getSingleDigit(x)
    if newX == 9 or x == 0:
        return True
    else:
        return False       
  
if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    #print("\n" * 3 + "~"*20 + "Problem 3" + "~"*20 + "\n")
    #xlst = [99,0,18273645,22,27]
    #print("The next " + str(len(xlst)) + " lines are calls to div_9")
    #for i in xlst:
    #    print(div_9(i))




###########################################################################
# Problem 4
###########################################################################
xs = ["", "I","II","III","IV", "V","VI","VII","VIII", "IX"]
yd = ["", "X","XX","XXX","XL", "L", "LX","LXX","LXXX","XC","C"]

#INPUT positive integer 1-100
#RETURN roman numeral equivalent
dictNum = {1:"I", 4: "IV", 5:"V", 9: "IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C"}
specialDict = {"IIII": "IV", "XXXX": "XV", "VIIII": "IX", "LXXXX" : "XC"}
iterList = [100, 90, 50, 40, 10, 9, 5, 4, 1]
def cicero(epectitus):
    if type(epectitus) != int:
        return epectitus
    strRet = ""
    while epectitus:
        for i in iterList:
            if epectitus >= i:
                epectitus -= i
                strRet += dictNum[i]
                break
    return strRet


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    #print("\n" * 3 + "~"*20 + "Problem 4" + "~"*20 + "\n")
    #for i in range(1,101):
    #    print("{0:<3} {1:<8}".format(i,cicero(i)),"   ", end="")
    #    if i % 5 == 0:
    #        print()

###########################################################################
# Problem 5
###########################################################################


#Make it easier to type 
A,C,T,G = 'A','C','T','G'

def make_pairing(xseq):
    retSet = ""
    for i in xseq:
        if i == A:
            retSet += T
        elif i == T:
            retSet += A
        elif i == C:
            retSet += G
        else:
            retSet += C
    return retSet

pair1,pair2 = {A, T}, {G, C}
def findError(s1,s2):
    temp = []
    retSet = ""
    for i in range(0, len(s1)):
        temp += [{s1[i], s2[i]}]
    for j in temp:
        if j == pair1 or j == pair2:
            retSet += "-"
        else:
            retSet += "*"
    return retSet
        




if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    print("\n" * 3 + "~"*20 + "Problem 5" + "~"*20 + "\n")
    
    s1 = "ATCGATTGAGCTCTAGCG"
    s2 = "TAGCTAACTCGAGATCGC"
    s3 = "TAACGAACTGGAGACCGC"
    answer = "--*-*----*----*---"

    print("The next line is a call to make_pairing")
    print("{0}\n{1}".format(s1,make_pairing(s1)))
    print(s2 == make_pairing(s1))
    print()
    print("The next line is a call to findError")
    print("{0}\n{1}\n{2}".format(s1,s3,findError(s1,s3)))



###########################################################################
# Problem 6
###########################################################################

#INPUT positive integer 2,3,...
#RETURN list of primes 

def primes(n):
    if n < 2:
        return []
    def findPrime(xList, pList=[]):
        nextList = []
        if xList == []:
            return pList
        else:
            pList += [xList[0]]
            for i in xList:
                if i % xList[0] != 0:
                    nextList += [i]
            return findPrime(nextList, pList)
        
    return findPrime(range(2,n+1))

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    print("\n" * 3 + "~"*20 + "Problem 6" + "~"*20 + "\n")
    
    print(f"Primes to 20: {primes(20)}")
    print(f"Primes to 2: {primes(2)}")
    print(f"Primes to 3: {primes(3)}")
    print(f"Primes to 23: {primes(23)}")
    

###########################################################################
# Extra Tests
###########################################################################

if __name__ == "__main__":
    """
    Feel free to add any tests below you want to try

    (Make sure you indent so it is inside of this if statement)
    """
    pass
