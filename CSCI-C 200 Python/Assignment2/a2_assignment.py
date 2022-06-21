import math

#PROBLEM 1 a2_1
#INPUT speed s mile/hr as integer
#RETURN change in speed as integer
def s(speed_limit):
    if speed_limit >= 55:
        return speed_limit + 5
    elif speed_limit >= 45:
        return speed_limit + 3
    elif speed_limit >= 30:
        return speed_limit + 1
    else:
        return speed_limit

#PROBLEM 2 a2_2
#INPUT kilograms
#RETURN energy joules
def E(m):
    c = 3e8 #uses scientific notation
    return m*(c**2.0) #calculate inline 

#PROBLEM 3 a2_3
#INPUT fuel_price, money, gas_mileage, distance
#RETURN Boolean (True or False) if this can be traveled
def f(fuel_price, money, gas_mileage, distance):
    if distance <= ((money/fuel_price) * gas_mileage): #distance <= ((gallons you can buy) * mileage)
        return True
    else:
        return False


#PROBLEM 4 a2_4
#INPUT angle (degrees), length, length
#RETURN length of opposite side
def law_cosines(angle, len_1, len_2):
    angle *= math.pi # times pi
    angle /= 180   # over 180
    return math.sqrt((len_1**2)+(len_2**2)-(2*len_1*len_2*math.cos(angle))) #equation inline

#PROBLEM 5 a2_5a
#You cannot use Python's max function
#You must use if, elif, else (or some combination)
#INPUT two numbers
#RETURN maximum of the two
def max(x,y):
    if x > y: 
        return x
    else:  #assuming x == y is not a special case
        return y

#PROBLEM 5 a2_5b
#You must use your max function
#INPUT non-empty list of numbers
#RETURN maximum number in list
def max_3(x,y,z):
    return (max(max(x,y),max(y,z)))  #combination to find the max of either

#PROBLEM 5 a2_5c
#You can *only* use if, elif, and else (or some combination)
#INPUT 3 numbers
#RETURN maximum number in list
def max_3h(x,y,z):      #>= assumes that if two variables are equal, returning either of them is as good as returning the max
    if x >= y and x >= z:  #if x is greatest,
        return x
    elif y >= x and y >= z: #if y is greatest,
        return y
    else:      #if z is greatest
        return z

#PROBLEM 6 a2_6
#INPUT pair of strings for colors:
# "yellow", "blue", "red", "green", "purple", and so on
#RETURN either a color when c1, c2 are the same
#or the 2ndary color given primary colors
#or "unknown" otherwise
def color_wheel(c1,c2):
    if c1 == c2:  #if the colors are the same
        return c1
    else:
        color = c1 + c2   #because order doesn't matter, I can use
        if "blue" in color and "red" in color: #substring searching to identify
            return "purple"                    #mixes of colors and return the correct color
        elif "blue" in color and "yellow" in color: #from there.
            return "green"
        elif "red" in color and "yellow" in color:
            return "orange"
        else:
            return "unknown"

#PROBLEM 7 a2_7a
#INPUT radius of circle in inches
#RETURN area of circle
def pizza_area(radius):
    return math.pi*(radius**2)

#PROBLEM 7 a2_7b
#INPUT r1, c1 (radius and cost of pizza 1)
#      r2, c2 (radius and cost of pizza 2)
#RETURN the radius of the pizza that's cheaper
#You must use the pizza_area function 
def cost_per_inch(r1,c1,r2,c2):
    pizza1 = c1/pizza_area(r1)
    pizza2 = c2/pizza_area(r2)
    if pizza1 < pizza2:
        return r1
    else:
        return r2 #if the prices are equal, might as well get more pizza out of the deal :)

#Separate problems in output
def pretty(asn):
    print(10*"~" + "problem " + str(asn) + 10*"~")

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """
    
    # pretty(1)
    # print(s(60),s(50),s(40),(20))

    # pretty(2)
    # print("{:.0e}".format(E(.1)))
    
    # pretty(3)
    # print(f(1, 7.50, 10, 200))
    # print(f(1, 20.00, 10, 200))
    # print(f(3, 20.00, 10, 200))
    # print(f(3, 20.00, 35, 200))

    # pretty(4)
    # print(law_cosines(50,3,4))
    # print(law_cosines(47,9,10))
    # print(law_cosines(90,5,5))

    # pretty(5)
    # print(max_3(1,2,3))
    # print(max_3(3,2,1))
    # print(max_3(1,3,2))
    # print(max_3h(1,2,3))
    # print(max_3h(3,2,1))
    # print(max_3h(1,3,2))

    # pretty(6)
    # print(color_wheel("yellow", "blue"))
    # print(color_wheel("blue", "yello"))
    # print(color_wheel("yellow", "yellow"))
    # print(color_wheel("orange", "yellow"))

    # pretty(7)
    # print(cost_per_inch(18,10,12,7))
    # print(cost_per_inch(18,10,12,5))
    # print(cost_per_inch(18,10,12,4))