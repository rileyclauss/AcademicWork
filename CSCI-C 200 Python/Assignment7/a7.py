###############
# PROBLEM ONE
###############

def d(n):
    return 1 if n == 0 else 3*d(n-1) + 1

def cr(n,m):
    if m == 0 or n == m:
        return 1
    else:
        return cr(n-1, m) + cr(n-1, m-1)

def B(n):
    if n == 0.0:
        return 1.0
    elif n == 1.0:
        return -0.5
    elif n == 2.0:
        return 0.5/3
    elif n == 3.0:
        return 0.0
    else:
        return (-1 * sum([cr(n+1, i) * B(i) for i in range(n)]))/(1+n)
        

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """
    #for i in range(5):
    #    print("d({0}) = {1}".format(i,d(i)))

    #for i in range(1,5):
    #    for j in range(i):
    #        print("cr({0},{1}) = {2}".format(i,j,cr(i,j)))
    
    #for i in range(6):
    #    print("B({0}) = {1}".format(i,B(i)))

###############
# PROBLEM TWO
###############
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def get_data(path,name):
    tmp = []
    pn = path + "/" + name
    file = open(pn, "r")
    for d in file:
        x,y = d.split(",")
        tmp += [[int(x), int(y)]]
    print(tmp)
    return tmp


def pop(year):
    return 1436.53 * (1.01395**year)

def error(data):
    return (100/len(data) * sum([(abs(data[i][1] - pop(data[i][0]))/data[i][1]) for i in range(0, len(data))]))



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """

    #data = get_data("Assignment7", "pop.txt")
    #total_error = round(error(data),4)

    #t = np.arange(0.0, 120.0)
    #fig,ax = plt.subplots()

    #ax.plot(t, pop(t),'g')
    #for y,p in data:
    #    ax.plot(y,p,'ro--')

    #ax.set(xlabel ="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    #title = "Population Growth. Total ave error = %{0}".format(total_error))
    #ax.grid()
    #plt.show()

###############
# PROBLEM THREE
###############

#recursive
def a(n):
    if type(n) == int:
        return 1 if n == 0 else a(n-1) + (n*((-1) ** n))
    else:
        return 0

#bottom-up memoization
d_a = {0:1}

def am(n):
    if n not in d_a.keys():
        d_a[n] = am(n-1) + (n*((-1)**n))
    return d_a[n]



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    # """
    #for i in range(0,6):
    #    print("a({0}) = {1},{2}".format(i,a(i),am(i)))

###############
# PROBLEM FOUR
###############
import csv

def my_int(xstr):
    if xstr == "":
        return 0
    else:
        return int(xstr)
        
#INPUT state and state dictionary of data
#RETURN give the total confirmed deaths for 
# entire state
def scd(state,dic):
    sumNum = 0
    for i in dic:
        if state in i:
            sumNum += my_int(dic[i][1])
    return sumNum

#INPUT dictionary data and interval (a,b)
#RETURN all confirmed county cases greater than or equal to a
#and strictly less than b
def ccc(dic,interval):
    retDict = {}
    sumNum = 0
    for i in dic:
        if my_int(dic[i][0]) >= interval[0] and my_int(dic[i][0]) < interval[1]:
            retDict[i[0]] = dic[i][0]
            sumNum += 1
    retDict[interval] = sumNum
    return retDict

#INPUT state, data dictionary, state population
#RETURN state death density: confirmed deaths / population of state
#as a percentage to 3 places use round(x*100,3)
def sdd(state, dic,state_pop):
    sumNum = 0
    for i in dic:
        if state in i:
            sumNum += my_int(dic[i][1])
    return round((sumNum/my_int(state_pop[state])) * 100, 3)

#INPUT data dictionary and state population 
#RETURN return the entire US death density
def usdd(dic,state_pop):
    
    usDict = {}
    for i in dic:
        if i[0] in state_pop:
            usDict[i[0]] = sdd(i[0], dic, state_pop)
        else:
            usDict[i[0]] = 0
    return usDict

