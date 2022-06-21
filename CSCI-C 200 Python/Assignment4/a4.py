import math

if __name__ == "__main__":
    print()
    print("Currently running `a4.py`")
    print("The output presented here is just extra print information; the output you see in the terminal is for reference—not for final grading")
    print("To determine if functions work properly, refer to the testing file")

#####################################################################################################
#PROBLEM ONE
#####################################################################################################

#INPUT non-negative integer n
#RETURN string of * that, when printed,
# is a block
# if n = 0, then return ""
def block(n):
    if n == 0:
        return ""
    ret = ("*" * n) + "\n"
    ret *= n
    return ret

#INPUT non-negative integer n
#RETURN string of * that, when printed,
# is an outline 
# if n = 0, then return ""
def square(n):
    ret = ("*" * n) + "\n"
    ret += (("*" + (" " * (n - 2)) + "*") + "\n") * (n - 2)
    ret += ("*" * n) + "\n"
    if n == 0:
        return ""
    if n == 1:
        ret = "*\n"
    return ret


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 1")
    for i in range(5):
        print("Block of size {0}".format(i))
        print(block(i))
    

    for i in range(5):
        print("Square of size {0}".format(i))
        print(square(i))
   

#####################################################################################################
#PROBLEM 2
#####################################################################################################

#DATA
## DO NOT CHANGE THESE VARIABLES MANUALLY
act, Au,Ag,Pd,Pt ="act", "gold", "silver", "paladium", "platinum"
spot_price = {Au:1833.15, Ag:27.61, Pt:1275.20, Pd: 2426.60}
portfolio = {act: 10000}
portfolio["holdings"] = {Au:(0,0), Ag:(0,0), Pt:(0,0), Pd: (0,0)}

#INPUT portfolio, metal, and number of ounces of metal
#RETURN True or False
#True: transaction has been made
#False: transaction has not been made  
def purchase(portfolio, metal, amt):
    buyPrice = spot_price[metal] * amt
    if buyPrice > portfolio[act]:
        return False
    portfolio[act] -= (buyPrice)
    newTup = ((portfolio["holdings"][metal][0] + amt),(portfolio["holdings"][metal][1] + buyPrice))
    portfolio["holdings"][metal] = newTup
    return True




#INPUT portfolio and metal
#RETURN non-negative integer of number of ounces
#that can be purchased
def how_much(porfolio, metal):
    if spot_price[metal] > porfolio[act]:
        return False
    return porfolio[act]//spot_price[metal]
    

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 2")
    print(purchase(portfolio,Au, 1))
    print(portfolio)
    print(purchase(portfolio,Au, 1000))
    print(portfolio)

    purchase(portfolio,Au, 2)
    purchase(portfolio,Ag,3)
    purchase(portfolio,Pt,2)
    print(portfolio)
    print(how_much(portfolio, Pd))

#####################################################################################################
#PROBLEM 3
#####################################################################################################

#INPUT a possibly empty list of numbers
#RETURN the smallest number and the number of times
#it occurs in the list
def find_num_min(xlst):
    if xlst == []:
        return ()
    
    currLow = xlst[0]
    lowCount = 0

    for i in xlst:
        if i < currLow:
            currLow = i
            lowCount = 1
        elif i == currLow:
            lowCount += 1
    return (currLow,lowCount)
    


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 3")
    x1 = []
    x2 = [1,0,0,1]
    x3 = [1,2,3,4,0]
    x4 = [5]
    x5 = [-1,0,2,2,0,-1]

    x = [x1,x2,x3,x4,x5]
    for i in x:
        print(find_num_min(i))

#####################################################################################################
#PROBLEM 4
#####################################################################################################
#Solving cryptarithms

#INPUT None
#RETURN list of all possible solutions
def search_me_me_bee():
    retList = []
    for m in range(10):
        for e in range(10):
            for b in range(10):
                if (((m*10)+e)*2) == ((b*100)+(e*10)+e) and (m+b+e) > 0:
                    retList += [['M', m], ['E', e], ['B', b]]
    return retList

#INPUT None
#RETURN list of all possible solutions
def search_go_to_out():
    retList = []
    for t in range(10):
        for o in range(10):
            for g in range(10):
                for u in range(10):
                    if ((t*10)+o)+((g*10)+o) == ((o*100)+(u*10)+t) and (t+o+g+u) > 0:
                        newList = [['T',t], ['O',o], ['G',g], ['U',u]]
                        retList += [newList]
    return retList


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 4")
    print(search_me_me_bee())
    print(search_go_to_out()) 

#####################################################################################################
#PROBLEM 5
#####################################################################################################

