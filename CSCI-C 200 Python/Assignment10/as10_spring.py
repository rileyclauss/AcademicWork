########################
#Problem One
########################

class Binary:

    def __init__(self, value = 0):
        res = ""
        negative = False
        if value == 0:
            res = "0"
        if value < 0:
            negative = True
        value = abs(value)
        while value != 0 and value != -1:
            res = f"{value % 2}" + res
            value = value // 2
        if negative:
            res = "-" + res
        self.binary = f"b{res}"
        
    def __str__(self):
        return self.binary

    def b_to_d(self):
        negative = 1
        if self.binary[1] == "-":
            negative = -1
            value = self.binary[2:]
        else:
            value = self.binary[1:]
        power = 0
        retVal = 0
        for i in sorted(range(len(value)), reverse=True):
            if value[i] == "1":
                retVal += 2**power
            power += 1
        return retVal * negative

    def d_to_b(self,v):
        res = ""
        negative = False
        if v == 0:
            res = "0"
        if v < 0:
            negative = True
        v = abs(v)
        while v != 0 and v != -1:
            res = f"{v % 2}" + res
            v = v // 2
        if negative:
            res = "-" + res
        return f"b{res}"

    def __add__(self, other):
        if type(self) == Binary and type(other) == Binary:
            resVal = Binary(self.b_to_d() + other.b_to_d())
            return resVal
        else:
            return None

    def __sub__(self,other):
        if type(self) == Binary and type(other) == Binary:
            resVal = Binary(self.b_to_d() - other.b_to_d())
            return resVal
        else:
            return None    

    def __mul__(self,other):
        if type(self) == Binary and type(other) == Binary:
            resVal = Binary(self.b_to_d() * other.b_to_d())
            return resVal
        else:
            return None 

    def __neg__(self):
        if self.binary[1] == '-':
            self.binary = self.binary[0] + self.binary[2:]
        else:
            self.binary = self.binary[0] + "-" + self.binary[1:]
        return self
    def localBtoD(self, me):
        power = 0
        negative = 1
        if me[1] == '-':
            negative = -1
        decVal = 0
        for i in sorted(range(len(me)), reverse=True):
            if me[i] == "1":
                decVal += 2**power
            power += 1
        return decVal * negative
    def __abs__(self):
        if self.binary[1] == "-":
            retB = Binary(self.localBtoD(self.binary[0] + self.binary[2:]))
        else:
            return self

    def __len__(self):
        if self.binary[1] == "-":
            return len(self.binary[2:])
        else:
            return len(self.binary[1:])

    def __and__(self,other):
        selfNeg, othNeg = False, False
        if self.binary[1] == '-':
            selfNeg = True
        if other.binary[1] == '-':
            othNeg = True
        newSelf, newOther = abs(self).binary, abs(other).binary
        while len(newSelf) < len(newOther):
            newSelf = newSelf[0] + '0' + newSelf[1:]
        while len(newOther) < len(newSelf):
            newOther = newOther[0] + '0' + newOther[1:]
        retVal = 'b'
        for i in range(1, len(newSelf)):
            if newSelf[i] == '1' and newOther[i] == '1':
                retVal += '1'
            else:
                retVal += '0'
        unchecked = True
        while unchecked:
            if retVal[1] == '0':
                retVal = retVal[0] + retVal[2:]
            else:
                unchecked = False
        return Binary(self.localBtoD(retVal))
    
    #free :)
    def __eq__(self, other):
        return self.b_to_d() == other.b_to_d()

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a10.py`. Feel free to add print statements. 
#   # """
#   print("~"*30)
#   print("Problem 1")
#   print("~"*30)
#   x = Binary(7)
#   y = Binary(1)
#   z = x + y
#   u = x & y
#   print(x,y,u)
#   print(z,z.b_to_d())
#   -z
#   print(z,z.b_to_d())
#   w = y - x
#   print(w)
#   print(len(w))
#   v = x - y
#   print(v)
#   t = v * Binary(2)
#   print(t)
#   print(len(Binary(7)))
#   print(len(Binary(1)))
#   abc = Binary(8)
#   print(abc)
#   print(len(abc))
#   -abc
#   print(abc)
#   print(len(abc))
#
#   for i in range(16):
#       x = Binary(i)
#       print(i,x)


########################
#Problem Two
########################

#change lat,lon to radians
from math import radians, sin, cos, sqrt, asin 

#INPUT two tuples that have lat, lon values
#RETURN distance in miles
def hd(loc1,loc2):
    latD = (loc2[0] - loc1[0])/2
    lonD = (loc2[1] - loc1[1])/2
    dist = sin(radians(latD))**2 + (cos(radians(loc1[0]))*cos(radians(loc2[0]))*(sin(radians(lonD))**2))
    return 2 * (3961) * asin(sqrt(dist))

def dd(loc1,loc2):
    """
    Standard distance formula
    """
    lat1,lon1 = loc1
    lat2,lon2 = loc2
    x = lat1 - lat2
    y = (lon1 - lon2)*cos(radians(lat2))
    return 69.385*sqrt(x**2 + y**2)

def eu_distance(loc1,loc2):
    """
    Euclidian Distance Forumula
    """
    return sqrt(sum([(i-j)**2 for i,j in zip(loc1,loc2)]))


if __name__ == "__main__":
    
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a10.py`. Feel free to add print statements. 
    # """
    print("~"*30)
    print("Problem 2")
    print("~"*30)
    #Lindley Hall where we had C200 on 
    #south side of campus
    l1 = (39.165341,-86.523588)

    #Luddy Hall the new Luddy building, where we have C200
    #on northside of campus
    l2 = (39.172725,-86.523295)

    #Distance between Lindley and Luddy
    print("haversine", hd(l1,l2), "mi")
    print("Euclidean", eu_distance(l1,l2), "mi")
    print("Approximate", dd(l1,l2), "mi")




