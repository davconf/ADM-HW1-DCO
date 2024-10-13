# Say "Hello, World!" with Python

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

