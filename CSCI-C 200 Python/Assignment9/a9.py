###########################
# Problem One
###########################
# There is no unit testing 
# for this problem
###########################
import numpy as np
import matplotlib.pyplot as plt
import random as rn



#translates a random int into a step along the random walk
#parameters: int i for the step index, numpy array x for tracking the left/right location at index i,
#numpy array y for tracking the forward/backward location at index i
#return: none
def step(x,y,i):
    direction = rn.randint(1,4)
    if direction == 1:
        x[i] = x[i-1] + 1
        y[i] = y[i-1]
    elif direction == 2:
        x[i] = x[i-1] -1
        y[i] = y[i-1]
    elif direction == 3:
        x[i] = x[i-1]
        y[i] = y[i-1] + 1
    else:
        x[i] = x[i-1]
        y[i] = y[i-1] - 1
    pass

def graphit(x,y,n):
   
    plt.title("Random {0} Walk\nLast Location {1},{2}".format(n,int(x[n-1]),int(y[n-1])) )
    plt.plot(x,y) 
    plt.plot([x[1],x[1]],[y[1]-10,y[1]+10], "b-")
    plt.plot([x[1]-10,x[1]+10],[y[1],y[1]], "b-")
    plt.plot([x[n-1]-10,x[n-1]+10],[y[n-1],y[n-1]], "r-")
    plt.plot([x[n-1],x[n-1]],[y[n-1]-10,y[n-1]+10], "r-")
    plt.show() 


#if __name__ == "__main__":
#     """
#     The code in "__main__" is not being graded, but a tool for you to test 
#     your code outside of the `test_a9.py`. Feel free to add print statements. 
#     """
 #  #print("*"*30)
 #  #print("* Executing Problem 1")
 #  #print("*"*30)

 #  #number of steps
 #  n = 100000   #You should change the number of steps to see
 #              #to see how it affects the plot
 #  x = np.zeros(n) 
 #  y = np.zeros(n) 

 #  #fill array with step values 
 #  for i in range(1,n):
 #      step(x,y,i)

 #  graphit(x,y,n)


###########################
# Problem Two
###########################

