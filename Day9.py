# usr a  for loop 
#without funciton 
for i in range(1,11):
    print(i)
# wwith funciton 
def print_numbers():
    for i in range(1,11):
        print(i)
print_numbers()

# print the square of the numebrs 1 to 10 
for i in range(1,11):
    print(i**2)
# with funciton 
def print_squares():
    for i in range(1,11):
        print(i**2)
print(print_squares)

# print first 10 multiples of 5
# withotu funciton 
for i in range(1,11):
    print(i*5)
# without function  
def print_multiples_of_five():
    for i in range(1,11):
        print(i*5)
print_multiples_of_five()

# print the elements of the list 
my_list=[1,2,3,4,5]
for item in my_list:
    print(item)
# with funciot 
my_list=[1,2,2,2,2,2]
def my_listitem():
    for item in my_list:
        print(item)

my_listitem()

#print character of the stirng 
my_string ="hello"
for char in my_string:
    print(char)

# with funnciton 
string="venkatesh j m "
def char_in_string():
    for char in string:
        print(char)

char_in_string()

# use nested loops
#print a 3x3 grid of print 
# without function
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

#withtout  function
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
#with function
def print_grid():
    for i in range(1,4):
        for j in range(1,4):
            print(i,j)
print_grid()

#print a right tringle pattern of"*"

#withtout funciton 
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# with function 
def print_traingle():
    for i in range(1,6):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
print_traingle()

#print multiplication table form 1 to 5 
def print_multiplication_table():
    for i in range(1,6):
        for j in range(1,11):
            print(f"{i}*{j}={i*j}")

print_multiplication_table()

#print pairs of elements form two lists
list1=[1,2,3,4,5]
list2=['a',"b","c"]
for item1 in list1:
    for item2 in list2:
        print(item1,item2)
# with function 
def print_pairs(list1,list2):
    for item1 in list1:
        for item2 in list2:
            print(item1,item2)
print_pairs([1,2,3,4,5],["a","b","c"])

# print a square pattern of "*"
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

#with function

def print_square():
    for i in range(1,6):
        for j in range(1,6):
            print("*",end=" ")
print_square()

#Use break statment 

#withtout function 

for i in range(0,11):
    if i==5:
        break
    print(i)
#with fucntion

def print_until_five():
    for i in range(1,11):
        if i ==5:
            break
        print(i)
print_until_five() 





# search or an element in a list and stop onece found 
my_list=[1,2,3,3,4,4,5]
search_element=3
for item in my_list:
    if item==search_element:
        print("Element found")
        break
def search_int_list(my_list,search_element):
    for item in my_list:
        if item ==search_element:
            print("Element found")
            break
search_int_list([1,2,3,4,5,6],3)

# print numbers until a specific condition is met 
#without function

for i in range(1,11):
    print(i)
    if i%7==0:
        break

# withotu  fucniton 
def print_until_condition():
    for i in range(1,11):
        print(i)
        if i%7==0:
            break 
print_until_condition()
# Exit a loop if a number is neagtive:
# withtout fucntion 
numbers =[1,2,3,5,6,6]
for num in numbers:
    if num<0:
        print("Negative number found ,exiting loop")
        break
    print(i)

# without function 
def check_negative(numbers):
    for num in numbers:
        if num<0:
            print("Negative numbers found, existing loop")
            break
        print(num)
check_negative([1,2,3,3,4,4,4,-1,4,5])

# stop processing when a certin character is found in a string 
# without function 
my_string ="hello world"
for char in my_string:
    if char ==" ":
        break 
    print(char)
# with function 
def process_until_space(my_string):
    for char in my_string:
        if char ==" ":
            break 
        print(char)
process_until_space("hello world")
# continue statment 
#print odd numbers from 1 to 10:
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

# withtout function 
for i in range(1,11):
    if i%2==0:
        continue
    print(i)
# witotu fucniton 
def print_odd_numbers():
    for i in range(1,11):
        if i % 2==0:
            continue
        print(i)
print_odd_numbers()
# print nubers form 1 to except mutiplices of 3 
#without function 
for i in range(1,11):
    if i%3==0:
        continue
    print(i)

# with function 
def skip_multiples_of_three():
    for i in range(1,11):
        if i%3==0:
            continue
        print(i)
skip_multiples_of_three()
# print character of sting  except  voweld 
#withtout fucntion 
my_string="hello"
for char in my_string:
    if char in "aeiou":
        continue
    print(char)

#with function 
my_string ="hello"
for char in my_string:
    if char in "aeiou":
        continue
    print(char)
# with fucniton 
def print_consonants(my_string):
    for char in my_string:
        if char in "aeoiu":
            continue
        print(char)
print_consonants("hello")
