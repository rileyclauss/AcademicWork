import sys
import string

wordDict = {}

def clean_word(word):
    if type(word) != str:
        return ""
    retWord = word.strip("{0}{1}".format(string.whitespace, string.punctuation))
    if retWord.isalpha():
        return retWord.lower()
    return ""

def process_line(line):
    wordList = line.split(" ")
    retList = []
    for i in wordList:
        x = clean_word(i)
        if x not in retList and x != '':
            retList.append(x)
    return retList

def extend_concordance(dictionary, line, line_number):
    words = process_line(line)
    for i in words:
        if i in dictionary:
            dictionary[i] += [line_number]
        else:
            dictionary[i] = [line_number]
    pass

def main(filename):
    d = dict()
    fileX = open(filename, "r")
    lines = fileX.readlines()
    for i in range(len(lines)):
        extend_concordance(d, lines[i], i+1)
    return d

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'Midterm/jabberwocky.txt'
    d = main(filename)
    for item in sorted(d.items()):
        print(f"{item[0]} : {item[1]}")