########################
#Problem Three
########################

import matplotlib.pyplot as plt
import numpy as np

abscissa = np.arange(20)
plt.gca().set_prop_cycle('color', ['red', 'green', 'blue', 'black'])

class MyLine:

    def __init__(self, *args, **kwargs):
        if kwargs['options'] == "2pts":
            self.slope = (args[1][1] - args[0][1])/(args[1][0] - args[0][0])
            self.intercept = args[1][1] - (self.slope * args[1][0])
        elif kwargs['options'] == "point-slope":
            self.slope = args[1]
            self.intercept = (self.slope * (0 - args[0][0]) - args[0][1])
        elif kwargs['options'] == "lambda":
            if args[0].index('x') == 0:
                self.slope = 1
            else:
                listofints = []
                negative = False
                for i in range(0, args[0].index('x')):
                    if args[0][i].isdigit():
                        listofints += [args[0][i]]
                    if args[0][i] == '-':
                        negative = True
                if len(listofints) == 2:
                    self.slope = int(listofints[0])/int(listofints[1])
                else:
                    self.slope = listofints[0]
                if negative:
                    self.slope *= -1
            try:
                self.intercept = int(args[0][args[0].index('x')+3:])
            except:
                self.intercept = 0
                print(args[0][args[0].index(x)+3:])
        self.line = lambda x: (self.slope * x) + self.intercept


    def draw(self):
        plt.plot(abscissa,self.line(abscissa))
 
    def get_line(self):
        return "y = {0:.2f}x + {1:.2f}".format(self.slope, self.intercept)

    def __str__(self):
        return self.get_line()

    def __mul__(self,other):
        if other.slope == self.slope:
            return ()
        xIntercept = (self.intercept-other.intercept) / (other.slope-self.slope)
        yIntercept = self.slope * xIntercept + self.intercept
        return (xIntercept, yIntercept)

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a10.py`. Feel free to add print statements. 
    """
 #  print("~"*30)
 #  print("Problem 3")
 #  print("~"*30)
 #  x1 = MyLine((0,0), (5,5),options = "2pts")
 #  x1.draw()
 #  x2 = MyLine((5,0),-1/4, options = "point-slope")
 #  x2.draw()
 #  x3 = MyLine("(-4/5)*x + 5", options = "lambda")
 #  x3.draw()
 #  x4 = MyLine("x + 2", options = "lambda")
 #  x4.draw()

 #  print("The intersection of {0} and {1} is {2}".format(x1,x2,x1*x2))
 #  print("The intersection of {0} and {1} is {2}".format(x1,x3,x1*x3))
 #  print("The intersection of {0} and {1} is {2}".format(x1,x4,x1*x4))


 #  plt.legend([x1.get_line(), x2.get_line(), x3.get_line(),x4.get_line()], loc='upper left')
 #  plt.show()

########################
#Problem Four
########################

import matplotlib.pyplot as plt

xlst, ylst = [],[]

def f(n):
    if n % 2 == 0:
        return n//2
    else:
        return (3*n) + 1

def g(n,i):
    xlst.append(i)
    ylst.append(n)
    print(str(n)+" ", end="")
    if n == 1:
        return 1
    else:
        return g(f(n), i+1)

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a10.py`. Feel free to add print statements. 
    """
   #print("~"*30)
   #print("Problem 4")
   #print("~"*30)
   #g(26,0)
   #xmax = max(tuple(xlst))
   #ymax = max(tuple(ylst))
   #print(ylst)
   #print("\nNumber of recursive calls: {0}\nMaximum number: {1}".format(xmax,ymax))
   #plt.plot(xlst,ylst,'r--')
   #plt.axis([0,xmax,0,ymax])
   #plt.show()


########################
#Problem Five
########################


import matplotlib.pyplot as plt
import numpy as np

def get_data(path,name):
    fileO = open(path + "\\" + name, "r")
    contents = fileO.readlines()
    retList = []
    for i in contents:
        n = i.strip()
        n = n.split(',')
        n[0], n[1] = float(n[0]), float(n[1])
        retList += [n]
    fileO.close()
    return retList
def mean(lst):
    if lst == []:
        return 0
    else:
        return sum(lst)/len(lst)

def sd(xlst):
    multi = (1 / (len(xlst) - 1))
    avg = mean(xlst)
    adder = lambda x: (x - avg) ** 2
    return (multi * sum([adder(n) for n in xlst])) ** 0.5

def r(x, y):
    multi = (1/(len(x) - 1))
    sumNum = 0
    avgX, avgY = mean(x), mean(y)
    sX, sY = sd(x), sd(y)
    for i in range(len(x)):
        sumNum += ((x[i] - avgX)/sX)*((y[i] - avgY)/sY)
    return multi * sumNum


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a10.py`. Feel free to add print statements. 
    """
    print("~"*30)
    print("Problem 5")
    print("~"*30)
    data = get_data("Assignment10", "stockdata.txt")
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    correlation = r(x,y)
    print(correlation)
    # Example of creating a plot
    plt.plot(x, y, 'ro')
    t = np.arange(0,6,.1)
    plt.plot(t,t*.65 + .5,'g--')
    plt.axis([0,6,0,6])
    plt.xlabel("A values")
    plt.ylabel("B value")
    plt.title("r = {0:.3}".format(correlation))
    plt.show()

