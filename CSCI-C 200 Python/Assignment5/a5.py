import math
import itertools

##########################################################################
#PROBLEM 1
##########################################################################
#
#INPUT positive number n
#RETURN log of number base 2
def log_2(n):
    #print("====math.log====")
    #print(math.log(n,2))
    return math.log(n,2)

#INPUT list of immutable objects
#RETURN probability distribution
def makeProbability(xlst):
    nList = {}
    for i in xlst:
        if i in nList:
            nList[i] += 1
        else:
            nList[i] = 1
    
    rList = []
    for i in nList:
        rList += [nList[i]/len(xlst)]
    return rList

#INPUT probability distribution
#RETURN non-negative number entropy
def entropy(xlst):
    entint = 0
    #print("===makeprobability===")
    #print(makeProbability(xlst))
    for i in xlst:
        entint += (i * (log_2(i)))
    return entint * -1




##########################################################################
#PROBLEM 2
##########################################################################
#INPUT positive integer
#RETURN positive integer
def magick(x):
    x += 15
    x *= 3
    x -= 9
    x /= 3
    #x -= 12?
    return x


##########################################################################
#PROBLEM 3
##########################################################################
#INPUT a list of lists of three positive integers [[a,b,c],[d,e,f],[g,h,i]]
#RETURN True if the input is a magic square
#You can create other functions to help you--they will 
#not be unit tested
def is_magic_square(s3):
    listOfChar = []
    for i in range(len(s3)):
        for j in range(len(s3[i])):
            if s3[i][j] in listOfChar:
                return False
            else:
                listOfChar += [s3[i][j]]
    if checkRows(s3) and checkColumns(s3):
        diag1 = (s3[0][0] + s3[1][1] + s3[2][2])
        diag2 = (s3[0][2] + s3[1][1] + s3[2][0])
        if diag1 == diag2:
            return True
        else: 
            return False
    else:
        return False

#pass whole list, check each row
def checkRows(x):
    rowVals = [0,0,0]
    for i in range(len(x)):
        rowVals[i] += x[i][0] + x[i][1] + x[i][2]

    if (rowVals[0] == rowVals[1] and rowVals[1] == rowVals[2]):
        return True
    else:
        return False


def checkColumns(x):
    colVals = [0,0,0]
    for i in range(len(x)):
        colVals[i] += x[0][i] + x[1][i] + x[2][i]

    if (colVals[0] == colVals[1] and colVals[1] == colVals[2]):
        return True
    else:
        return False

#INPUT nothing
#RETURN list of solutions to magic square size 3
def generate_3_square():
    solutions = []
    numRange = [1,2,3,4,5,6,7,8,9]
    allPerms = itertools.permutations(numRange)
    argList = []
    for i in allPerms:
        argList = []
        argList += [i[0:3], i[3:6], i[6:9]]
        if is_magic_square(argList) == True:
            solutions += [argList]

    return solutions

