# # computer the quatient of two integers 
# def divide_integers(a,b): 
#     return a//b 
# a=10 
# b=3 
# result =divide_integers(a,b)
# print(result)



# # without using a fucntion 
# a=10 
# b=3 
# result =a//b 
# print(result)

# # Divide all elements in an array by a given number 
# def divide_array(arr,divisor): 
#     return [x /divisor for x in arr]
# arr=[10,20,30]
# divisor =2 
# result =divide_array(arr,divisor)
# print(result)

# # without  using a funciton 
# arr=[10,20,30]
# divisor=2 
# result=[x /divisor for x in arr]
# print(result)

# # divide two flaoting point  numbers 
# def divide_floats(x,y): 
#     return x/y
# # Example usage
# x=10.5 
# y=2.5
# result =x/y
# print(result)
# # computer the qutient of two complex numbers 
# # using funciton 
# def divide_complex(c1,c2): 
#     return c1/c2 
# c1=complex(1,2)
# c2=complex(3,4)
# result =divide_complex(c1,c2)
# print(result)
# # without using a funciton 
# c1=complex(1,2)
# c2=complex(3,4)
# result=c1/c2
# print(result)
# # Divide a large integers lareg integers(provided as a string ) by another large 
# # interger(also a string)
# def divide_large_intergers(a_str,b_str): 
#     a=int(a_str)
#     b=int(b_str)
#     return str(a//b)
# # EXample usage 
# a_str="123456"
# b_str="987234"
# result =divide_large_intergers(a_str,b_str)
# print(result)
# # without using a funciton 
# # a_str="123455745765675"
# # b_str="232543645"
# # a=int(a_str)
# # b=int(b_str)
# # result=str(a//b)
# # print(result)

# # # compute a% b 
# # #This can be done directly using the modules operator % in pyhton 
# # a=10 
# # b=3 
# # remainder=a%b 
# # print(remainder)

# # fucniton to find the remainder of each elements in an array divided by a given numbers 
# def remainders(arr,divisor): 
#     return [x % divisor for x in arr]
# array=[10,20,30,40,50]
# divisor=6
# result =remainders(array,divisor)
# print(result)

# # Determain wheter a given intergers is even or idd using modules operator 
# def is_even_or_odd(num): 
#     if num % 2 ==0: 
#         return " Even"
#     else: 
#         return "Odd"
# # example usage
# number=7 
# result=is_even_or_odd(number)
# print(result)

# # find  the remainder of the division of two intergers provided as strings 
# def large_modulus(str_num1,str_num2): 
#     num1=int(str_num1)
#     num2=int(str_num2)
#     return num1%num2
# large_num1="123455"
# large_num2="123455"
# remainder=large_modulus(large_num1,large_num2)
# print(remainder)

# compute the sum of digits of an intergers until the sum 
# become a single digit using the moduls operator 
# # using funciton 
# def sum_of_digit_until_single_digit(n): 
#     while n>=10 : 
#         n=sum(int(digit) for digit in str(n))
# #         return n
# # Example usage 
# number =1234
# result-sum_of_digit_until_single_digit(number)
# print(result)

# # withotu funciton 
# n=1234
# while n>=10: 
#     n=sum(int(digit) for digit in str(n))
# print(n)

# # Compute a^b (a raised to the power of b)
# #using the exponentiation operator ** in python 
# a=2 
# b=3 
# result=a**b 
# print(result)

# # Funciton to raise each elements in an array to a given 
# def raise_to_power(arr,power): 
#     return [x ** power for c in arr]
# arr=[1,2,34,5,5]
# power=3 
# result=raise_to_power(array,power)
# print(result)

# withotu using a function 
array=[1,2,3,4,5]
power=3 
result=[x** power for x in array]
print(result)
# computer the power of a floating-point numbers x raise 
x=2.4 
y=3.5 
result=x**y 
print(result)

# using a fucniton 
def power_of_float(x,y): 
    return x**y 
# Example usage 
result=power_of_float(2.4,3.2)
print(result)

# calculate the power of a matrix raised to a given intergers ex[ponet 
import  numpy as np 
matrix =np.array([[1,2],[3,4]])
exponent=3 
result =np.linalg.matrix_power(matrix,exponent)
print(result)

# using a funciton 
def matrix_power(matrix,exponent): 
    return np.linalg.matrix_power(matrix,exponent)
#Example usage 
matrix =np.array([[1,2],[3,4]])
exponent =3 
result =matrix_power(matrix,exponent)
print(result)
# Find the value of a polynomial at a given point using th 

def polynomial_value(coefficients, x):
    return sum(coef * (x ** i) for i, coef in enumerate(coefficients))

# Example usage:
coefficients = [1, 0, 3]  # Represents 1 + 0x + 3x^2
x = 2
result = polynomial_value(coefficients, x)
print(result)  # Output will be 13 (3*2^2 + 0*2 + 1)

coefficients = [1, 0, 3]  # Represents 1 + 0x + 3x^2
x = 2
result = sum(coef * (x ** i) for i, coef in enumerate(coefficients))
print(result)  # Output will be 13 (3*2^2 + 0*2 + 1)
# computer a // b interger division 
#suing the floor division operator // in python 
a=10 
b=3 
result =a//b 
print(result)

# Fucniotn to floor divide each elelemts in an array bu a numbers 
def floor_divide_array(arr,divisor): 
    return [x // divisor for x in arr]
array=[10,20,30,40,50]
divisor=6 
result=floor_divide_array(array,divisor)
print(result)

# without using a fucniton 
array=[10,20,30,40,50]
divisor=6 
result=[x // divisor for x in array]
print(result)

# compute the floor divison of two floating point num a and y 
# using the floor division operator // 
x=7.5 
y=2.3 
result =x//y 
print(result)

#using a  function 

def floor_divide_floats(x,y): 
    return x//y

result=floor_divide_floats(7.5,2.3)
print(result)

# impliment a functin that simulates integers division using the divisiopn opeator 
def interger_division(dividend ,divisor): 
    quotient=0 
    while dividend >=divisor:
        quotient+=1 
    return quotient 
result =interger_division(10,3)
print(result)

# without using funciton 
dividend=10 
divisor=3 
quotient=0 
while dividend>=divisor: 
    dividend -=divisor
    quotient +=1 
print(quotient)