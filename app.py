"""
# # # The following are exercises from MIT's Introduction to Computation and Programming Using Python, Third Edition [Book]
        # and Programming abstractions in C++ by Eric roberts
        # and CS106b (stanford) assignments (https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1214/build/assignments/3-recursion/)
        # https://ocw.mit.edu/courses/6-00sc-introduction-to-computer-science-and-programming-spring-2011/pages/resource-index/

# 1 # This is a program to print the biggest odd number (if any) amongs 3 inputted by the user

def getThreeNumbersFromUser():
    li = []
    # get 3 ints from user and store them in a sorted list
    for i in range(3):
        num = int(input('Enter a number: '))
        li.append(num)
    li.sort(reverse=True)
    return li


listOfThreeIntegers = getThreeNumbersFromUser()


def compareTheThreeNumbers(list):
    for i in range(len(list)):
        if list[i] % 2 != 0:
            return print('number is: ' + str(list[i]))

    return print('all numbers are even')


compareTheThreeNumbers(listOfThreeIntegers)

# --------------------

# 2 # This is the mario problem from CS50

levelsCount = int(input('How many times should I print the letter X? '))


def marioPyramid(numLevels):

    toPrint = ''
    numSpace = 0
    counter = 1
    while (numLevels != 0):

        numSpace = numLevels - 1
        toPrint = toPrint + str(numSpace * ' ') + str(counter * 'x')
        toPrint = toPrint + ' ' + str(counter * 'x') + '\n'
        counter = counter + 1
        numLevels = numLevels - 1
    return toPrint


print(marioPyramid(levelsCount))

# --------------------


# 3 # This is a program to print the biggest odd integer (if any) amongs 10 user inputs


def oddest(numInput):
    li = []
    oddest = None

    for i in range(numInput):

        num = int(input('Enter a number: '))
        li.append(num)
        li.sort(reverse=True)

    for j in range(len(li)):
        if li[j] % 2 != 0:
            oddest = li[j]
            break

    print('The list of numbers you entered is: \n' + str(li))

    if oddest == None:
        return print('the odds for odds are: ZEROOO!')
    else:
        return print('oddest is: ' + str(oddest))


oddest(4)

# --------------------


# 5 # This is a program that approximates a squareroot of an integer
import math
import random

x = random.randint(4, 1000000)
g = 1


def mysqrt(num, initGuessNum):

    while not (math.isclose(initGuessNum**2, num, rel_tol=0.0013)):
        initGuessNum = round((initGuessNum + num/initGuessNum)/2, 1)
    return initGuessNum


print('x is: ', x)
print('their square root: ', round(math.sqrt(x), 1))
print('my square root: ', mysqrt(x, g))

# --------------------



# 6 # a humanly direction algorithm to get to the nearest Edeka from my place

directions from thehouse to the nearest Edeka:

    go o the second block behind our building
    there would be a mall between the 2nd the 3rd blocks:
        edeka is on the under-ground flour

# --------------------


# 6 # a program to check if an int is a perfect cube


import random

x = 740696101223623662366236
k = 0

while k**3 < abs(x):
    # print('Value of the decrementing function abs(x) - k**3 is', abs(x) - k**3)

    k = k + 1


if k**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        k = -k
    print('Cube root of', x, 'is', k)

# --------------------


# 7 # a program that checks if a number is prime

import random

x = random.randint(4, 1000)


def isPrime(number):
    counter = 2
    smallestDivisor = 1
    largestDivisor = number / smallestDivisor

    while(counter < number - 1):
        if number % counter == 0:
            smallestDivisor = counter
            print(number, ' is not prime')
            return largestDivisor
        counter = counter + 1
    print(number, ' is  prime')
    return largestDivisor


print(isPrime(x))

#----------------------

# 7 # a program that prints the largest divisor of a number

import random

x = random.randint(1, 100)
sdiv = None
bdiv = None

for i in range(2, x):
    if x % i == 0:
        bdiv = x/i
        break
if bdiv != None:
    print('largest divisor of', x, 'is', bdiv)
else:
    print(x, 'is prime')


"""


"""
# 7 # 
program that taks an int (input) and prints pwr & root composing
#the int if any.

num = int(input('Enter a number: '))


def rAndp(x):

    for i in range(2, 6):
        pwr = int(x**(1/i))
        root = i

        if pwr**root == x:
            print('pwr is: ', pwr, 'and root is: ', root)
            return

    print('no perfect power in the range has been found!')
    return


rAndp(num)

"""


"""
# 7 # program that prints the sum of primes under 1000

def is_prime():
    sumOfPrimes = 0
    flagIsPrime = True

    for i in range(9, 1000, 2):
        for j in range(2, i):
            if i % j == 0:
                flagIsPrime = False
                break

        if flagIsPrime == True:
            
            sumOfPrimes += i
        flagIsPrime = True
    return sumOfPrimes


is_prime()

"""


