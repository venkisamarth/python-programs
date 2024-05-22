print("hello")
message ="Hello world"
print(message)

def hello_world(): 
    print("Hello world")

hello_world()

#using lambda function 

hello_world=lambda: print("hello,world")
hello_world()
 
# with f string 
print(f"{"hello,world!"}")

# print variable 
varaible=42 
print(varaible)

# using fucniton 
def print_varaible(varaible): 
    print(varaible)

print_varaible(42)

# using F-string

variable =42 
print("varaible value:{}".format(variable))


# 3 usign with concatination 
varaible =45 
print("Variable value:"+str(varaible))

# printing the sum of two numbers 
a,b=5,7 
print(a+b)


# using a function 

def sum_to_numbers(a,b):
    return a+b 
print(sum_to_numbers(5,7))

# using lambda funciton 
sum_two_numbers=lambda a,b:a+b
print(sum_two_numbers(2,4))

# using intput 
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a+b)
# using f string 
a,b=23,23
print(f"The sum of {a} and {b} is {a+b}")


# diffrence of two string 
# using a funciton 

def diffrence(a,b): 
    return a-b 
print(diffrence(10,4))

# using lambda funciton 
diffrence=lambda a,b:a,b
print(diffrence(10,4))

# mehtod using input 
a=int(input("Enter the two numbers:  "))
b=int(input("Enter second numbers: "))
print(a-b)


# using f string 
a,b=10,4
print(f"The diffrence betwee {a} and {b} is {a-b}")

# print the product of two Numbers 
a,b=6,7
print(a*b)

# using funciton 
def product(a,b):
    return a * b
print(product(5,5))

# using lambda Fucntion 
product=lambda a,b:a*b
print(product(6,7))

# using input 
a=int(input("Enter first numbers: "))
b=int(input("Enter second number:  "))
print(a*b)

# using f string 
a,b=223,23
print(f"The product of {a} and {b} is {a*b}")

#3 print the Division of two numbers 
# direct method 
a,b=23,2
print(a/b)

# using a funciton 
def division(a,b): 
    return a/b
print(division(12,34))


# usingg lambda funciton 
a=int(input("Enter first number:  "))

b=int(input("Enter teh second number: "))

print(a/b)


# using F-stirng 
a,b=23,23
print(f"The division of {a} by {b} is{a/b}")

# print the REmainder of a  divsion 
# direct method 

a,b=17,5 
print(a%b)
# using a fucnito 
def remainder(a,b): 
    return a%b 
print(remainder(17,5))

# using lambda funciton 
remainder =lambda a,b:a%b 
print(remainder(17,5))

# using f-string 
a,b=17,5 
print(f"The remainder of {a} divided by {b} is {a%b}")


# swap of two numbers 
## using a temporary variable 
a,b=3,4
tem=a
a=b 
b=tem
print(a,b)
# using tuple unpaking 
a,b=4,9
a,b=b,a
print(a,b)

# using arthimethic Operations 
a,b=3,8 
a=a+b 
b=a-b
a=a-b 
print(a,b)

# using XOR method 
a,b=3,8 
a=a^b 
b=a^b 
a=a^b 
print(a,b)


# using a Funciton 
def swap(a,b): 
    return b,a
a,b=swap(3,8)
print(a,b)


#swap Teo VAriable without using a Third VAraible 
# using Tuple Unpking 

a,b=5,9
a,b=b,a
print(a,b)

# using Arithemetic  operation 
a,b=5,8 
a=a+b
b=a-b
a=a-b 
print(a,b)
# find the gratest of two numbers  
# using if-Else statments 
a,b,c=10,23,24
if a>b and a>c: 
    gretest=a 
elif b>c: 
    greatest=b 
    
else: 
    greatest=c 
    print(greatest)

# using max funciton 
a,b,c=10,15,8 
greatest =a if (a>b and a>c) else (b if b>c else c)
print(greatest )


# using a funciton 
def find_greatest(a,b,c): 
    if a>b and a>c : 
        return a 
    elif b>c : 
        return b 
    else: 
        return  c 
    
print(find_greatest(10,15,8))


# using lambda fucniton 
find_greatest=lambda a,b,c:a if (a>b and a>c) else (b if b>c else c)
print(find_greatest(10, 15, 8))

# check if if the numbers is even or odd 

num=4 
if num%2 ==0: 
    print("Even")
else: 
    print("Odd")

# using Ternary Operator 
def is_even_or_odd(num):
    return "Even" if num % 2 ==0 else "Odd"
print(is_even_or_odd(4))


# using input 
num =int(input("Enter  a numer:  "))
if num % 2 == 0: 
    print("even")
else: 
    print("odd")

#print("Hello [name ] using user input")
using input and print 

name =input("enter your name: ")
print(f"Hello,{name}!")

