#INPUT two values
#RETURN A and B
def myAnd(A,B):
     return (A and B)

#INPUT two values
#RETURN A or B 
def myOr(A,B):  
     return (A or B)

#INPUT one value
#RETURN not A
def myNot(A):   
     return(not A)

#INPUT two values
#RETURN not (A and B) (called nand)
#REQUREMENTS use only previous functions
def myNand(A,B):
     return myNot(myAnd(A,B))

#INPUT two values
#RETURN not (A or B) (called nor)
#REQUIREMENTS use only previous functions
def myNor(A,B):
     return myNot(myOr(A,B))

#INPUT two values A,B
#Return material implication A => B 
#REQUIREMENTS use only previous functions
def myImplication(A,B):
     return myOr(myNot(A),B)

#INPUT two values A,B
#RETURN A or B 
#REQUIREMENTS only use myNand gate
def DeMorganNand(A,B):
     return myNand(myNand(A,A),myNand(B,B))
     