def get_dic(file_path):
    """
    Reading from the file passed in, 
    extract the following information into a dictionary and RETURN a dictionary. 

    The key for the dictionary (also described in the document): a tuple
    The value for each key (also described in the document): a list of size 2 (both need to be integers)

    To read the file, you can do it the way we have seen before or using csv.reader. https://docs.python.org/3/library/csv.html#csv.reader 
    If you want to do it another way, please ask before attempting to use a method not talked about in class.

    HINT: You will need to skip the first row. 
            If you use a CSV reader, you can skip a row by doing `next(reader, None)`
    """
    retDict = {}
    file = open(file_path, "r")
    stateData = []
    for l in file:
        stateData += [l.split(',')]
    stateData = cleanZeroes(stateData[1:])
    for i in range(len(stateData)):
        retDict[(stateData[i][2], stateData[i][1])] = [stateData[i][6], stateData[i][7]]
    return retDict

def get_state_pop(file_path):
    """
    Reading from the file passed in, 
    extract the following information into a dictionary and RETURN a dictionary. 

    The key for the dictionary (also described in the document): a string
    The value for each key (also described in the document): an integer

    To read the file, you can do it the way we have seen before or using csv.reader. https://docs.python.org/3/library/csv.html#csv.reader 
    If you want to do it another way, please ask before attempting to use a method not talked about in class.
    """
    retDict = {}
    file = open(file_path, "r")
    stateLines = []
    for l in file:
        stateLines += [l.split(',')]
    stateLines = clean(stateLines)
    for i in range(len(stateLines)):
        retDict[stateLines[i][0]] = stateLines[i][len(stateLines[i]) - 1]
    return retDict

def clean(xLst):
    for i in range(len(xLst)):
        for j in range(len(xLst[i])):
            xLst[i][j] = xLst[i][j].strip()
        xLst[i] = [k for k in xLst[i] if k] #Remove empty elements from sublists
    xLst = [i for i in xLst if i]  #Remove empty sublists from list
    return xLst

def cleanZeroes(xLst):
    for i in range(len(xLst)):
        for j in range(len(xLst[i])):
            xLst[i][j] = xLst[i][j].strip()
        xLst[i] = [(k if k else 0) for k in xLst[i]] #Remove empty elements from sublists
    xLst = [i for i in xLst if i]  #Remove empty sublists from list
    return xLst

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    # """

    #Our solutions used these two dictionaries 
    # has state, county, confirmed case, comfirmed deaths 
    # has state *most* current population 
    #dic = get_dic("Assignment7/us-counties.csv")
    #state_pop = get_state_pop("Assignment7/sp.csv")

    #county confirmed cases
    #intervals = [(0,1),(1,2),(0,2)]
    #c0 = ccc(dic,intervals[0])
    #c1 = ccc(dic,intervals[1])
    #c2 = ccc(dic,intervals[2])
    #print(f"Number of state-counties {intervals[0]} is {c0[intervals[0]]}")
    #print(f"Number of state-counties {intervals[1]} is {c1[intervals[1]]}")
    #print(f"Number of state-counties {intervals[2]} is {c2[intervals[2]]}")
    #max = float('inf')
    #cm = ccc(dic,(266380,max))
    #print(">= 266380 confirmed cases")
    #print(cm)

    #state confirmed deaths
    #print(f"Alabama: {scd('Alabama', dic)}")
    #print(f"Alabama state pop: {state_pop['Alabama']}")
    #print(f"Alabama death density: {sdd('Alabama', dic, state_pop)}%")
    #print(f"{round((8166 / 4903185)*100, 3)}%")

    #entire country death density percentage
    #x = usdd(dic,state_pop)
    #print(f"Alabama: {x['Alabama']}%")
    #print(x["Texas"])



###############
# PROBLEM FIVE
###############
#You cannot simply divide or use modulus
#You must implement the algorithm as described
def div_11(n):
    if not n or not type(n) == int:
        return False
    xlst = [i for i in str(n)]
    sumBool = 1
    sumNum = 0
    for i in xlst:
        sumNum += my_int(i) * sumBool
        sumBool *= -1
    return (sumNum == 11 or sumNum == -11 or not sumNum)


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """

    #nlst = [587657752,11,22,2728,31415,1358016]

    #for n in nlst:
    #    print(div_11(n))

