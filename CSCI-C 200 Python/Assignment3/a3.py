"""
TODO: Add comment about who your partner was (or if you worked alone). 
Include anything else you want to in this comment

"""

import math


###########################################################################
# Functions for Problem 1
###########################################################################
#INPUT d dollars, r interest rate, y time
#RETURN amount of money at end of term
def y(d,r,t):
    return (d * math.exp(r*t))

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    return (n_0 * math.exp(m*t))

#INPUT t days
#RETURN number of teach
def N_t(t):
    return math.ceil(71.8*(math.e**(-8.96*(math.e**(-0.0685*t)))))

#INPUT t hours
#RETURN concentration
def K(t):
    return round((((((9)/(2.6))*t)/((2*(t**2)+3)))/100),5)


#INPUT t years
#RETURN average monthly rent
def r(t):
    return round(((1.5207*(t**4))-(19.166*(t**3))+(62.91*(t**2))+(6.0726*t)+(1026)), 2)

#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    return math.ceil(8.314*300*(math.log(P_i/P_f)))

#INPUT cost c, salvage value s, life el where c >= s
#RETURN
def dep(c,s,el):
    return round(((c-s)/el),0)

#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    return math.ceil(0.0033*(V**2)*A*C_l)

###########################################################################
# Functions for Problem 2
###########################################################################
def q(a,b,c):
    # This function will return a tuple of 2 values
    # The "plus" value must be first in the tuple
    # The "minus" value must be second in the tuple 
    # The unit test expects ((v+u),(v-u)) **not** ((v-u),(v+u))

    discrim = (b**2) - (4*a*c)
    
    ans1 = 0
    ans2 = 0

    if discrim < 0:
        ans1 = (-b)/(2*a) - math.sqrt(abs(discrim))/(2j*a)
        ans2 = (-b)/(2*a) + math.sqrt(abs(discrim))/(2j*a)
        
    else: 
        ans1 = (-b)/(2*a) + math.sqrt(discrim)/(2*a)
        ans2 = (-b)/(2*a) - math.sqrt(discrim)/(2*a)
    return ans1, ans2



###########################################################################
# Functions for Problem 3
###########################################################################
def checkout(xlst):
    #list of lists
    amt = 0
    for item in xlst:
        if item[2]:
            amt += (item[0]*item[1]) * 0.07
        amt += (item[0] * item[1])

    return amt


###########################################################################
# Functions for Problem 4
###########################################################################
def open_seat_count(xlst):
    total = len(xlst)*len(xlst[0])
    taken = 0
    for rows in xlst:
        for seats in rows:
            taken += seats
    return total-taken

###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

def arithmetic_mean(nlst):
    if len(nlst) < 1:
        return "Data Error: 0 values"
    return sum(nlst)/len(nlst)

def geo_mean(nlst):
    if len(nlst) < 1:
        return "Data Error: 0 values"
    tot = 1
    for i in nlst:
        tot *= i
    return tot**(1/len(nlst))

def har_mean(nlst):
    if len(nlst) < 1:
        return "Data Error: 0 values"
    tot = 0
    for i in nlst:
        if i == 0:
            return "Data Error: 0 in data"
            break
        tot += (1/i)
    return len(nlst)/tot

def RMS_mean(nlst):
    if len(nlst) < 1:
        return "Data Error: 0 values"
    tot = 0
    for i in nlst:
        tot += i**2
    return math.sqrt(tot/len(nlst))


###########################################################################
# Functions for Problem 6
###########################################################################
#INPUT ISBN string, assume "D-DDD-DDDDD-D" 
# D is digit
#RETURN Boolean if valid ISBN

def valid_ISBN(ISBN_str):
    ISBN_str = ISBN_str.replace("-","")
    tot = 0
    for i in range(0,len(ISBN_str)):
        tot += (i+1)*int(ISBN_str[i])
    if tot%11 == 0:
        return True
    else:
        return False


###########################################################################
# Functions for Problem 7
###########################################################################

#INPUT [b,c,x]
#RETURN b*x + c
def cost(b,c,x):
    return b*x + c

#INPUT [a,x]
#RETURN a*x
def revenue(a,x):
    return a*x

#INPUT [a,b,c,x]
#RETURN profit(x) = revenue(a,x) - cost(b,c,x)
#REQUIRES revenue & cost
def profit(a,b,c,x):
    return revenue(a,x) - cost(b,c,x)




#INPUT [a,b,c]
#RETURN x smallest integer of units
# to break even profit(x) >= 0
# Does not require any functions
def break_even(a,b,c):
    return math.ceil(c/(a-b))


###########################################################################
# Functions for Problem 8
###########################################################################

#INPUT list [p,i,n] principal, interest rate, payments
#RETURN montly payment float
def Mortgage(house):
    if house[1] > 1:
        house[1] = house[1]/100.0
    mortg = ((house[1]/12)*((1.0+(house[1]/12.0)) ** (house[2]*12.0)))/(((1.0+(house[1]/12.0)) ** (house[2]*12.0)) - 1.0)
    return round((house[0] * mortg),2)



#INPUT list [p,i,n] principal, interest rate, payments
#RETURN the difference between total payout and value
#of home
#REQUIRES Mortgage function
def total_paid(house):
    paid = Mortgage(house)*house[2]*12.0
    return round(paid - house[0], 1)


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """
    Mortgage([300000,2.9,30])