##########################################################################
# PROBLEM 4
##########################################################################
key = "abcdefghijklmnopqrstuvwxyz{"
ciphDict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', '{':'{'}
#INPUT takes a letter and shift
#RETURN new letter shifted 
def encrypt(letter, n):
    return ciphDict[letter]    
#INPUT takes a letter and shift
#RETURN original letter
def decrypt(letter, n):
    return ciphDict[letter]
#INPUT takes a sentence of lowercase letters and spaces and shift
#RETURN caeser cypher
def encrypt_sentence(sentence, shift):
    sentence = sentence.replace(" ", "{")
    for i in range(len(key)):
        if i + shift < len(key):
            ciphDict[key[i]] = key[i+shift]
        else:
            ciphDict[key[i]] = key[(i+shift) - len(key)]
    result = ""
    for i in sentence:
        result += encrypt(i, shift)
    return result


#INPUT takes an encrypted sentence and shift
#RETURN decrypted sentence
def decrypt_sentence(sentence, shift):
    for i in range(0,2):
        for j in range(len(key)):
            ciphDict[key[j]] = key[(j-shift)]
    result = ""
    for i in sentence:
        result += encrypt(i, shift)
    result = result.replace("{", " ")
    return result

##########################################################################
# PROBLEM 5
##########################################################################

#INPUT non-negative integer and non-negative integer > 1
#RETURN Wild Number [string, base]
#string is encoding of number in base, base is integer
def make_number(decimal, base):
    divisor = decimal
    resultStr = ""
    while divisor > 0:
        if divisor % base == 0:
            resultStr += "0"
        else:
            resultStr += str(divisor % base)
        divisor = divisor // base
    return [resultStr[::-1], base]
#INPUT Wild number 
#RETURN new wild number in new base
def convert(number, base):
    newNum = int(number[0], number[1])
    return make_number(newNum, base)

#INPUT two wild numbers
#RETURN product as a (possibly new) base
def mul_(number1, number2, base):
    deciX = convert(number1, 10)
    deciY = convert(number2, 10)
    sumX = str(int(deciX[0]) * int(deciY[0]))
    return convert([sumX, 10], base)

#INPUT two wild numbers
#RETURN sum as a (possibly new) base
def add_(number1, number2, base):
    deciX = convert(number1, 10)
    deciY = convert(number2, 10)
    sumX = str(int(deciX[0]) + int(deciY[0]))
    return convert([sumX, 10], base)

##########################################################################
# PROBLEM 6
##########################################################################

#the dictionary for the transation
aa_d = {}
#the FASTA file
DNA_d = [ ]

#the translation
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"

#INPUT path and file name of amino acid file
#RETURN a dictionary 
#Key is a tuple (c0, c1, ... , cn) where ci are codons
#Value is a pair [name, abbreviation] for the amino acid
def get_amino_acids(path,name):
    fileX = open(path + "/" + name, "r")
    contents = fileX.readlines()
    aminoAcidDict = {}
    for i in contents:
        i = i.strip()
        listX = i.split(", ")
        aminoAcidDict[tuple(listX[2:])] = [listX[0], listX[1]]
    return aminoAcidDict

#INPUT path and file name of amino acid file
#RETURN a list [header, DNA]
#header is first line in the file
#DNA is a string of letters from remainder of file
#no whitespace
def get_DNA(path,name):
    DNAseq = ""
    fileX = open(path + "/" + name, "r")
    contents = fileX.readlines()
    header = contents[0].strip()
    for i in range(1, len(contents)):
        DNAseq += contents[i].strip()
    return [header, DNAseq]

#INPUT FAST file
#RETURN a string representing the protein
#using the dictionary
def translate(DNA_d):
    currStrand = ""
    translation = ""
    for i in range(0,len((DNA_d[1])), 3):
        currStrand = DNA_d[1][i:i+3]
        for keys in aa_d:
            for j in keys:
                if j == currStrand:
                    translation += aa_d[keys][1]
    return translation
#Do not modify these statements
aa_d = get_amino_acids("Assignment5", "amino_acids.txt")
DNA_d = get_DNA("Assignment5", "DNA.txt")
protein = translate(DNA_d)

##########################################################################
if __name__ == "__main__":
    print("For your use...")
    print("Please comment the code you want to run. Make sure it is inside of this if statement")
#     # Feel free to add your own tests here to help with error handling. 
#     print("This is the code file. To see test results, please run 'test_a5.py'")
#     print("Feel free to write your own tests here. The tests you write below will not be graded.")
    
    #print("*"*10 + "Problem 1"+"*"*10 +  "\n")
    #s0 = ["a", "b", "a", "c", "c", "a"]
    #s1 = ['a','b','a','b','a','b','b','b']
    #s2 = [(1),(2),(3),(4)]
    #s3 = [1]
    #s4 = [1,2,1,2]

    #xlst = [s0, s1,s2,s3,s4]

    #for i in xlst:
    #    p = makeProbability(i) 
    #    e = entropy(p)
    #    print(f"{p} has entropy {e}")


    #print(magick(25))

    #print("*"*10 + "Problem 2"+"*"*10 +  "\n")
    #s1 = [[2,7,6],[9,5,1],[4,3,8]] #True
    #s2 = [[8,1,6],[3,5,7],[4,9,2]] #True
    #s3 = [[8,6,1],[3,6,7],[4,9,2]] #False
    #s4 = [[1,1,1],[1,1,1],[1,1,1]] #False
    #s = [s1,s2,s3,s4]
    #for i in s:
    #    print("{0} is ".format(i) + "not "*(not is_magic_square(i)) + "a magic square." )
    #print(generate_3_square())

    #print("*"*10 + "Problem 4"+"*"*10 +  "\n")
    #sentence = "this is a secret message about the class"
    #shift = 5
    #secret = encrypt_sentence(sentence, shift)
    #decode_secret = decrypt_sentence(secret, shift)
    #
    #print(f"original: {sentence}")
    #print(f"encrypted: {secret}")
    #print(f"decrypted: {decode_secret}")

    #print("*"*10 + "Problem 5"+"*"*10 +  "\n")    
    #n1,n2 = 5,4
    #base2, base10 = 2,10

    #x1, y1 = make_number(n1,base2), make_number(n2,base2)
    #print(x1,y1)
    #print(convert(x1,base10))
    #print(add_(x1,y1,base10))
    #print(add_(x1,y1,base2))
    #print(convert(add_(x1,y1,base2), base10))
    #print(mul_(x1,y1,base2))
    #print(convert(mul_(x1,y1,base2),base10))

    print("*"*10 + "Problem 6"+"*"*10 +  "\n") 

    print("Dictionary")
    print(aa_d)
    print("FASTA file")
    print(DNA_d)
    print("Translations match:", str(protein == actual))

    #should return "PLHS"    
    print(translate(["nothing", "CCACTGCACTCA"]))

    #should returns "D-"
    # print(translate(["nothing", "GACTAA"]))