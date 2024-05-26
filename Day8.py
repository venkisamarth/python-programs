# # determin the largest of three numbers using funciton 
# def largest_of_three(a,b,c): 
#     if a>=b:
#         if a>c: 
#             print(a)
#         else: 
#             print(c)
#     else: 
#         if b>c: 
#             print(b)
#         else: 
#             print(c)
# print(largest_of_three(10,20,30))

# # without funtion 
# a,b,c=10,20,30
# if a>=b: 
#     if a>=c: 
#         print(a)
#     else: 
#         print(c)
# else:
#      if b>c: 
#          print(b)
#      else: 
#          print(c)
# print(largest_of_three(1,20,30))
# # check the give year is leap year or not 
# def is_leap_year(year): 
#     if year% 4==0: 
#         if year%100==0: 
#             if year %400==0: 
#                 return True
#             else: 
#                 return False
#         else: 
#             return True 
#     else: 
#         return False 
# # Test the fucnitn 
# year =2024 
# if  is_leap_year(year):
#     print(f"{year} if a leap year")
# else: 
#     print(f"{year} if not a leap year")

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# # Test the function
# year = 2024
# if is_leap_year(year):
# #     print(f"{year} is a leap year.")
# # else:
# #     print(f"{year} is not a leap year.")
# # # without using funciton 
# # year =2024 
# # if year %4==0: 
# #     if year%100 ==0: 
# #         if year%400==0:
# #             print(f'{year} is leap year')
# #         else:
# #             print(f"{year} is not leap year")
# #     else:
# #         print(f"{year} is sleap year")
# # else:
# #     print(f"{year} is not leep year")

# def determain_grade(marks): 
#     if marks >=90: 
#         return "A"
#     else: 
#         if marks >=80: 
#             return "B"
#         else:
#             if marks>=70:
#                 return "c"
#             else: 
#                 if marks>=60: 
#                     return "D"
#                 else: 
#                     if marks>=50 : 
#                         return "E"
#                     else:
#                         return "F"
# marks=85
# grade=determain_grade(marks)
# print(f"The grade for marks {marks} if {grade}.")
# without Funciton 
# # To deetermain grade 
# #wihtout funciton 
# marks=85 
# if marks>=90:
#    print("grade is A")
# else:
#     if marks>=80:
#         grade="B"
#     else:
#         if marks>=70:
#             grade="c"
#         else:
#             if marks>=60:
#                 grade="D"
#             else: 
#                 if marks >="50": 
#                     grade="E"
#                 else:
#                     grade="F"
# print(f"The grade for marks{marks} is {grade}")

#without funciton 
import math  
# # def find_roots(a,b,c): 
# #     disciminant=b**2-4*a*c
# #     if disciminant >0: 
# #         root1 =(-b+math.sqrt(disciminant))/(2*a)
# #         root2=(-b-math.sqrt(disciminant)/(2*a))
# #         return  ("Two distict real roots",root1,root2)
# #     else: 
# #         if disciminant==0: 
# #             root=-b/(2*a)
# #             return("Two equal roots",root,root)
# #         else:
# #             real_part=-b/(2*a)
# #             imaginary_part=math.sqrt(-disciminant)/(2*a)
# #             return ("Two complex roots",complex(real_part,imaginary_part),complex(real_part,-imaginary_part))
# # Test the funciton 
# a,b,c=1,-3,2
# restult =find_roots(a,b,c)
# print(f"{restult[0]}:{restult[1],{restult[2]}}") 
# # import math 
# a,b,c=1,-3,2 
# discriminant=b**2-4*a*c

# if discriminant>0:
#     root1=(-b+math.sqrt(discriminant))
#     root2=(-b-math.sqrt(discriminant))/(2*a)
# else:
#     if discriminant==0:
# #         root=-b/(2*a)
# #         print(f"Two equal real roots:",{root},{root})
# #     else:
# #         real_part=-b/(2*a)
# #         imaginary_part=math.sqrt(discriminant)/(2*a)
# #         print(f"Two complex roots: {complex(real_part,imaginary_part)},{complex(real_part,-imaginary_part)}")
# # To clsssify a give  character as vowel,consonant,digit or special character we ca use nested if statment to check the character's category
# # without function 
# # here is the solution using a funciton 
# def classify_character(char): 
#     if char.isalpha():
#         if char.lower() in "aeiou":
#             return "Vowel"
#         else:
#             return "consonant"
#     else:
#         if char.isdigit():
#             return "Digit"
#         else:
#             return "Special character"
# # Test the fucniton
# char="A"
# result=classify_character(char)
# print(f"The character '{char}' is a {result}")
# # wihtout funciton 
# #here is the solution withotu using a function ,directly implementing the logic in the main part of the scrip
# char="A"
# if char.isalpha():
#     if char.lower() in "aeiou":
#         classification="Vowel"
#     else:
#         classification ="consonant"
# else:
#     if char.isdigit():
#         classification="Special character"
# print(f"The character "{char} "is a {classification}.")
#prin numbers from 1 to 10 
def print_numbers(n):
    i=1
    while i <=n:
        print(i)
        i=i+1
print_numbers(10)


def print_numbers(n):
    i=1
    while i<n:
        print(i)
        i=i+1
print(print_numbers(10))
# without using function
i=1
n=10
while i<=n:
    print(i)
    i=i+1
# for loop  h
#calculate the sum if natural numbers up to given number 
def sum_of_natural_numbers(n):
    total=0
    for i in range(0,n+1):
        total=total+i
    return total
# test the function
n=10 
print(f"The sum of natural numbers up to {n} is{sum_of_natural_numbers(n)}")

#withtout using function 
n=10 
totl=0 
for i in range(1,n+1):
    total =total+1
print(f"The sum of natural numbers up to {n} is {total}")

# reverse a given numbers

def reverse_number(num):
    reverse_number=0
    while num>0:
        remainder=num%10
        reverse_number=reverse_number*10+remainder
        num//=10
    return reverse_number

num=1234
print(f"The reverse of the number{num} is {reverse_number(num)}")
#without using the function 
num=12345
reversed_num=0
while num>0:
    remainder=num%10 
    reverse_number=reversed_num*10+remainder
    num//=10

num=1

