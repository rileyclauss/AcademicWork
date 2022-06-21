###############
# PROBLEM ONE
###############
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def cost(x):
    return 2000 + 500*x

def revenue(x):
    return (2000*x) - (10*(x**2))

def profit(x):
    return revenue(x) - cost(x)

    """ 
    Do Not Change Below
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


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """
    #f = fp(profit)
    #x = newton(f,fp(f),1,.0001)
    #print("The maximum profit is about ${0}".format(profit(round(x,0))))

    #t = np.arange(0.0, 100.0)
    #fig,ax = plt.subplots()

    #ax.plot(t, profit(t),'g')
    #ax.plot(75,profit(75), 'bo--')
    #ax.set(xlabel ="Widgets Sold", ylabel="Profit ($)",
    #title = "Maximal Profit = ${0}".format(profit(75)))
    #ax.grid()
    #plt.show()



###############
# PROBLEM TWO
###############


def sign(x):
    return -1 if x<=0 else 1


def bisect(f,a,b,tau):
    c = (a+b)/2
    if b-c <= tau:
        return c
    elif sign(f(b)) * sign(f(c)) <= 0:
        return bisect(f,c,b,tau)
    else:
        return bisect(f,a,c,tau)

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """
    #ex_f = lambda x: x**6 - x - 1
    #x = bisect(ex_f,1.0,2.0,.001)
    #print(x,ex_f(x))

 
###############
# PROBLEM THREE
###############
# THERE IS NO UNIT TEST ON THIS PROBLEM
###############

import pygame
import sys
import random as rn

 
DARKGREEN = (0,55,0)
BLACK = ( 0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
RED =   (255,0,0)
YELLOW = (255,255,0)


class Rectangle:

    def __init__(self,color,loc):
        self.loc = loc
        self.color = color

    def my_draw(self,screen):
        pygame.draw.rect(screen, self.color, self.loc)
    
    def my_move(self,xoffset,yoffset):
        self.loc = [self.loc[0]+xoffset,self.loc[1]+yoffset] + self.loc[2:]#

    def my_color(self, newColor):
        self.color = newColor
  
       




if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a8.py`. Feel free to add print statements. 
    """
    #pygame.init()
    #size = [300, 300]
    #screen = pygame.display.set_mode(size)
    #pygame.display.set_caption("C200 CHANGE")

    #r = Rectangle(RED, [0, 0, 20, 20])

    #while True:
    #    
    #    pygame.time.wait(40)
    #    
    #    for event in pygame.event.get(): 
    #        if event.type == pygame.QUIT: 
    #            pygame.quit()
    #            sys.exit()
    #
    #    screen.fill(WHITE)
    #    
    #    r.my_draw(screen)
    #    
    #    if r.loc[0] > 280:
    #        xd = -rn.randint(1,3)
    #        newColor = DARKGREEN
    #    if r.loc[1] > 280:
    #        yd = -rn.randint(1,3)
    #        newColor = BLUE
    #    if r.loc[0] < 10:
    #        xd = rn.randint(1,3)
    #        newColor = RED
    #    if r.loc[1] < 10:
    #        yd = rn.randint(1,3)
    #        newColor = YELLOW
    #    r.my_color(newColor)
    #    r.my_move(xd,yd)

    #    pygame.display.flip()


###############
# PROBLEM FOUR
###############

def secant(f,x0,x1,tau):
    if abs(x0-x1) <= tau:
        return x1
    else:
        return secant(f, x1, (x1 - f(x1) * ((x1 - x0)/(f(x1) - f(x0)))), tau)

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a8.py`. Feel free to add print statements. 
    """

    #ex_f = lambda x: x**6 - x - 1
    #x = secant(ex_f,2.0,1.0,.0001)
    #print(x,ex_f(x))
    

###############
# PROBLEM FIVE
###############
import math 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def even(x):
    pass

def simpson(fn,a,b,n):
    deltX = (b-a)/n
    innerF = lambda z : a+(z*(deltX))
    sumList = [fn(a)]
    i = 1
    while i<n:
        tempVal = fn(innerF(i))
        if i%2:
            tempVal *= 4
        else:
            tempVal *= 2
        sumList += [tempVal]
        i += 1
    sumList += [fn(b)]
    return (deltX/3)*(sum(sumList))


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a8.py`. Feel free to add print statements. 
    """

    #data = [[lambda x:3*(x**2)+1, 0,6,2],
    #        [lambda x:x**2,0,5,6],
    #        [lambda x:math.sin(x), 0,math.pi, 4],
    #        [lambda x:1/x, 1, 11, 6]]


    #for d in data:
    #    f,a,b,n = d
    #    print(simpson(f,a,b,n))

    #t = np.arange(0.0, 10.0,.1)
    #fig,ax = plt.subplots()
    #s = np.arange(0,6.1,.1)
    #ax.plot(t, (lambda t: 3*(t**2) + 1)(t),'g')
    #plt.fill_between(s,(lambda t: 3*(t**2) + 1)(s)) 
    #ax.grid()
    #ax.set(xlabel ="x", ylabel=r"$f(x)=3x^2 + 1$",
    #title = r"Area under the curve $\int_0^6\,f(x)$")

    #plt.show()
###############
# PROBLEM SIX
###############

#recursive
def V(n,m):
    if m == 0:
        return 4
    else:
        return 2*n - V(n-1,m-1)

#update dictionary e inside Vm
#memoization
e = {}

def Vm(n,m):
    e[(n-m, 0)] = 4
    for nIt, mIt in zip(range(n-m+1, n+1), range(1, m+1)):
        e[(nIt,mIt)] = 2*nIt - e[(nIt - 1, mIt - 1)]
    return e[(n,m)]



#generator
def h(n,m):
    current,previous = 4,0
    nIt = n-m
    while True:
        yield current
        previous = current
        current = 2*(nIt+1) - previous
        nIt += 1

def Vh(n,m):
    cnt = 0
    for i in h(n,m):
        if cnt == m:
            return i
        cnt+= 1
      



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a8.py`. Feel free to add print statements. 
    # """
    #print("\n"*5)
    #print("Problem 6")
    #for i in range(5):
    #    for j in range(5):
    #        print(i,j,V(i,j), Vm(i,j), Vh(i,j))
    