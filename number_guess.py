import math
import random


v1 = int(input("Select a number from : "))
v2 = int(input("To : "))
lst = []
if not lst:
    lst.append(v1)
    while (v1) < (v2) :
     v1 = (v1)+1
     lst.append(v1)

num = random.choice(lst)

for i in lst:
 guess = int(input ("guess the number :"))

 if guess < num :
   print ("too low")
   continue
 elif guess > num :
     print ('too high')
     continue 
  
 elif guess == num :
   print ('correct')
   exit() 