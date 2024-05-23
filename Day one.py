print("venkatesh jayappa mariyappanaver")
print("this is the first day of the work and")
import builtins

# Get all attributes of the builtins module
builtin_functions = dir(builtins)

# Filter out functions that start and end with double underscores
builtin_functions = [func for func in builtin_functions if not func.startswith("__") and not func.endswith("__")]

# Print the list of built-in functions
print(builtin_functions)

['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
  'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 
 
'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

print("Hello, world")

my_list=[1,2,3,4,4,4]
print(my_list)
print(len(my_list))
# name=input("Enter the name:")
# print("Hello,"+name)

print(type(5))
#int return s in value of the number
print(int("5"))

print(str(1234))
my_list=list(range(1,4))
print(my_list)

my_tuple=tuple([1,2,3,4,5])
print(my_tuple)

# dict(): returns a dictionary object:

my_dict=dict([("a",1),("b",2)])
print(my_dict)


# set(): return a set object . 
my_set=set([1,2,3,4,4])
print(my_set)

print(max([3,6,1,9]))
print(min([2,3,4,5,2,24]))
print(sum([1,2,2,3,4,4,5]))
nums_tuple=tuple(range(5))
print(nums_tuple)

# dict(): returns a dictionary 

my_dict=dict(name="john",age=10)
print(my_dict)
minmum =min(5,10,3,8)
print(minmum)
total=sum([1,2,3,3,4,5])
print(tuple)

absolute_value=abs(-14)
print(absolute_value)
sorted_list=sorted([3,1,4,1,5])
print(sorted_list)
numbers=list(range(5))
print(numbers)
colors=['red',"green","blue"]
enum_colors=list(enumerate(colors))
print(enum_colors)


names = ['John', 'Alice', 'Bob']
ages = [30, 25, 35]
zipped_data = list(zip(names, ages))
print(zipped_data)

print("hello World!")

def hello_world(): 
    message='Hello,world!'
    print(message)

hello_world()


# calculate tge sum of two numbers: 
sum=lambda a,b:a+b
print(sum(5,3))

def calculater_sum(a,b): 
    return a+b 
result=calculater_sum(3,5)
print(result)

# Find the Largest Among the Three numbers: 
max_num=lambda a,b,c:max(a,b,c)
print(max_num(3,2,5))

def find_largest(a,b,c): 
    return max(a,b,c)
result=find_largest(3,2,5)
print(result)

# check if numbers is prime or not 

is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print(is_prime(11))

def is_prime(num): 
    if num<=1: 
        return False
    for i in range(2,int(num ** 0.5)+1): 
        if num %i ==0: 
            return False
        return True
print(is_prime)

# print Fibonacci Series up to n Terms 

def fibonacci(n): 
    fib=[0,1]
    [fib.append(fib[-1]+fib[-2]) for  _ in range(n-2)]
    return fib[:n]
print(fibonacci(10))

def fibonacci(n): 
    fib_sequance=[0,1]
    while len(fib_sequance)<n:
         next_fib=fib_sequance[-1]+fib_sequance[-2]
         fib_sequance.append(next_fib)
    return fib_sequance[:n]

print(fibonacci(10))


# convert celsius to Fahrenheit: 
celsius_to_farenheit=lambda c:c*9/5 +32
print(celsius_to_farenheit(25))
def celsius_to_fahrenheit(celsius): 
    return (celsius *9/5)+ 32 
print(celsius_to_farenheit(25))

# check  is a string is a palindrome 
is_palindrome=lambda s:s==s[::-1]
print(is_palindrome("radar"))

def is_palindrome(s): 
    return s==s[::-1]

print(is_palindrome("radar"))


# calculat the factorial of the numbers: 
import math  
factorial =lambda n:math.factorial(n)
print(factorial(5))

def factoral(n): 
    if n==0: 
        return 1 
    else: 
        return n*factorial(n-1)
print(factorial(5))

# find the Square Root of a numbers 
# import math  
# square_root =lambda n:math.sqrt(n): 
# print(square_root(25))

# def square_root(n): 
#     return n**0.5
# print(square_root)

# reversing the string 
def reverse_string(s): 
    return s[::-1]
s="hello"
print(reverse_string(s))










