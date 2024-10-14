##### Say "Hello, World!" with Python

print("Hello, World!")

##### Python If-Else

# integer n from input()
n = int(input())
# if n is odd print "Weird"
if n % 2 != 0:
  print ("Weird")
elif n % 2 == 0 and n >= 2 and n <= 5:
  print ("Not Weird")
elif n % 2 == 0 and n >= 6 and n <= 20:
  print ("Weird")
elif n % 2 == 0 and n > 20:
  print("Not Weird")

##### Arithmetic Operators

#a = int(input("First integer a: "))
#b = int(input("Second integer b: "))
#print("Sum a+b:", a+b)
#print("Difference a-b:", a-b)
#print("Product a*b:", a*b)
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

##### Python: Division

a = int(input())
b = int(input())
print(a//b) # integer division a // b
print(a/b) # float division a / b

##### Loops

n = int(input())
for i in range(n): # function range() : 0, 1, 2, ... n
  print(i*i)

##### Write a function

def is_leap(year):
    leap = False # is not a leap year
    # leap = True # is a leap year

    """
    In the Gregorian calendar, three conditions are used to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
      The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.
    """

    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          leap = True
        else:
          leap = False
      else:
        leap = True
    else:
      leap = False

    return leap

year = int(input())
print(is_leap(year))

##### Print Function

n = int(input())
for i in range(n):
  print(i+1, end="") # end="" (on the same line)


##### List Comprehensions

""" print a list of all possible coordinates
given by (i,j,k) where the sum of i+j+k is not equal to n
0<=i<=x, 0<=j<=y, 0<=k<=z """
x = int(input())
y = int(input())
z = int(input())
n = int(input())

list_x = [i for i in range(x+1)]
list_y = [j for j in range(y+1)]
list_z = [k for k in range(z+1)]

list_xyz = [[i,j,k] for i in list_x for j in list_y for k in list_z]
#print(list_xyz)
list_xyz_sum_not_n = [i for i in list_xyz if sum(i) != n]
print(list_xyz_sum_not_n)

##### Find the Runner-Up Score!

n = int(input())
str = input()
arr_str = str.split()
arr_num = []

for i in range(len(arr_str)):
  arr_num.append(int(arr_str[i])) # append integer value in arr_num

#print(arr_num)
max_value = max(arr_num)
# now that we have the max_value, we have to find if there are
# other elements with the same max_value, and exclude them
arr_num_excluding_max_values = [i for i in arr_num if i != max_value]
# now the max item of the list is the runner-up
print(max(arr_num_excluding_max_values))

##### Nested Lists

# a way to get data problem via input()
# step 1: number of students, int(input())
# step 2: for function (get name and score for each student)
# char '_' is a possibility beacuse we don't need an index here
students = []
for _ in range(int(input())):
  name = input()
  score = float(input())
  students.append([name, score]) # the nested list required by the problem

# using a special lambda function to sort the list students [0:name, 1:score] by score
students.sort(key=lambda x: x[1]) # by score
lowest_grade = students[0][1] # get the lowest grade

# using a list (for all the second lowest grades)
second_lowest_grade = []
for i in range(len(students)):
  if students[i][1] != lowest_grade: # if is different from the lowest grade
    second_lowest_grade.append([students[i][0],students[i][1]])
    # break the for loop if the grade of the next item i+1 is different
    # condition: i+1 < len(students) for not exceed the list limit
    if i+1 < len(students) and students[i][1] != students[i+1][1]:
      break

second_lowest_grade.sort() # alphabetically ordering
for i in range(len(second_lowest_grade)):
  print(second_lowest_grade[i][0])

##### Finding the percentage

# input-set from HackerRank *****************
if __name__ == '__main__':
  n = int(input())
  student_marks = {} # empty dictionary
  for _ in range(n):
      # Reads a line of input, splits it into words,
      # and assigns the first word to name and the rest to the list line.
      name, *line = input().split()
      # Converts the elements in line to floating-point numbers
      # and stores them in the scores list.
      scores = list(map(float, line))
      # Adds the name and scores pair to the student_marks dictionary
      student_marks[name] = scores
  query_name = input()
# ********************************************

  # arithmetic average (is a float)
  average = sum(student_marks[query_name])/len(student_marks[query_name])
  # using format() method
  # "{:.2f}" format string
  # . indicates the position of the decimal point.
  # 2 specifies the number of decimal digits to display.
  # f indicates that we are formatting a float number.
  print("{:.2f}".format(average))

##### Lists

if __name__ == '__main__':
  N = int(input())
  list = []
  for _ in range(N):
    command = input().split()

    # 1. "insert i e": insert integer "e" at position "i"
    if command[0] == "insert":
      # list.insert(int(position), int(element))
      list.insert(int(command[1]), int(command[2]))
    # 2. "print": print the list
    elif command[0] == "print":
      print(list)
    # 3. "remove e": delete the first occurence of integer e
    elif command[0] == "remove":
      list.remove(int(command[1]))
    # 4. "append e": insert integer "e" at the end of the list
    elif command[0] == "append":
      list.append(int(command[1]))
    # 5. "sort": sort the list
    elif command[0] == "sort":
      list.sort()
    # 6. "pop": pop the last element from the list
    elif command[0] == "pop":
      list.pop()
    # 7. "reverse": reverse the list
    elif command[0] == "reverse":
      list.reverse()

##### Tuples

# OK in HackerRank if I set "Pypy 3" as Language (WHY?)

n = int(input())
numbers_tuple = tuple(map(int, input().strip().split()))
# map(function, iterable)
# map(): Return an iterator that applies function
# to every item of iterable, yielding the results.
# print(numbers_tuple)
print(hash(numbers_tuple))

"""
Input (stdin)
2
1 2
Expected Output
3713081631934410656
"""

# a (possibile) explanation: https://stackoverflow.com/questions/74686631/why-this-code-is-giiving-different-result-in-python-and-pypy3

##### sWAP cASE

def swap_case(s):
  new_s = [] # empty list
  def_string = '' # empty string
  for i in range(len(s)): # for loop for each character of the input string
    if s[i].isupper(): # if upper >>> lower
      new_s.append(s[i].lower())
    elif s[i].islower(): # else if lower >>> upper
      new_s.append(s[i].upper())
    else: # else >>> nothing happens
      new_s.append(s[i])

  # from list to string
  for i in range(len(new_s)):
    def_string += new_s[i]

  # return a string
  return def_string

# from HackerRank (not possibile to do in another way on hackerrank)
if __name__ == '__main__':
  s = input()
  result = swap_case(s)
  print(result)

##### String Split and Join

def split_and_join(line):
    list_of_strings = line.split(" ") # line is converted in a list of strings
    return "-".join(list_of_strings) # join the elements of the list by "-"

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

##### What's Your Name?

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    message = "Hello " + first + " " + last + "! You just delved into python."
    print(message)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

##### Mutations

# lists are mutable (they can be changed)
# tuples are immutable (they cannot be changed)

def mutate_string(string, position, character):
  string_in_list = list(string)
  string_in_list[position] = character # modify a single char
  string = ''.join(string_in_list) # join the elements of the list in a new string
  return string

if __name__ == '__main__':
  s = input()
  i, c = input().split()
  s_new = mutate_string(s, int(i), c)
  print(s_new)

##### Find a string

def count_substring(string, sub_string):
  count = 0
  for i in range(len(string)):
    # string[from:to]
    # s.startswith(ss): returns True if s starts with ss
    if string[i:].startswith(sub_string):
      count += 1
  return count

if __name__ == '__main__':
  string = input().strip()
  sub_string = input().strip()

  count = count_substring(string, sub_string)
  print(count)


##### String Validators

if __name__ == '__main__':
  s = input()

  any_alphanumeric = False
  any_alphabetical = False
  any_digits = False
  any_lowercase = False
  any_uppercase = False

  for i in range(len(s)):
    if any_alphanumeric == False and s[i].isalnum() == True: # any alphanumeric
      any_alphanumeric = True
    if any_alphabetical == False and s[i].isalpha() == True: # any alphabetical
      any_alphabetical = True
    if any_digits == False and s[i].isdigit() == True: # any digits
      any_digits = True
    if any_lowercase == False and s[i].islower() == True: # any lowercase
      any_lowercase = True
    if any_uppercase == False and s[i].isupper() == True: # any uppercase
      any_uppercase = True

  print(any_alphanumeric)
  print(any_alphabetical)
  print(any_digits)
  print(any_lowercase)
  print(any_uppercase)


##### Text Alignment

# from HackerRank, with some "variations"
thickness = int(input()) #This must be an odd number (5 in the example)
c = "H"
s = " " # empty char (or "-", or anything else)

#Top Cone
for i in range(thickness):
  # 4 left char + char fixed + 4 right char
  print((c*i).rjust(thickness-1,s)+c+(c*i).ljust(thickness-1,s))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2,s)+(c*thickness).center(thickness*6,s))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6,s))
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2,s)+(c*thickness).center(thickness*6,s))
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness,s)+c+(c*(thickness-i-1)).ljust(thickness,s)).rjust(thickness*6,s))


