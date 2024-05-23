def sum_of_two_integers(a,b): 
    return a+b
# Example 
a=10 
b=20 
print(sum_of_two_integers(a,b))

#you have array of integers write a funtion to tuen the sum of all elemens 
def sum_of_array(arr): 
    return sum(arr)
arr=[1,2,3,4]
print(sum_of_array(arr))

# Give to floting -point numbers x and yy compute thei sum 
def sum_of_two_floates(x,y):
    return x+y 
#example 
x=3.14 
y=2.71 
print(sum_of_two_floates(x,y))

# wtite a prgram to add a two complex numbers 
def sum_of_two_complex_numbers(c1,c2): 
    return c1+c2
c1=complex(1,2)
c2=complex(3,4)
print(sum_of_two_complex_numbers(c1,c2))

# calucalte the sum two large intergers provided as string s 
def sum_of_large_intergers(s1,s2): 
    return str(int(s1)+int(s2))
#Example 
s1="12345"
s2="23455"
print(sum_of_large_intergers(s1,s2))

# using normal approch 
# a=int(input("Enter first interger:  "))
# b=int(input("Enter secind intergers: "))

# sum_ab=a+b
# print("sum:",sum_ab)

#you have an array of intergers write a funciton to return the sum of all the elemnts 

# arr = [int(x) for x in input("Enter integers separated by space: ").split()]

# sum_arr = 0
# for num in arr:
#     sum_arr += num

# print("Sum of array:", sum_arr)
# give two flaoting -point numbers "x" and "y" compute their sum 
x=float(input("enter first flaoting-point numbes: "))
y=float(input("Enter second floating-point numbers: "))
sum_xy=x+y
print("sum:",sum_xy)


# write a program to add two complex nuumbers 
real1=float(input("Enter real part of first complex: "))
image1=float(input("Enter imaginary part of first complex number:  "))
real2=float(input("Enter real part of second complex number:  "))
imag2=float(input("Enter imginary part of second complex number: "))
c1=complex(real1,image1)
c2=complex(real2,imag2)

sum_c=c1+c2
print("sum of complex numbers:",sum_c)

# calculate the sum of two large intergers provided as string 
s1=input("Enter first large inter: ")
s2=input("Enter second large intergers: ")

# Reverse both string to facilitate addition from least significant 
s1=s1[::-1]
s2=s2[::-1]

max_len=max(len(s1),len(s2))
carry=0 
result =[]
for i in range(max_len): 
    digit1=int(s1[i]) if i <len(s1) else 0 
    digit2=int(s2[i]) if i<len(s2) else 0 
    total =digit1 +digit2 +carry
    result.append(str(total % 10))
    carry =total//10 
if carry : 
    result.append(str(carry))
sum_of_large_intergers="".join(result[::-1])
print("sum of large intergers: ",sum_of_large_intergers)
# Give two intergers a and b find the diffrence  
def diffrence_of_intergers(a,b): 
    return a-b 
# example usage 
a=15 
b=10 
print("Diffrnece: ", diffrence_of_intergers(a,b))

# fiven an array of integers compute the diffrence between the largeset ans smal elemnts 
def difference_between_largest_and_smallest(arr): 
    largest=max(arr)
    smallest=min(arr)
    return largest -smallest
# example usage 
arr=[1,2,3,4,4]
print("Diffrence betwen largest and smallest:", difference_between_largest_and_smallest)

# substract two floating point numbers x and y 
def diffence_of_floats(x,y): 
    return x-y 
# Example usage 
x=5.75 
y=3.50 
print("Diifrece", diffrence_of_intergers(x,y))
# Write a fucniton to substaract two complex numbers 
def diffrence_of_complex_numbers(c1,c2): 
    return c1-c2 
# example usage 
c1=complex(2,4)
c2=complex(2,4)

print("Diffrnece of complex numbers:", diffrence_of_complex_numbers(c1,c2))
# Caluculate the diffrence between the lenghs of two given strings 
def diffrence_betweena_lenght(s1,s2): 
    lenght1=len(s1)
    lenght2=len(s2)
# Example usage 
s1="Hello"
s2="world!"
print("Diffrence between lenght: ", diffrence_betweena_lenght(s1,s2))
# Given two intergers "a" and b find the diffrrence betwen b 
a=int(input("Enter first integers: "))
b=int(input("Enter second intergers: "))

diffrence_ab=a-b
print("Diffrence:",diffrence_ab)


# Given an array of intergers ,complet the diffrence betwen the largest ans smalles telements 

arr=[int(x) for x in input("Enter integers separeted by space : ").split()]
largest=max(arr)
smallest=min(arr)
diffrence=largest-smallest
print("Diifrence between largest and smallest:",diffrence)

#substarct two floating point numbers x and y 
x=float(input("Enter first flaoting-point number: "))
y=float(input("Enter second flaoting-point number: "))


# give tow integers a an b find the product of a and b 
def product_of_two_integers(a,b): 
    return a* b 
a=10 
b=20 
print("product:", product_of_two_integers(a,b))

# write a function to computs the product of all elements in and integers array 
def product_of_array(arr): 
    product=1 
    for num in arr: 
        product *=num
    return product
# example usage 
arr=[1,2,3,4,4,5]

print("product of array:",product_of_array(arr))

# Multiply two floating-point numbers x and y 
def product_of_floats(x,y): 
    return x*y 
# example usage 
x=3.13
y= 3.34
print("product:",product_of_floats(x,y))

# Calculate the priduct
def matrix_product(A,B)
    # assuming A B are 2d Arry lists and have valid dimensios for matrix 
    rows_A=len(A)
    col_A=len(A[0])
    row_B=len(B)
    cols_B=len(B[0])

    # Intialization  result matrix with zero 
    result =[[0 for _ in range(col_B)] for _ in range(rows_A)]

    for i in range(row_A):
        for j in range(cols_B): 
            for k in range(cols_A): 
                result[i][j] +=A[i][k] *B[K][j]

    return result
#Example usage 
A=[[1,2],[3,4]]
b=[[5,6],[7,8]]

def polynomial_product(poly1, poly2):
    m = len(poly1)
    n = len(poly2)
    product = [0] * (m + n - 1)
    
    for i in range(m):
        for j in range(n):
            product[i + j] += poly1[i] * poly2[j]
    
    return product

# Example usage:
poly1 = [1, 2, 3]  # Represents 1 + 2x + 3x^2
poly2 = [4, 5]     # Represents 4 + 5x
result = polynomial_product(poly1, poly2)
print("Product of polynomials:", result)  # Output: [4, 13, 22, 15]