#INPUT a (possibly empty) list of integers
#RETURN the length of the longest monotonic sequence
def increase(xlst):
    if xlst == []:
        return 0
    
    currentSequence = 0
    longestSequence = 0
    
    for i in range(len(xlst)-1):
        if xlst[i] < xlst[i+1] or xlst[i] == xlst[i+1]:
            currentSequence += 1
        elif xlst[i] > xlst[i+1]:
            currentSequence = 0
        if longestSequence <= currentSequence:
            longestSequence = currentSequence
        
    return longestSequence
        #if sequence follows 



if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 5")
    x1 = [0,1,2,2,3,1,2,3,1,1,0,1]
    x2 = [1,2,3,4,5,0,1,1,1,1,1,1,1,1]
    x3 = [1,2,3,4,5,1]
    x4 = [5,4,3,2,1]
    xlst = [x1,x2,x3,x4, []]
    for i in xlst:
        print("Longest monotonic sequence in {0}: \n{1}".format(i,increase(i)))

#####################################################################################################
#PROBLEM 6
#####################################################################################################

#INPUT string of containing only letters, spaces, comma, and period
#RETURN a dictionary that gives the count of each letter
def letter_count(text):
    justLettersText = ""
    for i in text:
        if i != " " and i != "," and i != ".":
            justLettersText += str.lower(i)
    letterList = {}
    for i in justLettersText:
        if i in letterList:
            letterList[i] += 1
        else:
            letterList[i] = 1
    return letterList

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 6")
    f ="Two roads diverged in a yellow wood,\
        And sorry I could not travel both\
        And be one traveler, long I stood\
        And looked down one as far as I could\
        To where it bent in the undergrowth"
    g = "the quick brown fox jumped over the lazy dog"
    print(letter_count(f))
    print(letter_count(g))

#####################################################################################################
#PROBLEM 7
#####################################################################################################

#INPUT two vectors of same length
#RETURN dot product
def dot_prod(x,y):
    z = []
    retSum = 0
    for i in range(len(x)):
        z += [x[i]*y[i]]
    for i in range(len(z)):
        retSum += z[i]
    return retSum

#INPUT vector and scalar
#RETURN vector 
def scalar_vec(x,n):
    ans = []
    for i in (range(len(x))):
        ans += [x[i]*n]
    return ans

#INPUT vector
#RETURN non-negative scalar (float or real)
def euc_len(x):
    z = []
    for i in range(len(x)):
        z += [x[i]*x[i]]
    sqrtSum = 0
    for i in range(len(z)):
        sqrtSum += z[i]
    return math.sqrt(sqrtSum)

#INPUT two vectors
#RETURN the angle in DEGREES between 
def ang_vec(x,y):
    ans = (dot_prod(x,y)/(euc_len(x)*euc_len(y)))
    ans = math.acos(ans)
    return math.degrees(ans)

#INPUT vector
#RETURN uni vector
def unit_vec(x):
    z = []
    euLen = (1/euc_len(x))
    for i in range(len(x)):
        z += [euLen*x[i]]
    return  z
    

#INPUT two vectors and either "+" or "-"
#RETURN sum or difference of vectors
def vec_op(x,y,op):
    ans = []
    if op == "+":
        for i in (range(len(x))):
            ans += [x[i]+y[i]]
    else:
        for i in (range(len(x))):
            ans += [x[i]-y[i]]
    return ans



if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 7")
    # Vectors
    x = [4,3]
    y = [3,5]

    print(vec_op(x,y,"+"))
    print(vec_op(x,y,"-"))
    print(dot_prod(x,y))
    print(scalar_vec(x,1/5))
    print(euc_len(x))
    print(euc_len(y))
    print(ang_vec(x,y))
    print(unit_vec(x))
    print(euc_len(unit_vec(x)))


#####################################################################################################
#PROBLEM 8
#####################################################################################################

# https://www.michigan.gov/documents/dnr/TreeAge_401065_7.pdf

def tree_age(circumferance, bark, growth_rate):
    radius = (circumferance[0] * 12) + circumferance[1]
    radius /= 2 * math.pi
    radius -= bark
    return math.floor(radius/growth_rate)


def noninvasive_tree_age(circumferance, tree):
    growthRate = {"White Oak":5.0, "Red Oak":4.0, "Pin Oak":3.0, "Linden":3, "Basswood":3.0}
    radius = (circumferance[0] * 12) + circumferance[1]
    radius /= 2 * math.pi
    return math.ceil(radius*growthRate[tree])

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 8")
    print("\ttree_age")
    print(tree_age([12,10], .5, .2))
    print(tree_age([1,1],0,.3))
    print("\tnoninvasive_tree_age")
    print(noninvasive_tree_age([12,10], "White Oak"))
    print(noninvasive_tree_age([5, 5], "Red Oak"))


#####################################################################################################
#PROBLEM 9
#####################################################################################################

