#Basic print Statmet
print("hello world")
# using a variable 
message ="hello world"
print(message)
#using function 
def greet():
    print("hello world")
greet()
# using a class 
class Greeter: 
    def say_hello(self): 
        print("hello, world!")
greeter=Greeter()
greeter.say_hello()
# using lambda function 
hello =lambda: print("hello,world!")
hello()

# problem Two Adding the two numbetrs 
#Basic addition 
a=5 
b=3 
print(a+b)

# using a function 
def add(x,y): 
    return a+b 
print(add(5,5))

# using user input
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print(a+b)


# using lambda function 
addtion =lambda a,b:a+b
print(addtion(5,6))

# using the class 
class calculator: 
    def add(self,x,y): 
        return x+y 
calc =calculator()
calc.add(5,4)

# problem 3 Substract two numbers 
# Basic mehtod 
a=4
b=5
print(a-b)

# using function 
def substraction(a,b): 
    return a-b
print(substraction(4,6))

# using lambda
sub=lambda a,b: a-b
print(sub(3,5))

# using class 
class substration(): 
    def substract(self,a,b): 
        return a-b
subtr=substration()
print(subtr.substract(4,6))

# multiply Two numbers 
#basic multiplication 
# basic method 
a=4
b=5
print(a+b)

#using useer input
a=int(input("Enter the first number "))
b=int(input("Enter second number"))
print(b+a)

#using function 

def mul(a,b):
    print(a*b)
    return a*b
print(mul(4,5))

# lambda
mul=lambda a,b:a*b

print(mul(4,5))

#using class 

class multiplication: 
    def mul(self,a,b):
        return a*b
multi=multiplication()
print(multi.mul(3,6))

# Find the remainder when one number is divided by another 
a=5 
b=3 
print(a%b)

# using a fucntion 
def remainder(x,y): 
    return x%y 
print(remainder(5,3))


# using user input
a=int(input("Enter first number"))
b=int(input("Enter the second number"))
print(a%b)

# using lambda 
remainder=lambda x,y:x%y 
print(remainder(5,3))


# using class
class Calculator: 
    def remainder(self,x,y):
        return x %y 
calc=Calculator()

print(calc.remainder(5,3))

#check if a number is positive ,negatibe or zzero 

# baisic if-else 
a=5 
if a>0: 
    print("positive")
elif a<0:
    print("negative")
else:
    print("Zero")

# using a fucntion 
def check_number(x):
    if x>0: 
        return "Positve"
    elif x<0: 
        return "Negative"
    else: 
        return "Zero"
    
# using user input
a=int(input("Enter a number:"))
if a>0: 
    print("possitive")
elif a<0:
    print("Negative")
else:
    print("Zero")

# using lambda 
check =lambda x:"positive" if x>0 else "negative" if x<0 else "Zero"
print(check(5))

# using a class 
class NumberChecker:
    def check(self, x):
        if x > 0:
            return "Positive"
        elif x < 0:
            return "Negative"
        else:
            return "Zero"

checker = NumberChecker()
print(checker.check(5))


# swap two numbers 
a=5 
b=3
temp =a 
a=b 
b=temp 
print(a,b)

# Without using a temporary varaible 
a=5 
b=3 
a,b=b,a
print(a,b)


#  using a temporary  varaible 
a=5 
b=3 
temp=a 
a=b 
b=temp
print(a,b)

# without using a temporarly varaible 
a=5 
b=3 
a,b=b,a 
print(a,b)

# using arithemetic oprations 
a=5 
b=3 
a=a+b 
b=a-b 
a=a-b 
print(a,b)

# using bitwise XOR 
a=5 
b=3 
a=a^b 
b=a^b 
a=a^b 

print(a,b)

# using a function 
def swap(x,y): 
    return y,x 
a=5 
b=3 
a,b=swap(a,b)
print(a,b)

# print the largest of three numbers 
# basic if-else 
a=5 
b=3 
c=8 
if a>b and a>c: 
    print(a)
elif b>a and b>c:
    print(b)
else: 
    print(c)


# using max funciton 
a=5 
b=3 
c=8 
print(max(a,b,c))

# using a fucntion 
def  largest(x,y,z):
    if x>y and x>z:
        return x 
    elif y>x and y>z:
        return y 
    else: 
        return z 
print(largest(5,3,8))

# using a list 
number =[5,3,8]
print(max(number))
# using sorted fucniton 
a=5 
b=3 
c=8 
largest =sorted([a,b,c],reverse=True)[0]
print(largest)

# print the smallest ot three numbers 
# basic if-else 
a=5 
b=3 
c=8 
if a>b and a<c: 
    print(a)
elif b<a and b<c: 
    print(b)
else: 
    print(c)

# using min fucntion 
a=5 
b=3 
c=8 
print(min(a,b,c))

# using a function 
def smallest(x,y,z): 
    if x<y and x<z: 
        return x 
    