##### Text Wrap

# import textwrap (it doesn't seem necessary)

def wrap(string, max_width):
  output = [] # empty list
  for i in range(0, len(string), max_width):
    single_line = string[i:i+max_width] # a single line
    output.append(single_line) # append each line at the end of the list
  return('\n'.join(output))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


##### Designer Door Mat

# from hackerrank...
# More than 6 lines of code will result in 0 score. Blank lines are not counted.
N, M = map(int,input().split()) # N:raw M:column

for i in range(1,N,2): # for loop (from,to,step)
    print('---'*((N-i)//2) + '.|.'*i + '---'*((N-i)//2))
print('-'*((M-7)//2) + 'WELCOME' + '-'*((M-7)//2)) # central raw
for i in range(N-2,-1,-2):
    print('---'*((N-i)//2) + '.|.'*i + '---'*((N-i)//2))


##### String Formatting

def print_formatted(number):
  # column width: set to match the width of the binary value of 'number'
  width = len(bin(n)[2:])
  for i in range(1, number+1):
    decimal = str(i).rjust(width) # align to the left
    octal = str(oct(i)[2:]).rjust(width) # first two chars [0][1] are 0o
    hexadecimal = str(hex(i)[2:]).upper().rjust(width) # first two chars [0][1] are 0X
    binary = str(bin(i)[2:]).rjust(width) # first two chars [0][1] are 0b
    print(decimal, octal, hexadecimal, binary)

if __name__ == '__main__':
  n = int(input())
  print_formatted(n) # for example: 17


##### Alphabet Rangoli

def print_rangoli(size):
  # your code goes here
  alphabet = "abcdefghijklmnopqrstuvwxyz" # string with all the letters (good idea)
  sub_alph = alphabet[:size] # substring of alphabet containing the first 'size' letters
  width = 4*size - 3 # total width of the pattern

  # TOP HALF  
  for i in range(size):
    letters_pattern = "-".join(sub_alph[-1-i:])
    
    left_side_letters_pattern = letters_pattern[1:][::-1]
    right_side_letters_pattern = letters_pattern
    print((left_side_letters_pattern + right_side_letters_pattern).center(width,"-"))

  # BOTTOM HALF (same code of the TOP HALF but with for loop reversed: i descendent)
  for i in reversed(range(size-1)):
    letters_pattern = "-".join(sub_alph[-1-i:])
    
    left_side_letters_pattern = letters_pattern[1:][::-1]
    right_side_letters_pattern = letters_pattern
    print((left_side_letters_pattern + right_side_letters_pattern).center(width,"-"))

if __name__ == '__main__':
  n = int(input())
  print_rangoli(n)



##### Capitalize!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
  input_list = s.split(" ") # create a list
  # capitalize each element of the list
  for i in range(len(input_list)):
    input_list[i] = input_list[i].capitalize() 
    
  s = " ".join(input_list) # list >>> string
  
  return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()


##### The Minion Game

def minion_game(string):
  kevin_score = 0
  stuart_score = 0
  for i in range(len(string)):
    if string[i] in 'AEIOU':
      kevin_score += len(string) - i
    else:
      stuart_score += len(string) - i
  if kevin_score > stuart_score:
    print('Kevin', kevin_score)
  elif kevin_score < stuart_score:
    print('Stuart', stuart_score)
  else:
    print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)


##### Merge the Tools!

def merge_the_tools(string, k):
  subsegments_list = [] # empty list for storing the subsegments of the string
  out = "" # empty string (it will be used to accumulate the unique char from each subsegment)
    
  # decomposing the string
  pieces_of_substring = int(len(string)/k)
  for i in range(pieces_of_substring):
    start_index_of_subsegment = i*k
    end_index_of_subsegment = start_index_of_subsegment + k
    subsegments_list.append(string[start_index_of_subsegment:end_index_of_subsegment])

  # choosing unique characters
  for part in subsegments_list: # for each subsegments
    for c in part: # for each character 
      if c not in out: # if c is not already in the 'out' string, it is appended to 'out'
        out += c
    print(out)
    out = "" # re-initialize to "" for the next subsegment

if __name__ == '__main__':
  string, k = input(), int(input())
  merge_the_tools(string, k)


##### Introduction to Sets

def average(array):
  #print(set(array))
  sum_arr = sum(set(array)) # sum of the unique values (set)
  #print(sum_arr)
  len_arr = len(set(array)) # length of the set
  #print(len_arr)
  result = sum_arr/len_arr
  return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


##### Symmetric Difference

m = int(input())
set_m = set(map(int, input().split()))
n = int(input())
set_n = set(map(int, input().split()))

list_sorted = sorted(set_m.symmetric_difference(set_n))
# convert the elements of the list to string,
# then use join and \n to print each string in a new line
print('\n'.join(map(str, list_sorted)))


##### No Idea!

n, m = map(int, input().split())
array_n = list(map(int, input().split())) # n integers, the elements of the array
set_A = set(map(int, input().split())) # m integers, elements of A
set_B = set(map(int, input().split())) # m integers, elements of B

happiness = 0
for i in array_n:
  if i in set_A:
    happiness += 1
  elif i in set_B:
    happiness -= 1

print(happiness)


##### Set .add()

n = int(input())
country_stamps = set() # empty set
for i in range(n):
  country_stamps.add(input()) # each input (string) is added in the country_stamps set

print(len(country_stamps))


##### Set .discard(), .remove() & .pop()

n = int(input()) # number of elements in the set s
s = set(map(int, input().split())) # elements of the set s
n_commands = int(input()) # number of commands
for i in range(n_commands):
  command = input().split()
  #print(type(command))
  if command[0] == 'pop':
    s.pop()
  elif command[0] == 'remove':
    s.remove(int(command[1]))
  elif command[0] == 'discard':
    s.discard(int(command[1]))

print(sum(s)) # print the sum of the elements of set s


##### Set .union() Operation

n = int(input()) # number of subscribers (English newspaper)
# set of roll numbers of English newspapers subscribers
set_roll_n_Eng = set(map(int, input().split()))
b = int(input()) # number of subscribers (French newspaper)
# set of roll numbers of French newspapers subscribers
set_roll_b_Fr = set(map(int, input().split()))

# print the number of students who have subscribed to at least one newspaper
print(len(set_roll_n_Eng.union(set_roll_b_Fr)))


##### Set .intersection() Operation

n = int(input()) # number of students who have subscribed to the English newspaper
# set of roll numbers of English newspapers subscribers
set_roll_n_Eng = set(map(int, input().split()))
b = int(input()) # number of students who have subscribed to the French newspaper
# set of roll numbers of French newspapers subscribers
set_roll_b_Fr = set(map(int, input().split()))

# print the number of students who have subscribed to both newspapers
print(len(set_roll_n_Eng.intersection(set_roll_b_Fr)))


##### Set .difference() Operation

n = int(input()) # number of students who have subscribed to the English newspaper
# set of roll numbers of English newspapers subscribers
set_roll_n_Eng = set(map(int, input().split()))
b = int(input()) # number of students who have subscribed to the French newspaper
# set of roll numbers of French newspapers subscribers
set_roll_b_Fr = set(map(int, input().split()))

# print the number of students who have subscribed to only English newspapers
print(len(set_roll_n_Eng.difference(set_roll_b_Fr)))


##### Set .symmetric_difference() Operation

n = int(input()) # number of students who have subscribed to the English newspaper
# set of roll numbers of English newspapers subscribers
set_roll_n_Eng = set(map(int, input().split()))
b = int(input()) # number of students who have subscribed to the French newspaper
# set of roll numbers of French newspapers subscribers
set_roll_b_Fr = set(map(int, input().split()))

# print the number of students who have subscribed to
# the English or the French newspapers but not both
print(len(set_roll_n_Eng.symmetric_difference(set_roll_b_Fr)))


##### Set Mutations

n_in_A = int(input()) # number of elements in set A
set_A = set(map(int, input().split())) # elements of set A
n_other_sets = int(input()) # number of other sets
for i in range(n_other_sets):
  command = input().split() # first line: space separated entries...
  set_other = set(map(int, input().split())) # second line: space separated list...

  if command[0] == 'intersection_update':
    set_A.intersection_update(set_other)
  elif command[0] == 'update':
    set_A.update(set_other)
  elif command[0] == 'symmetric_difference_update':
    set_A.symmetric_difference_update(set_other)
  elif command[0] == 'difference_update':
    set_A.difference_update(set_other)

print(sum(set_A))


##### The Captain's Room

k = int(input()) # size of each group
room_list = list(map(int, input().split())) # list of room numbers

# for loop: each element of room_list is checked
for i in set(room_list):
  room_list.remove(i) # find and remove the first element with value i
  # if there aren't others elements with value i...
  if i not in room_list: # ... we find the captain's room number
    print(i)
    break


##### Check Subset
n_test_cases = int(input()) # number of test cases

for i in range(n_test_cases):
  n_elements_A = int(input()) # number of elements in set A
  elements_in_A = set(map(int, input().split())) # elements of set A
  n_elements_B = int(input()) # number of elements in set B
  elements_in_B = set(map(int, input().split())) # elements of set B

  if elements_in_A.issubset(elements_in_B):
    print(True)
  else:
    print(False)


##### Check Strict Superset

elements_in_A = set(map(int, input().split())) # elements of set A
n_other_sets = int(input()) # number of other sets
for i in range(n_other_sets):
  set_other = set(map(int, input().split())) # space separated elements of the other sets
  if not elements_in_A.issuperset(set_other):
    print(False)
    break
  elif i == n_other_sets - 1:
    print(True)


##### collections.Counter()

# collections.Counter()
# A counter is a container that stores elements as dictionary keys,
# and their counts are stored as dictionary values.

from collections import Counter

n_of_shoes = int(input()) # numer of shoes
list_of_sizes = list(map(int, input().split())) # list of all the shoe sizes in the shop
n_of_customers = int(input()) # number of customers
#print(list_of_sizes)
counter = Counter(list_of_sizes)
#print(counter)

# output: print the amount of money earned
money_earned = [] # empty list
#print(type(money_earned))

for i in range(n_of_customers):
    size, price = map(int, input().split())
    if counter[size] > 0:
        money_earned.append(price)
        counter[size] -= 1


##### DefaultDict Tutorial

from collections import defaultdict

size_n_of_groupA, size_m_of_groupB = map(int, input().split())

groupA = []
groupB = []

for i in range(size_n_of_groupA):
  groupA.append(input())

for i in range(size_m_of_groupB):
  groupB.append(input())

#print(groupA)
#print(groupB)

positions = defaultdict(list) # empty defaultdict
#print(positions)
for i in range(len(groupA)):
    # for each word in groupA, appends its index to the corresponding list
    # in the defaultdict positions
    positions[groupA[i]].append(i+1) # index i+1, as requested by the problem

for word in groupB:
    # for each word in groupB, checks if the word exists as a key in the defaultdict
    if word in positions:
        print(" ".join(map(str, positions[word])))
    else:
        print(-1)


##### Collections.namedtuple()

from collections import namedtuple

number_of_students = int(input())
columns_names = input().split()
total_marks = 0
for i in range(number_of_students):
    students = namedtuple('student', columns_names)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)

print((total_marks / number_of_students))


##### Collections.OrderedDict()

from collections import OrderedDict

ordered_dictionary = OrderedDict()  # empty OrderedDict

number_of_items = int(input())

for i in range(number_of_items):
  items = input().split()
  item_name = " ".join(items[:-1]) # all the items, except the last one, are part of the name
  item_price = int(items[-1]) # the last item is the price

  # if the key 'item_name' exists, it will retrieve the current value
  # if not, it will create a new entry with the key 'item_name'
  # get(item_name,0): 'get' method for the OrderedDict to retrieve the value associated with the key item:name
  # The second argument, 0, is the default value that will be returned if the key doesn't exist
  ordered_dictionary[item_name] = ordered_dictionary.get(item_name, 0) + item_price

for item_name, item_price in ordered_dictionary.items():
  print(item_name, item_price)


##### Word Order

n = int(input())
words = [] # list to store words from the input()
for i in range(n):
    word = input()
    words.append(word)

words_dictionary = {} # empty dictionary
for word in words:
    # Uses the get method of the dictionary to retrieve the current frequency of the word.
    # If the word doesn't exist, it sets the frequency to 0.
    # +1 at the end --> increments the frequency of the word by 1
    words_dictionary[word] = words_dictionary.get(word, 0) + 1

print(len(words_dictionary)) # the length of the dictionary IS the number of unique words
for element in words_dictionary.values():
    print(element, end=" ")


##### Collections.deque()

from collections import deque
# double-ended queue

d = deque()
n = int(input())
for i in range(n):
  command = input().split()

  if command[0] == 'append':
    d.append(int(command[1]))
  elif command[0] == 'appendleft':
    d.appendleft(int(command[1]))
  elif command[0] == 'pop':
    d.pop()
  elif command[0] == 'popleft':
    d.popleft()

print(*d)
## or, alternatively...
#for element in d:
#  print(element)


##### Company Logo

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
  s = input()
  s_sorted = sorted(s) # list (ordering each character of the string s)

  # frequency_tab is a Counter object
  # (for counting the occurrences of each character in the input string)
  frequency_tab = Counter(list(s_sorted))

  # using for loop to print the three words with frequency
  # most_common(3): return the top 3 items based on their values in descending order
  # for k, v in each tuple in the list
  for k, v in frequency_tab.most_common(3):
    print(k, v)


##### Calendar Module

import calendar
m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())


##### Time Delta

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
  # string format for strptime method (for parsing a string)
  # from example: Sun 10 May 2015 13:54:36 -0700
  #               %a  %d  %b  %Y  %H:%M:%S  %z (UTC offset in the form +/-HHMM)
  string_format = '%a %d %b %Y %H:%M:%S %z'
  t1 = datetime.strptime(t1, string_format)
  t2 = datetime.strptime(t2, string_format)
  return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()


##### Exceptions

number_of_test_cases = int(input())
for _ in range(number_of_test_cases):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)


##### Zipped!

# zip([iterable, ...])
# return a list of tuples
# the i-th tuple contains the i-th element
# from each of the argument sequences or iterables

#print(zip([1,2,3,4,5,6],'Hacker'))
#print(list(zip([1,2,3,4,5,6],'Hacker')))

n, x = map(int, input().split())
scores = []
for _ in range(x):
    # append in scores[] the grades (all in one input line, separated by space)
    scores.append(map(float, input().split()))

#print(list(zip(*scores)))
for i in zip(*scores):
    print(sum(i)/len(i))



##### Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
  nm = input().split()
  n = int(nm[0])
  m = int(nm[1])

  arr = [] # empty list
  # read a two dimensional matrix of integers from the input
  # and store it in a list, "arr" in this case
  for _ in range(n):

    # repetita iuvant

    # input(): reads a line of in put
    # rstrip(): remove trailing whitespaces from the input string
    # split(): splits the input string into a list of substrings (whitespace as delimiter)
    # map(int, ...): applies the 'int' function to...
    # ... each element of the list returned by split()
    # list(): convert the result of map(), a map object, into a list
    arr.append(list(map(int, input().rstrip().split())))

  k = int(input()) # k starts from 0 (first column = 0)

  # sort the matrix (list of lists) with the sorting criterion...
  # ... specified by 'key=lamba x: x[k]' ...
  # ... it uses a lambda function to extract the element at index k from each sublist
  # in this way we can sort the matrix by the values in the k-th column
  for i in sorted(arr, key=lambda x: x[k]):
    print(*i) # unpacks the elements of the sublist i and prints them



##### ginortS

s = input()
list_s = list(s)
# for categorize each alphanumeric characters
list_s_lowercase = []
list_s_uppercase = []
list_s_odd = []
list_s_even = []
# for loop to categorize each alphanumeric characters
for i in range(len(list_s)):
  if list_s[i].islower():
    list_s_lowercase.append(list_s[i])
  elif list_s[i].isupper():
    list_s_uppercase.append(list_s[i])
  elif list_s[i].isdigit():
    if int(list_s[i]) % 2 == 0:
      list_s_even.append(list_s[i])
    else:
      list_s_odd.append(list_s[i])

# output string
list_sorted = sorted(list_s_lowercase) + sorted(list_s_uppercase) + sorted(list_s_odd) + sorted(list_s_even)
print(''.join(list_sorted))



##### Map and Lambda Function

######################################################
# The map() function applies a function to every member of an iterable
# and returns the result. It takes two parameters: first, the function
# that is to be applied and secondly, the iterables.

#Let's say you are given a list of names, and you have
# to print a list that contains the length of each name.

#print (list(map(len, ['Tina', 'Raj', 'Tom'])))
######################################################

######################################################
# Lambda is a single expression anonymous function often used as an inline function.
# In simple words, it is a function that has only one line in its body.
# It proves very handy in functional and GUI programming.

#sum_with_lambda = lambda a, b, c: a + b + c
#print(sum_with_lambda(1, 2, 3)) # result: 6
######################################################

#cube = lambda x: # complete the lambda function
cube = lambda x: x**3

fibonacci_list = [] # empty list
def fibonacci(n):
  # return a list of fibonacci numbers
  # i=0, i=1 fixed; we start calculus with i=2
  for i in range(n):
    if i == 0:
      fibonacci_list.append(0)
    elif i == 1:
      fibonacci_list.append(1)
    else:
      fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
  return fibonacci_list

if __name__ == '__main__':
  n = int(input())
  print(list(map(cube, fibonacci(n))))


##### Detect Floating Point Number

import re

for _ in range(int(input())):
  # bool(), boolean value: true (match) or false (doesn't match)
  # RegEx rules:
  # ^ : matches the beginning of the string
  # [-+]? : matches an optional sign, '-' or '+'
  # [0-9]* : matches zero or more occurences of digits 0-9
  # \. : matches a literal dot '.'
  # [0-9]+ : matches one or more occurences of digits 0-9
  # $ : matches the end of the string
  print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))