#INPUT list of int, str, set, tuple, lists...
#RETURN list of unique values in list
#REQUIREMENTS cannot use Python set or set functions
#Can use in predicate
def make_unique(xlst):
    if xlst == []:
        return []
    uniqueList = []
    for i in xlst:
        if i in uniqueList:
            1 == 1
        else:
            uniqueList += [i]
    return uniqueList



#INPUT list and size
#RETURN returns a list of list of size
#if there is left over that's less than
#size, then make the a list
def partition(xlst, size):
    if len(xlst) == 0 or size == 0:
        return []
    partList = []

    if len(xlst) % size == 0:
        for i in xlst[0::size]:
            partList += [xlst[i-1:size+i-1]]
    else:
        rem = len(xlst) % size
        leng = len(xlst) - rem
        for i in xlst[0:leng:size]:
            partList += [xlst[i-1:size+i-1]]
        partList += [xlst[(rem*-1):]]

    return partList

#INPUT list and object
#RETURN all the locations of object in the list
#REQUIREMENTS Cannot use any list functions
def occurs_at_index(xlst, item):
    if len(xlst) == 0:
        return []
    indexList = []
    for i in range(len(xlst)):
        if xlst[i] == item:
            indexList += [i]
    return indexList



#INPUT two lists x,y
#RETURN list of *unique* objects that belong to both lists
#REQUIREMENTS cannot use Python set, set functions
def intersect(xlst, ylst):
    if len(xlst) == 0 or len(ylst) == 0:
        return []
    intersect = []
    for i in range(len(xlst)):
        for j in range(len(ylst)):
            if xlst[i] == ylst[j] and (xlst[i] not in intersect):
                intersect += [xlst[i]]
    return intersect


#INPUT list of numbers and int 0,1
#RETURN if int is 0, then find minimum
#if int is 1, then find maximum
#REQUIREMENTS cannot use Python max, min
#ERROR if list is empty, return []
def optimum(xlst,s):
    if len(xlst) == 0:
        return []
    if (s):
        maxNum = xlst[0]
        for i in xlst:
            if i > maxNum:
                maxNum = i
        return maxNum
    else:
        minNum = xlst[0]
        for i in xlst:
            if i < minNum:
                minNum = i
        return minNum

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 9")
    print("\tmake_unique")
    x1 = [1,0,1,0,"dog", "cat", "cat", (1,),(1,),(2,)]
    x2 = [[],[],"","",(),()]
    print(make_unique(x1))
    x3 = []
    print(make_unique(x2))
    print(make_unique(x3))
    print("\tpartition")
    print(partition([1,2,3,4],0))
    print(partition([1,2,3,4],2))
    print(partition([1,2,3,4],1))
    print(partition([1,2,3,4],3))
    print(partition([1,2,3,4],4))
    print(partition([1,2,3,4],5))
    print("\toccurs_at_index")
    print(occurs_at_index([0,1,0,1,1],1))
    print(occurs_at_index([0,1,0,1,1],2))
    print(occurs_at_index([0,1,0,1,1],0))
    print("\tintersect")
    print(intersect([],[1]))
    print(intersect([2],[]))
    print(intersect([1,1],[1,1,2]))
    print(intersect([2,1,2,3],[3,1,3]))
    print("\toptimum")
    print(optimum([],0))
    print(optimum([],1))
    print(optimum([1],0))
    print(optimum([1],1))
    print(optimum([1,1,-1,100,-100],0))
    print(optimum([1,1,-1,100,-100],1))


#####################################################################################################
#PROBLEM 10
#####################################################################################################

#INPUT list of numbers 
#RETURN sum
def sigma(xlst):
    if len(xlst) == 0:
        return []
    sumX = 0
    for i in xlst:
        sumX+= i
    return sumX


#INPUT list of numbers
#RETURN sum of the squares
def sigma_square(xlst):
    if len(xlst) == 0:
        return []
    sumX = 0
    for i in xlst:
        sumX+= (i*i)
    return sumX


#INPUT list of pairs of numbers [[x0,y0],[x1,y1],...,[xn,yn]]
#RETURN sum of the products x0*y0+x1*y1+...+xn*yn
#If list is empty, return []
def sigma_product(xlst,ylst):
    if len(xlst) == 0 or len(ylst) == 0:
        return []
    sumX = 0
    for i in range(len(xlst)):
        sumX+= (xlst[i]*ylst[i])
    return sumX


#INPUT takes a list of lists
#RETURN returns list of slices [0:1], [1:2], ...
#of each list
#The ORDER of the ouput is critical -- look at the
#unit test please
def separate(xlst):
    if len(xlst) == 0 or len(xlst[0]) == 0:
        return []
    retList = []
    loopList = []
    for j in range(len(xlst[0])):
        for i in range(len(xlst)):
            loopList += [xlst[i][j]]
        retList += [loopList]
        loopList = []
    return retList




