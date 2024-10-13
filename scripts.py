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