##### Re.split()

import re

# the re.split() expression splits the string by occurrence of a pattern.
print(re.split(r"-","+91-011-2711-1111"))
# RESULT: ['+91', '011', '2711', '1111']

#regex_pattern = r""	# Do not delete 'r'.
regex_pattern = r"[,.]"
print("\n".join(re.split(regex_pattern, input())))


##### Group(), Groups() & Groupdict()

import re

# re.search() search for the first occurence of a pattern
# ([a-zA-Z0-9]) : captures a single alphanumeric into a capturing group (group 1)
# \1 : this refers to the character captured in group 1. It checks if the same
#       character appears immediately after the captured one
m = re.search(r'([a-zA-Z0-9])\1', input())
print(m.group(1) if m else -1) # if m else -1: if m is not None (a match was found)
                               # it prints the captured character. Otherwise, it prints -1



##### Re.findall() & Re.finditer()

import re

s = input()
# re.findall: returns a list of all matching substrings
# (?<=[^aeiouAEIOU]) : ensures that the match is preceded (?<=) by a non-vowel character [^aeiouAEIOU]
# ([aeiouAEIOU]{2,}) : captures two or more consecutive vowels (case-insensitive) into a capturing group
# (?=[^aeiouAEIOU]) : ensures that the match is followed by a non-vowel character
for m in re.findall(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])', s):
    print(m)
