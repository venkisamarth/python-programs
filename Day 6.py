# # program to check if a number is possitve of negative 
# number=5 
# if number>0: 
#  print("The number is posstive")
# else: 
#  print("Negative")

# # check if a string is empty 
# string=""
# if not string: 
#  print("The stirng is empty")

# # check if peson id an adult 
# age=20 
# if age>=18: 
#  print("The person id an adult")

#  # check if a n item is in a list 
# item ="apple"
# fruits=['apple',"banana","cherry"]
# if item in fruits: 
#  print("The item is in the list")

# # chekc if  year is a leap year(simple version)
# year =2024
# if year % 4 ==0: 
#  print("It's a leap year")
# use if else statmets 
# check if a numbers is even or odd

# check if a numer is prime or not 
number =17 
is_prime=True
if number >1: 
  for i in range(2,number): 
    if number % i==0: 
     is_prime=False
     break 
  
if is_prime: 
 print("The number is prime.")

 #check if year is a leap year (compoles version )
year=2014
if (year %4 ==0 and year%100 !=0) or (year %400==0): 
  print("It is a leap year")

# check of the character is a vowel
char ='e'
if char in "aeiouAEIOU": 
  print("This character is a vowel.")
# check if a list is sorted in ascnding order 
list1=[1,2,3,4,4]
is_sorted=True
for i in range(len(list1)-1):
  if list1[i] >list1[i+1]:
    is_sorted =False
    break 
  if is_sorted:
    print("The list is sorted in ascending order.")
# check if a number is a perfect square 
import math 
number =16 
if math.isaqrt(number) **2==number:
  print("The number is a perfect square.")
# us if else statments  
#find the largest of two numbers 
a=5
b=10 
if a>b:
  print(f"{a} is largest than {b}.")
else: 
  print(f"{b} is larger than {a}.")

  

