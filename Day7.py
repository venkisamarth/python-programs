# Determain if a numbers if divisible by 5 
number =15 
if number % 5==0: 
    print("Divisible by 5 ")
else: 
    print("Not Divisible by 5 ")

# check positive numver or negaitve number 
number=12
if number>0: 
    print("Number is positive ")
else: 
    print("Negative")    

# check single characte check 
char=input()
if char in "aeiouAEIOU":
    print("Vowel")
else: 
    print("This is not vowel")

# check odd or even number  
number=int(input())
if number %2==0: 
    print("odd")
# age check for Voting 
age=20 
if age >=18:
    print("The person is eligible for vote")
else: 
    print("NOt Eligible ")
# using if else statments 
number -int(input())
if number %2==0: 
    print("Evnen ")
else: 
    print("Odd")
# psitive ir Negative 
number=int(input())
if number>=0: 
    print("positive")
else: 
    print("Negative")

# check uppercase or lowercase 
char =input()
if char.isupper():
    print("uppercase")
else:
    print('lowercase')

# Number comparision 
a=int(input())
b=int(input())
if a>b: 
    print("First number is greater")
else: 
    print("Second is greater")
# check Multiple of 3 
number =int(input())
if number %3==0: 
    print("multiple of 3")
else: 
    print("Not a multiple of 3")
# Using if elif-else statmets 
# grade classification 
grade=int(input())
if grade>=90: 
    print("A")
elif grade>=80: 
    print("B")
elif grade >=70: 
    print("C")
elif grade>=60: 
    print("D")
else: 
    print("f")

# day of the Week
day =int(input())
if day ==1 : 
    print("Monday")
elif day==2:
    print("Monday")
elif day==3:
    print("Wdnesday")
elif day==3:
    print("thursday")
elif day==5: 
    print("Friday")
elif day==6: 
    print("Saturday")
elif day==6: 
    print("Saturday")
else: 
    print("Sunday")
# Temperature Description
temperature =int(input())
if temperature<10:
    print("Cold")
elif temperature<=20: 
    print("Cool")
elif temperature<=30: 
    print("warm")
else: 
    print("Hot")

# trafic light signal 
signal =input()
if signal=="R": 
    print("Stop")
elif signal=="Y": 
    print("Ready")
elif signal=="G": 
    print("Go")
else: 
    print("Invalid signal")
# Bmi classification  
bmi =float(input())
if bmi <18.5: 
    print("underweight")    
elif bmi<25: 
    print("Normal weight")
elif bmi<30: 
    print("overweight")
else: 
    print("obese")

# find the maximum if three numbers
a=int(input())
b=int(input())
c=int(input())
if a>b: 
    if a>c: 
        print(a)
    else: 
        print(c)
else: 
    if b>c: 
        print(b)
    else: 
        print(c)

# TRiangle type 
a=int(input())
b=int(input())
c=int(input())
if a>b: 
    if a==c: 
        print("Equilateral")

    else: 
        print("Isosceles")
else: 
    if a==c or b==c:
        print("Isosceles")
    else: 
        print("Scalen")
# NUmber Range classifiction 
number -int(input())
if number <=50:
    print('low')
else: 
    if number <=100: 
        print("Medium")
    else: 
        print("height")

# Employee Bonus Calcultion 
year=int(input())
salary =int(input())
if year>10: 
    print(salary**0.2)
else: 
    if year>5: 
        print(salary*0.1)
    else:
        print(0)
# nested if complex condition 
a=int(input())
b=int(input())
if a%2==0: 
    if b%2==0: 
        if a+b>20: 
            print("Condition met")
        else: 
            print("condition not met")
    else: 
        print("condition not met")
else: 
    print("conditon not met")

# using while loops 
N=int(input())
sum_natural=0 
i=1 
while i<= N: 
    sum_natural +=i
    i+=1 
print(sum_natural)

# reverse a Number 
number =int(input())
reversed_number=0 
while number >0: 
    remainder=number%10 
    reversed_number=reversed_number*10+remainder
    number =number//10 
print(reversed_number)

#sum of Digits 

number =int(input())
sum_digit=0: 
while number >0:
    sum_digit +=number %10 
    number =number %10 
    number =number //10 
print(sum_digit)

# Fibonacci seris 
number =int(input())
sum_digits=0 
while number >0 : 
    sum_digit +=number %10 
    number = number //10 
print(sum_digits)

# sum of digit 