if not re.findall(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])', s):
    print(-1)


##### Re.start() & Re.end()

import re

s_string = input()
k_substring = input()

all_matches = [] # empty list to store tuples (start and end indices of found substring)
start = 0 # to keep track of the starting position for subsquent searches
while True:
  start = s_string.find(k_substring, start)
  if start == -1: # no more occurences found >>> break
    break
  end = start + len(k_substring) # calculates the ending index of the substring
  all_matches.append((start, end)) # append a tuple containing (start,end) index
  start += 1 # increment variable to move to the next character

if all_matches: # if the list is not empty (at least one occurence was found)
  for match in all_matches:
    print(match[0], match[1])
else:
  print("(-1, -1)")


##### Regex Substitution

n = int(input())
for _ in range(n):
  line = input()
  while ' && ' in line or ' || ' in line:
    line = line.replace(" && ", " and ").replace(" || ", " or ")
  print(line)


##### Validating Roman Numerals

#regex_pattern = r""	# Do not delete 'r'.
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"


import re
print(str(bool(re.match(regex_pattern, input()))))


##### Validating phone numbers

import re

n_of_inputs = int(input())
for _ in range(n_of_inputs):
  phone_number = input()
  if re.match(r'^[789]\d{9}$', phone_number):
    print("YES")
  else:
    print("NO")