#INPUT coefficents and input value to linear function
#RETURN predicted value
def linear_model(a,b,x):
    return a*x + b

#INPUT list of pairs d = [[x0,y0], [x1,y1], ... ]
#RETURN coefficients a,b as a tuple to 
#linear function f(x) = ax + b
def make_linear(xlst):
    xVals, yVals = separate(xlst)
    n = len(xVals)
    a = (((n*(sigma_product(xVals,yVals)))-(sigma(xVals)*sigma(yVals)))/((n*(sigma_square(xVals))) - (sigma(xVals)**2)))
    b = ((sigma(yVals)*sigma_square(xVals))-(sigma(xVals)*sigma_product(xVals,yVals)))/((n*sigma_square(xVals))-(sigma(xVals)**2))
    return a,b


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 10")
    print("\tsigma")
    print(sigma([]))
    print(sigma([1,2,-3,3]))
    print(sigma([100,10,1]))
    print("\tsigma_square")
    print(sigma_square([]))
    print(sigma_square([-1,1,1]))
    print(sigma_square([10,2,3]))
    print("\tsigma_product")
    print(sigma_product([1,2,3],[1,10,100]))
    print(sigma_product([-1,-2,3],[9,0,3]))
    print(sigma_product([],[]))
    print("\tseparate")
    print(separate([]))
    print(separate([[1],[2],[3],[4],[5]]))
    print(separate([[1,10],[2,20]]))
    print(separate([[1,10,100],[2,20,200],[3,30,300]]))
    print(separate([[1,1],[2,3],[4,3],[3,2],[5,5]]))


    print("** To see plot uncomment the lines below **")

    # d1 = [[43,99],[21,65],[25,79],[42,75],[57,87],[59,81]]
    # d2 = [[1,1],[2,3],[4,3],[3,2],[5,5]]

    # x,y = separate(d1)
    # print(x)
    # print(y)
    # a,b = make_linear(d1)
    # print(a,b)
    # x,y = separate(d2)
    # print(x)
    # print(y)
    # a,b = make_linear(d2)
    # print(a,b)

    # #Code to visualize data
    # #BEGIN
    # import matplotlib.pyplot as plt

    # x,y = separate(d2)

    # #plot data and line
    # x1 = list(range(1,6))
    # y1 = []
    # for i in x1:
    #     y1 += [linear_model(a,b,i)]
    # plt.scatter(x,y,color="red")
    # plt.plot(x1,y1)

    # #plot predicted points
    # for i in x:
    #     plt.scatter(i,linear_model(a,b,i),color="green")

    # #plot residuals
    # for i,j in d2:
    #     plt.plot([i,i],[j,linear_model(a,b,i)], linestyle =(0, (1, 1)), color="black" )

    # #text on plot   
    # plt.text(3.2,2.27,r"residuals $|y - f(x)|$")
    # plt.ylabel(r"$f(x) = {0}x + {1}$".format(a,b))
    # plt.xlabel('x')
    # plt.title("Linear Model")

    # #render to display
    # plt.show()

    # #END

#####################################################################################################
#PROBLEM 11
#####################################################################################################

#INPUT either list, string, or tuple
#RETURN reverse list, string, or tuple
#REQUIREMENTS cannot use slicing 
#to reverse string
#if the iterable is a number DD0..0, then the
#return discards the leading zeros DD
def reverse(x):
    firstX = str(x)
    firstX = firstX.strip("(), ")
    badChars = ' (),[]0'
    newX = []
    for i in firstX:
        if i in badChars:
            pass
        else:
            newX += [i]
    retX = ""
    for i in range(len(newX), 0, -1):
        retX += newX[i-1]
    if type(x) == str:
        return str(retX)
    if type(x) == int:
        return int(retX)
    if type(x) == tuple:
        realNewX = ()
        for i in retX:
            realNewX += (int(i),)
        return realNewX
    else:
        realNewX = []
        for i in retX:
            realNewX += [int(i)]
        return realNewX
    


#INPUT take a string
#RETURN True if the string is palindrome, False otherwise
#REQUIREMENTS treat letters as all lower case
#remove space, comma, period, question mark, exclamation
#point
def palindrome(x):
    badChars = ' ,.?!'
    newX = []
    for i in x:
        if i in badChars:
            pass
        else:
            newX += [i]
    retX = ""
    for i in newX:
        retX += str(i)
    retX = retX.lower()
    if retX == reverse(retX):
        return True
    else:
        return False


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 11")
    print("\treverse")
    xtest = ["abc", 120, (1,2,3), [1,2,3]]

    for i in xtest:
        print(reverse(i))

    print("\tpalindrome")
    xlst = ["Step on no pets.", "Was it a cat I saw?", "A",\
            "Eva, can I see bees in a cave?", "Uhh...", "Oreos yum!"]

    for i in xlst:
        print(palindrome(i))