#Assume this is in 2D dimension
def distance(p1,p2):
    return (((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))**0.5


def brute(xlst):
    dDict = {}
    def distanceRec(yLst):
        if yLst:
            for i in range(1, len(yLst[1:]) + 1):
                dDict[(yLst[0], yLst[i])] = distance(yLst[0], yLst[i])
                #print(yLst[0], yLst[i])
            distanceRec(yLst[1:])
    distanceRec(xlst)
    #print(dDict)
    currLow = (xlst[0], xlst[1])
    for i in dDict:
        if dDict[i] < dDict[currLow]:
            currLow = i

    return [currLow[0], currLow[1], dDict[currLow]]

 
#if __name__ == "__main__":
 #  """
 #  The code in "__main__" is not being graded, but a tool for you to test 
 #  your code outside of the `test_a9.py`. Feel free to add print statements. 
 #  """
 #  print("*"*30)
 #  print("* Problem 2")
 #  print("*"*30)

 #  x = [(rn.randint(1,50), rn.randint(1,50)) for _ in range(10)]
 #  y = [(34, 34), (28, 38), (24, 3), (18, 17), (33,33), (16,1), (32,45), (50,24), (5, 35), (48,30)]
 #  print(y)
 #  print(brute(y))


###########################
# Problem Three
###########################

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math 

def productivity(N,T = 40):
    return N * T * (0.55 - (0.00005 * N * (N-1)))


    """ 
    Do Not Change fp or newton
    """
def fp(f):
    h = .00001
    return lambda x: (f(x + h) - f(x-h))/(2*h)

def newton(f,fp,x,tau):
    def n(x):
        while f(x) > tau:
            x = x - f(x)/fp(x)
        return x
    return n(x)


#if __name__ == "__main__":
     #"""
     #The code in "__main__" is not being graded, but a tool for you to test 
     #your code outside of the `test_a9.py`. Feel free to add print statements. 
     #"""
     #print("*"*30)
     #print("* Problem 3")
     #print("*"*30)
     #f = fp(productivity)
     #x = math.ceil(newton(f,fp(f),62,.01))
     #y = math.ceil(productivity(x))

     #print("The maximum productivity is P({0}) ~ {1} person x hrs".format(x,y))
     #t = np.arange(0.0, 100.0)
     #fig,ax = plt.subplots()
     #ax.plot(t, productivity(t),'g')
     #ax.plot(x,productivity(x), 'bo--')
     #ax.set(xlabel ="Number of people", ylabel="person x hrs", title = "Maximal Productivity P({0}) ~ {1}".format(x,y))
     #ax.grid()
     #plt.show()



###############
# PROBLEM Four
###############
def nn(x,y,z):
    retList = []
    diffList = []
    for i in range(0, len(x)):
        diffList += [abs(y-x[i])]
    def isSmallest(lst, x):
        smallest = True
        for i in lst:
            if x > i:
                smallest = False
        return smallest
    while z:
        for i in range(len(diffList)):
            if isSmallest(diffList, diffList[i]):
                diffList = diffList[0:i] + diffList[i+1:]
                retList += [x[i]]
                x = x[0:i] + x[i+1:]
                break
        z -= 1
    return retList

#if __name__ == "__main__":
#  """
#  The code in "__main__" is not being graded, but a tool for you to test 
#  your code outside of the `test_a9.py`. Feel free to add print statements. 
#  """
#  x = [1,2,3,4,5,6,7,8,9,10]
#  y = 5
#  z = 3
#  print(nn(x,y,z))
#
#  x = [1.6,2,3]
#  y = 2
#  z = 2
#  print(nn(x,y,z))
#
#  x = [1,2,3,3]
#  y = 2
#  z = 3
#  print(nn(x,y,z))

###############
# PROBLEM Five
###############
from datetime import date
import numpy as np

x = 0
def get_next_id():
    global x
    x += 1
    return x

class Bank:
    def __init__(self, name, checking = 0, saving = 0):
        self.name = name
        self.checking = checking
        self.savings = saving
        self.ID = get_next_id()
        self.over_draft = 0
        self.checks_written = []
        self.check_number = 100

    def add_to_checks_written(self,information):
        self.checks_written += [[f'#{self.check_number}', f'{date.today()}', information, f'Acct: {self.ID}']]
        self.check_number+= 1
        pass

    def cut_check(self,amt):
        if self.checking - amt >= 0:
            self.add_to_checks_written(amt)
            self.checking -= amt
            return (1, amt, 0)
        else:
            self.over_draft += 25
            return (0, 0, self.over_draft)

    def deposit(self,amt,accnt):
        if type(amt) == float:
            if accnt == "checking":
                self.checking += amt
            else:
                self.savings += amt
        elif type(amt) == tuple:
            if amt[0] == 1:
                if accnt == "checking":
                    self.checking += amt[1]
                else:
                    self.savings += amt
        pass


    def __str__(self):
        header1 = f"\n{date.today()} \n"
        header2 = f"Account: {self.ID}  Name: {self.name}\n"
        accnts = f"Checking: ${self.checking} Savings: ${self.savings}\n"
        owed = f"Overdraft fee: ${self.over_draft}"
        return "*"*30 + header1 + header2 + accnts + owed + "\n" + "*"*30 + "\n"

#if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print statements. 
    # """
  # clst = [Bank("Ursala",1000,1000), Bank("Kaiser",50), Bank("Shilah")]

  # clients = np.empty(3,dtype=Bank)
  # for i,c in enumerate(clst):
  #     clients[i] = c#

  # #print(clients[0].cut_check(500))
  # #print(clients[1].cut_check(500))
  # #print(clients[1].cut_check(500))
  # #print(clients[0].checks_written)

  # #for c in clients:
  # #    print(c)

  # print("Starting Accounts")
  # print(clients[0])
  # print(clients[1])
  # print(clients[2])

  # clients[1].deposit(clients[0].cut_check(500),"checking")
  # clients[0].cut_check(200)
  # print("Accounts")
  # print(clients[0])
  # print(clients[1])
  # print("Ursala's checks")
  # print(clients[0].checks_written)
  # clients[1].cut_check(560)
  # clients[1].cut_check(1000)
  # clients[1].cut_check(550)
  # print("Kaiser's checks")
  # print(clients[1].checks_written)
  # print(clients[1])

###############
# PROBLEM Six
###############

"""
Please use `fungame.py`
"""
if __name__ == "__main__":
    print("***Problem 6***")
    print("Code must be done in `fungame.py` which has been provided")