"""

# 8 # a program that approximates the cube root of a given number


num = 941192


def sq(x):
    y = 0.01
    guess = 0
    low = 0
    high = max(1, x)
    ans = (high+low)/2
    iterationCount = 0

    while abs(ans**3 - x) >= y:
        print('low = ', low, 'high = ', high, 'ans = ', ans)
        guess += 1
        if ans**3 < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2
        iterationCount += 1

    print('guesses: ', guess)
    print('ans +: ', ans)
    print('ans -: ', -ans)


sq(num)
"""

"""

# 9 # Newton-Raphson algo for sqrts

y = 0.01  # precision measure
x = 1000
guess = x/2
iterationCount = 0
while abs(guess**2 - x) >= y:
    guess = guess - (((guess**2) - x) / (2*guess))
    iterationCount += 1
print('sqrt of ', x, 'is approx ', guess)

"""

"""
# 10 # a program that prints the longest substring alphabetically ordered within a given string

string = 'renhsyhjkdhgkgjdfshgrehstrhsthhdhd'

# Helper func


def sortAndReverseLists(lst):
    lst2 = sorted(lst, key=len)
    lst2.reverse()
    return lst2


# Main func


def listAllSubstringsThatAreAlphabeticallyOrdered(s):

    subList = []
    sub = s[0]
    for i in range(0, (len(s) - 1)):
        # print(s[i])
        if s[i] <= s[i+1]:
            sub += s[i+1]
        else:
            if len(sub) != 0:
                subList.append(sub)
            sub = s[i+1]
    return subList


list = listAllSubstringsThatAreAlphabeticallyOrdered(string)
LongestSubstringAlphabeticallyOrdered = sortAndReverseLists(list)[0]
print(LongestSubstringAlphabeticallyOrdered)


"""

"""

# 11 # a function that compares 2 strings and a function that tests the first function

def is_in (s1, s2):
    if s1 in s2 or s2 in s1:
        return True
    return False

str_list = ['list', 'li', 'me', 'mama' ,'cream', 'creamer']

def test_is_in(list):
    for s1 in list:
        for s2 in list:
            if s1 == s2:
                break
            result = is_in(s1, s2)
            if result == False and (s1 in s2 or s2 in s1):
                print(result)
                print(s1, s2)
                print("it doesnt work")
                return
    print("it's all good")
    return
            
test_is_in(str_list)

"""

# ----------------------------------------

"""
# exer book p.103

def mult(num1, num2 = None):
    if num2 == None:
        print(num1)
        return
    print(num1 * num2)
    
mult(2, 3)

"""
"""
Concepts:

- shallow copy => creates a new compount object -> inserts *references* to objects found in the original compound object
    syntax: obj.copy() | (or) obj[:] for lists
- deep copy => creates a new compount object -> inserts *copies* to objects found in the original compound object
"""

# video lections:
    #  shorturl.at/rACGI