########################
#Problem Six
########################

def check_number(i,msg,low,high):
    """
    Checks that integer i is in correct range  low..high (inclusive)
    i (int) the number
    msg (str) error message fragment (one of 'Month', 'Day', or 'Year')
    low (int) low end of range
    high (int) high end of range

    returns i or raises ValueError(...)
    """
    if i >= low and i <= high:
        return i
    else:
        raise(ValueError(f"Invalid {msg} {i}"))


def parse_date(inp):
    """
    Checks that str is a valid date mm/dd/yyyy or mm-dd-yyyy
    Raises SyntaxError if form is wrong or mm, dd,
    yyyy are not digit strings with correct number 
    of digits.  
    Raises ValueError if mm, dd, yyyy are not in legal ranges 
    (checked in order mm, dd, yyyy)

    Returns (int(mm),int(dd),int(yyyy))
    """
    if '-' in inp:
        lst = inp.split('-')
    elif '/' in inp:
        lst = inp.split('/')
    else:
        raise(SyntaxError(f"Incorrect Date Syntax {inp}"))
    if len(lst[0]) + len(lst[1]) + len(lst[2]) != 8:
        raise(SyntaxError(f"Incorrect Date Syntax {inp}"))
    try:
        mm = int(lst[0])
        dd = int(lst[1])
        yyyy = int(lst[2])
    except Exception as err:
        raise(f"Invalid {err} {mm}")
    mm = check_number(mm, "Month", 1, 12)
    dd = check_number(dd, "Day", 1, 31)
    yyyy = check_number(yyyy, "Year", 1900, 2021)
    return (mm,dd,yyyy)

if __name__ == "__main__":
    print(parse_date("00/00/1800"))