##### Validating and Parsing Email Addresses

import re
import email.utils

n_of_email_addresses = int(input())
for i in range(n_of_email_addresses):
  name, email_address = email.utils.parseaddr(input())
  if re.match(r'^[a-zA-Z][\w\.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email_address):
    print(email.utils.formataddr((name, email_address)))


##### Hex Color Code

import re

color_codes = []

number_of_code_lines = int(input())
for _ in range(number_of_code_lines):
  css_code_lines = input()
  # to find all matches of the specified regex within the css_code_lines string
  # r'(?<!^)(#(?:[\da-fA-F]{3}){1,2})' : matches hexadecimal color codes (that are not at the beginning of the line)
  matches = re.findall(r'(?<!^)(#(?:[\da-fA-F]{3}){1,2})', css_code_lines)
  if matches:
    color_codes.extend(matches) # extends color_codes list with the extracted color_codes

for code in color_codes:
  print(code)


##### HTML Parser - Part 1

from html.parser import HTMLParser

# MyHTMLParser: name of the subclass of HTMLParser
# creation of a subclass... and override the handler methods
class MyHTMLParser(HTMLParser):
  # This method is called to handle the start tag of an element.
  # (For example: <div class='marks'>)
  # The tag argument is the name of the tag converted to lowercase.
  # The attrs argument is a list of (name, value) pairs containing...
  # ... the attributes found inside the tag's <> brackets.
  def handle_starttag(self, tag, attrs):
    #print("from handle_starttag method:")
    print("Start :", tag)
    for attr in attrs:
      print("->", attr[0], ">", attr[1])

  # This method is called to handle the end tag of an element.
  # (For example: </div>)
  # The tag argument is the name of the tag converted to lowercase.
  def handle_endtag(self, tag):
    #print("from handle_endtag method:")
    print("End   :", tag)

  # This method is called to handle the empty tag of an element.
  # (For example: <br />)
  # The tag argument is the name of the tag converted to lowercase.
  # The attrs argument is a list of (name, value) pairs containing...
  # the attributes found inside the tag's <> brackets.
  def handle_startendtag(self, tag, attrs):
    #print("from handle_startendtag:")
    print("Empty :", tag)
    for attr in attrs:
      print("->", attr[0], ">", attr[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
number_of_lines = int(input())
for _ in range(number_of_lines):
  line = input()
  parser.feed(line)


##### HTML Parse - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  # This method is called when a comment is encountered
  # (e.g. <!--comment-->).
  # The data argument is the content inside the comment tag
  def handle_comment(self, data):
    if '\n' in data:
      print('>>> Multi-line Comment')
    else:
      print('>>> Single-line Comment')
    print(data)

  # This method is called to process arbitrary data
  # (e.g. text nodes and the content of <script>...</script> and <style>...</style>).
  # The data argument is the text content of HTML
  def handle_data(self, data):
    if data != '\n':
      print('>>> Data')
      print(data)

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()


##### Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print(tag)
    for attr in attrs:
      print("->", attr[0], ">", attr[1])

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)



##### Validating UID

import re

number_of_test_cases = int(input())
for _ in range(number_of_test_cases):
  uid = input()

  # valid uid conditions
  at_least_2_uppercase = bool(re.search(r'[A-Z]{2}', uid))
  at_least_3_digits = bool(re.search(r'[0-9]{3}', uid))
  only_alphanumeric = bool(re.match(r'^[a-zA-Z0-9]*$', uid))
  # using 'set' : collection of unique elements (any characters will be removed creating the set)
  exactly_10_char_and_no_repeated = bool(len(set(uid)) == 10)

  if at_least_2_uppercase and at_least_3_digits and only_alphanumeric and exactly_10_char_and_no_repeated:
    print("Valid")
  else:
    print("Invalid")


##### Validating Credit Card Numbers

import re

n = int(input())
for _ in range(n):
  card_number = input()

  # ^[456]\d{3} : first element is 4 or 5 or 6, then three digits
  # (-?\d{4}){3} : three groups of optionally hyphen-separated four digits numbers
  if re.match(r'^[456]\d{3}(-?\d{4}){3}$', card_number):
    # checks for four consecutive identical digits (excluding the first digit)
    if not re.search(r'(\d)\1{3}', card_number.replace('-', '')):
      print('Valid')
    else:
      print('Invalid')
  else:
    print('Invalid')



##### Validating Postal Codes

#regex_integer_in_range = r"_________"	# Do not delete 'r'.
# from 100000 to 999999
regex_integer_in_range = r"^[1-9][0-9]{5}$"
#regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.
# matches alternating repetitive digit pairs
# \d captures a digit in a group
# (?=\d\1) positive lookahead assertion that checks if the captured digit
# is followed by another digit and the the same captured digit
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

# positive lookahead
# syntax: (?=pattern)
# example
# text = "singing, dancing, running, walking"
# matches = re.findall(r"\w+(?=ing)", text) [\w matches one or more word characters]
# print(matches) >>> Output: ['sing', 'danc', 'runn', 'walk']

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


##### Matrix Script

import re

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(input())

# Transpose Matrix (not my idea, sadly)

"""
1. Unpacks 'data' list
2. Creates tuples of corresponding elements

example.

original matrix
[
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

transposed matrix
[
    ['a', 'd', 'g'],
    ['b', 'e', 'h'],
    ['c', 'f', 'i']
]

zip(*data) creates the following tuples:
(('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i'))

3. Iterates over the tuples [  for elem in zip(*data)  ]
elem takes values ('a', 'd', 'g') and so on...

4. Concatenates elements into a string
string += ''.join(elem)
('a', 'd', 'g') --> string 'adg'
"""

# Transpose Matrix
string = ''
for elem in zip(*data): # zip(*data) : column --> raw (tuples)
    string += ''.join(elem) # concatenates elements into string

# matches any non-word characters (no whitespace) that are
# preceded and followed by word characters
print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', string))



##### XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
  # your code goes here
  # calculates the total number of attributes and return it
  # len(child.attrib) : retrieves the number of attributes present within a single child node
  # for child in node.iter(): iterates over all descendant nodes of the given node,
  #                           including direct children, grandchildren, and so on.
  return sum(len(child.attrib) for child in node.iter())

if __name__ == '__main__':
  sys.stdin.readline()
  xml = sys.stdin.read()
  tree = etree.ElementTree(etree.fromstring(xml))
  root = tree.getroot()
  print(get_attr_number(root))



##### XML2 - Find the Maximum Depth

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for i in elem:
        depth(i, level) #recalls this function

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


##### Standardize Mobile Number Using Decorators

# the 'wrapper' decorator modifies the 'sort_phone' function to format
# the phone numbers in a specific format before sorting

def wrapper(f):
  def fun(l):
    # complete the function
    # For each element n, formats the phone number using '+91 {} {}'.
    # The -10:-5 and -5: slicing extracts the last 5 digits and the last 5 digits,
    # respectively, to create the desired format.
    # The formatted phone numbers are passed as an argument
    # to the original function f.
    f('+91 {} {}'.format(n[-10:-5], n[-5:]) for n in l)
  return fun

@wrapper
def sort_phone(l):
  print(*sorted(l), sep='\n')

if __name__ == '__main__':
  l = [input() for _ in range(int(input()))]
  sort_phone(l)



##### Decorators 2 - Name Directory

import operator
from operator import itemgetter # Import itemgetter from operator module

def person_lister(f):
  def inner(people):
    # complete the function

    people.sort(key=itemgetter(2))
    return (f(person) for person in people)

    #return [f(person) for person in sorted(people, key=operator.itemgetter(2))]

  return inner

@person_lister
def name_format(person):
  return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
  people = [input().split() for i in range(int(input()))]
  print(*name_format(people), sep='\n')


##### Arrays

import numpy

# Arrays
# A NumPy array is a grid of values. They are similar to lists,
# except that every element of an array must be the same type.

def arrays(arr):
    # complete this function
    # use numpy.array
    # numpy.array() is used to convert a list into a NumPy array
    return numpy.array(arr[::-1], float) # arr[::-1] reverses the order in the 'arr' list

arr = input().strip().split(' ')
result = arrays(arr)
print(result)



##### Shape and Reshape

import numpy

line_9_numbers = input().strip().split(' ')
# numpy.array() is used to convert a list into a NumPy array
array_9_numbers = numpy.array(line_9_numbers, int)
print(numpy.reshape(array_9_numbers, (3, 3)))



##### Transpose and Flatten

import numpy

array = []
n, m = map(int, input().split())
for _ in range(n):
  line = input().strip().split()
  array.append(line)

array_numpy = numpy.array(array, int)
print(numpy.transpose(array_numpy))
print(array_numpy.flatten())



##### Concatenate

import numpy

array_elements_N = []
array_elements_M = []

rows_N, rows_M, cols_P = map(int, input().split())
for _ in range(rows_N):
  line_of_P_cols = input().strip().split()
  array_elements_N.append(line_of_P_cols)

for _ in range(rows_M):
  line_of_P_cols = input().strip().split()
  array_elements_M.append(line_of_P_cols)

array_elements_N_numpy = numpy.array(array_elements_N, int)
array_elements_M_numpy = numpy.array(array_elements_M, int)

print(numpy.concatenate((array_elements_N_numpy, array_elements_M_numpy), axis=0))


##### Zeros and Ones

import numpy

dimension = list(map(int, input().split()))
#print(numpy.zeros(dimension, dtype=numpy.int)) # (deprecated)
#print(numpy.ones(dimension, dtype=numpy.int)) # (deprecated)
print(numpy.zeros(dimension, dtype=int))
print(numpy.ones(dimension, dtype=int))



##### Eye and Identity

import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
print(numpy.eye(n, m))



##### Array Mathematics

import numpy

array_A = [] # empty list
array_B = [] # empty list

N_r, M_c = map(int, input().split())
for _ in range(N_r):
  line_of_A = input().strip().split()
  array_A.append(line_of_A)
for _ in range(N_r):
  line_of_B = input().strip().split()
  array_B.append(line_of_B)

arr_A_numpy = numpy.array(array_A, int)
arr_B_numpy = numpy.array(array_B, int)

print(numpy.add(arr_A_numpy, arr_B_numpy))
print(numpy.subtract(arr_A_numpy, arr_B_numpy))
print(numpy.multiply(arr_A_numpy, arr_B_numpy))
print(numpy.floor_divide(arr_A_numpy, arr_B_numpy))
print(numpy.mod(arr_A_numpy, arr_B_numpy))
print(numpy.power(arr_A_numpy, arr_B_numpy))


##### Floor, Ceil and Rint

import numpy
numpy.set_printoptions(legacy='1.13')

array_elements = list(map(float, input().split()))
arr_numpy = numpy.array(array_elements)
print(numpy.floor(arr_numpy))
print(numpy.ceil(arr_numpy))
print(numpy.rint(arr_numpy))


##### Sum and Prod

import numpy

array_elements = []
N_r, M_c = map(int, input().split())
for _ in range(N_r):
  elements = input().strip().split()
  array_elements.append(elements)

arr_numpy = numpy.array(array_elements, int)

# Compute the sum along axis. Then, print the product of that sum.
print(numpy.prod(numpy.sum(arr_numpy, axis=0)))



##### Min and Max

import numpy

N, M = map(int, input().split())
array_elements = []
for _ in range(N):
  elements = input().strip().split()
  array_elements.append(elements)

arr_numpy = numpy.array(array_elements, int)
print(numpy.max(numpy.min(arr_numpy, axis=1)))



##### Mean, Var, and Std

import numpy

N, M = map(int, input().split())
array_elements = []
for _ in range(N):
  elements = input().strip().split()
  array_elements.append(elements)

arr_numpy = numpy.array(array_elements, int)
print(numpy.mean(arr_numpy, axis=1))
print(numpy.var(arr_numpy, axis=0))
#print(numpy.std(arr_numpy, axis=None))
# with round(), otherwise we get error on hackerrank
print(numpy.std(arr_numpy, axis=None).round(11))



##### Dot and Cross

import numpy

array_A = []
array_B = []

N = int(input())
for _ in range(N):
  elements_A = input().strip().split()
  array_A.append(elements_A)
for _ in range(N):
  elements_B = input().strip().split()
  array_B.append(elements_B)

arr_A_numpy = numpy.array(array_A, int)
arr_B_numpy = numpy.array(array_B, int)

print(numpy.dot(arr_A_numpy, arr_B_numpy))



##### Inner and Outer

import numpy

elem_A = input().strip().split()
elem_B = input().strip().split()

A_numpy = numpy.array(elem_A, int)
B_numpy = numpy.array(elem_B, int)

print(numpy.inner(A_numpy, B_numpy))
print(numpy.outer(A_numpy, B_numpy))



##### Polynomials

import numpy

coeff_of_P = list(map(float, input().split()))
x_value = int(input())

print(numpy.polyval(coeff_of_P, x_value))



###### Linear Algebra

import numpy

array_elements = []

N = int(input())
for _ in range(N):
  elements = input().strip().split()
  array_elements.append(elements)

arr_numpy = numpy.array(array_elements, float)
print(numpy.linalg.det(arr_numpy).round(2))







##### Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
  # Write your code here
  # find the max value in the candles list and count it in the list
  return candles.count(max(candles))

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  candles_count = int(input().strip())
  candles = list(map(int, input().rstrip().split()))
  result = birthdayCakeCandles(candles)
  fptr.write(str(result) + '\n')
  fptr.close()




###### Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
  # Write your code here

  # kangaroo 1 : position after N jumps = x1 + v1*N
  # kangaroo 2 : position after N jumps = x2 + v2*N
  # we need to check if there is an N such that:
  # x1 + v1*N = x2 + v2*N
  # ---> N = (x2-x1)/(v1-v2)
  # N can only be an integer, so our conditions to say YES is:
  # (x2-x1) % (v2-v1) = 0

  if v1 <= v2:
    return "NO"
  if (x2 - x1) % (v2 - v1) != 0:
    return "NO"
  return "YES"

  # a simple solution (step by step verification of a "long" run),
  # ... but not efficient
  #for i in range(10000):
  #  if x1 + v1 * i == x2 + v2 * i:
  #    return "YES"
  #return "NO"

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  first_multiple_input = input().rstrip().split()
  x1 = int(first_multiple_input[0])
  v1 = int(first_multiple_input[1])
  x2 = int(first_multiple_input[2])
  v2 = int(first_multiple_input[3])
  result = kangaroo(x1, v1, x2, v2)
  fptr.write(result + '\n')
  fptr.close()



##### Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
  # Write your code here

# example (n=5)
# Day Shared Liked Cumulative
# 1      5     2       2
# 2      6     3       5
# 3      9     4       9
# 4     12     6      15
# 5     18     9      24

  shared = 5 # number of people who shared the ad on the first day
  cumulative = 0
  # for loop from the first day
  for i in range(n):
    liked = shared // 2
    cumulative += liked
    shared = liked * 3
  return cumulative

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  n = int(input().strip())
  result = viralAdvertising(n)
  fptr.write(str(result) + '\n')
  fptr.close()



##### Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
  # Write your code here
  #print(type(n))

  p = n*k # number p is created by concatenating 'k' times the string 'n'
  super_digit = 0
  for i in range(len(p)):
    super_digit += int(p[i])

  # if length of super_digit > 1 then it recursively calls superDigit function
  if len(str(super_digit)) > 1:
    return superDigit(str(super_digit), 1) # superDigit accepts (str,int) as arguments
  return super_digit

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  first_multiple_input = input().rstrip().split()
  n = first_multiple_input[0]
  k = int(first_multiple_input[1])
  result = superDigit(n, k)
  fptr.write(str(result) + '\n')
  fptr.close()




##### Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
  # Write your code here
  test_value = arr[n-1] # last element of arr

  i = n-2 # 'while' loop iterates from the second-to-last element (i=n-2)...
          # ... down to the first element
  while i >= 0:
    if test_value < arr[i]:
      arr[i+1] = arr[i]
      print(*arr, sep = " ")
    else: # (test_value has found its correct position --> break the while)
      break
    i -= 1
  arr[i+1] = test_value
  print(*arr, sep = " ")

if __name__ == '__main__':
  n = int(input().strip())
  arr = list(map(int, input().rstrip().split()))
  insertionSort1(n, arr)



##### Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
  # Write your code here
  # for loop starting from the second element (index 1)
  for i in range(1, n):
    # Pick the current element and its index
    current_element = arr[i]
    current_index = i

    # Shift elements to the right while they are greater than the current element
    while current_index > 0 and arr[current_index-1] > current_element:
      arr[current_index] = arr[current_index-1]
      current_index -= 1

    # Insert the current element at its correct position
    arr[current_index] = current_element

    # Print the current state of the array after each iteration
    print(*arr)

if __name__ == '__main__':
  n = int(input().strip())
  arr = list(map(int, input().rstrip().split()))
  insertionSort2(n, arr)