"""
#  CS106B
#  Recursion 1


# 1 # recusively check if a string is a palindrom 

s1 = 'Madam'
s2 = 'Hkaalh'

def isPalindrom(str):
    str = str.lower()
    if len(str) < 2:
        print(f"Your string is Palindrom.")
        return True
    if str[0] != str[len(str)-1]:
        print(f"Not Palindrom because: {str[0]} ' =/= ' {str[len(str)-1]}")
        return False
    b = (len(str) - 1) - (len(str) - 2)
    e = len(str) - 1
    subStr = str[b:e]
    isPalindrom(subStr)

isPalindrom(s1)

# ----------------------------------------

# 2 # Print file content lines in reverse order

#  Add a file here => 
    #  fo = open("lines.txt", "r")

def rev(file):
    line = file.readline()
    if line:
        rev(file)
        print(line, end='')
    else:
        return
    
rev(fo)

fo.close()

# ----------------------------------------

# 3 # Recursively print names of directory and directories/files in it

import os
from pathlib import Path

di = "/Users/banana/repos/sandbox/py"
fi = "/Users/banana/repos/sandbox/py/a.py"
ind = "    "

def crwl(file, space):
    if not Path(file).is_dir():
        print( space + Path(file).parts[-1])
    
    if Path(file).is_dir():
        dirName = Path(file).parts[-1]
        print(dirName)
        notEmpty = any(Path(file).iterdir())
        if notEmpty:
            li = list(Path(file).iterdir())
            for p in li:
                # print(space)
                crwl(p, space)
            
        else:    
            print('nothing to see here.. 👀')
            

    
   
crwl(di, ind)

# ----------------------------------------

# 4 # cs106b part one: Sierpinski Triangle

from turtle import *

color("black")
                
t = Turtle()

def sp(forw, dep):
    if dep == 0:
        return
    else:
        for i in range(3):
            t.forward(forw)
            t.left(120)
            sp(forw/2, dep - 1)

        
        
sp(300, 4)

done()

# ----------------------------------------

# 5 # recursive bisection search

li = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def bis(x, l):
    if x == l[0] or  x == l[-1]:
        print("found")
        return
    if x < l[0] or x > l[len(l)-1]:
        print("not in the list")
        return 
    mid = int((len(l) - 1) / 2)
    if x > l[mid]:
        bis(x, l[mid:])
    elif x < l[mid]:
        bis(x, l[:mid])
    
    
bis(100, li)

# ----------------------------------------

# 6 # recursive factorial

def fact(num):
    if num == 0 or num == 1:
        return 1
    return num * fact(num - 1)

print(fact(4))

# ----------------------------------------

# 7 # recursive fibonacci

def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

min = int(input("Min: "))
max = int(input("Max: "))

for i in range(min, max + 1):
    print(f"{i}'th fibonacci number is: {fib(i)}")
    
# ----------------------------------------

# 8 # CS106b: Recursion part I & part II (shorturl.at/crsBI)

def weightOnBackOf(row, col, height, dictionary):
    # Out of range (not in the pyramid)
    if row > (height - 1) or row < 0 or col > (height - 1) or col < 0 or col > row:
        print(row, col, height)
        raise Exception("invalid colum/row number")
    
    # Base case
    if row == 0 and col == 0:
        return 0

    # Memoization check
    if row in dictionary.keys():
        if col in dictionary[row].keys():
            return dictionary[row][col]
    
    # Recursion 
    # Left edge
    if col == 0:
        weight = 80 + ((1/2) * weightOnBackOf(row - 1, 0, height - 1, dictionary))
        dictionary.update({row: {col: weight}})
        return weight

    # Right edge
    elif col == row:
        weight = 80 + ((1/2) * weightOnBackOf(row - 1, col - 1, height - 1, dictionary))
        dictionary.update({row: {col: weight}})
        return weight
    
    # Center
    weight = 160 + ((1/2) * weightOnBackOf(row - 1, col - 1, height - 1, dictionary)) + ((1/2) * weightOnBackOf(row - 1, col, height - 1, dictionary))
    dictionary.update({row: {col: weight}})
    return weight
    

def wrap(row, col, height):
    dic = {}
    result = weightOnBackOf(row, col, height, dic)
    return result

print(wrap(200, 100, 210))

# ----------------------------------------
# 8 # CS106b: iterative version of part III 
# TODO: try implimenting this recursively


s = "what are you doing"
k = s.split()


# getting all possible subsets which are all possible word combinations from s
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
   
    a = chain.from_iterable(combinations(iterable, r) for r in range(len(iterable)+1))
    return a

# list of tuples of subsets
j = list(powerset(k))

# function that converts tuple to string
def join_tuple_string(strings_tuple) -> str:
   return ' '.join(strings_tuple)

# joining all the tuples
result = map(join_tuple_string, j)
res = list(result)


#  getting list of lists of words that form all possible subsets of s and converting them to uppercase
for i in range(0,len(res)):
    res[i] = res[i].split()
# print(res)

# converting every word in in every possible subset of words from s into upper-case
for i in range(0, len(res)):
    res[i] = [x.upper() for x in res[i]]



# reconstructing each subset of words to the full sentence (matching s) while being case sensitive so that what was converted
# previously to uppper case, stays upper-case
for li in res:
    for word in k:
        if word.upper() not in li:
            i = k.index(word)
            li.insert(i, word)
    
    # printing all possible allEmphasesOf s
    print(" ".join(li))
    
    
# ----------
# Recursive version of part III from Stackoverflow help: https://stackoverflow.com/a/71448663/17161821

inputStr = "what are you doing"
wordList = inputStr.split()

def allEmphasesOf(wl):
    if not wl:
        return []
    if len(wl) == 1:
        return [[wl[0]], [wl[0].upper()]]
    
    ans = []
    options =  allEmphasesOf(wl[1:])
    
    
    for option in options:
        ans.append([wl[0]] + option)
        ans.append([wl[0].upper()] + option)
        
   
    return ans

ls = allEmphasesOf(wordList)

def g(ls):
    
    j = []
    for el in ls:
        j.append(' '.join(el))
        
    return j



print(g(ls))


# ----------
# Tower of Hanoi (p.361)

def h(frm, to):
    print(f"move disk from {frm} to {to}")
    
def f(start, end, temp, n):
    if n == 1:
        return h(start, end)
    
    f(start, temp, end, n - 1)
    h(start, end)
    f(temp, end, start, n - 1)

f("a", "b", "c", 3)
# ----------


def f(s, i):
    if i in s:
        return True
    
    
    elif sum(s) == i:
        return True
    
    elif len(s) > 0:
        el = s[0]
        return f(s[1:], i) or f(s[1:], i - el)
    
    return False
    
    
        


a = [-2, 1, 3, 8]

print(f(a, 13))

# -----------
# subset sum (book)
def f(s, i):
    if i in s:
        return True
    
    
    elif sum(s) == i:
        return True
    
    elif len(s) > 0:
        el = s[0]
        return f(s[1:], i) or f(s[1:], i - el)
    
    return False
    
    
        


a = [-2, 1, 3, 8]

print(f(a, 5))

# ---------------
# string permutations


from itertools import permutations

perms = permutations(list("ABC"))

result = []

for perm in perms:
    result.append(perm)
    
print(result)
"""


