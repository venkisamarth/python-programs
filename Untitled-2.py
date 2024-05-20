def reverse_string(s):
     return s[::-1]
s="venkki"
print(reverse_string(s))

# usingl loops

def reverse_string(s): 
    reversed_s=""
    for char in s: 
         reversed_s=char+reversed_s
    return reversed_s

s="hello"
print(reverse_string(s))  

#check if a string is a palindrome 
def is_palindrome(s): 
     return s == s[::-1] 
s="radar"
print(is_palindrome(s))

# using a loop 
def is_palindome(s): 
     for i in range(len(s)//2): 
          if s[i] != s[-(i+1)]: 
               return  False 
          return True
     
    #  count Vowels in a strin 
     def count_vowels(s): 
          return sum(1 for char in s.lower() if chr in "aeiou")
     
     s="hello"
     print(count_vowels(s))



def count_vowels(s): 
     count=0 
     vowels ="aeiou"
     for char in s.lower(): 
          if char in vowels: 
               count =count +1 
     return count
# s
s="hello"
print(count_vowels(s))
# counting consonats in a string 
def count_consonants(s): 
      return sum(1 for char in s.lower() if char.isalpha() and char not in "aeiou")

# example usage 
s="hello"
print(count_consonants(s))

def count_consonats(s): 
     count=0 
     vowels="aeiou"
     for char in s.lower(s): 
          if char.isalpha() and char not in vowels: 
               count +=1 
          return count 
# exmaple usage 
s="hello" 
print(count_consonants(s))


# convert a string to uppercase 

def to_uppercase(s): 
     return s.upper()
s="hello"
print(to_uppercase(s))

def to_uppercase(s): 
     result=""
     for char in s: 
          if "a" <=char<="z": 
               result +=chr(ord(char)-32)
          else: 
               result +=char
     return result

# example usage 
s="hello"
print(to_uppercase(s))


#convert a strinng to lowercase 
def to_lowercase(s): 
     return s.lower()
s="hello"
print(to_lowercase(s))



def count_consonants(s): 
     count=0 
     vowels="aeiou"
     for char in s.lower():
          if char.isalpha() and char not in vowels: 
               count +=1 
     return count 

s="hello"
print(count_consonants(s))


# convert a string to uppercase 
def to_uppercase(s): 
     return s.upper()
#Example usage 
s="hello"
print(to_uppercase(s))

def  to_uppercase(s): 
     result =""
     for char in s: 
          if 'a' <=char <="z": 
               result +=char(ord(char)-32)

          else: 
               result +=char
     return result 

# Example usage
s="hello"
print(to_uppercase(s))


#convert a string to lowercase 

def to_lowercase(s):
     return s.lower()
# example usage 
s="Hello"
print(to_lowercase(s))

# # using a loop 
# def to_lowercase(s): 
#      result =""
#      for char in s: 
#           if "A" <= char <="Z": 
#                result +=char(ord(char) +32)
#           else: 
#                result +=char
#      return result 

# # Example  usage 
# s="Hello"
# s="Hello"
# print(to_lowercase(s))

#captalize the first character of each word in a string 
def capaitalize_word(s):
     return s.title()
s="hello"
print(capaitalize_word(s))


# using loop 
def capitalize_words(s):
     word=s.split()
     capitalize_words=[word[0].upper() +word[1:].lower()]
     return  "  ".join(capitalize_words)
s="hello"
print(capitalize_words(s))

#finding the lienght of the stirng 
def string_lenght(s): 
     return len(s)
s="hello world"
print(string_lenght(s))

# solution using loop 
def string_lenght(s): 
     count = 0 
     for cahr in s: 
          count  +=1
     return count
# example usage 
s="hello"
print(string_lenght) 

# Replaceing the substring in a string 
def replace_substring(s,old,new): 
     return s.replace(old,new)
s="hello world"
print(replace_substring(s,"world","there"))


import re  
def replace_substring(s,old,new): 
     return re.sub(re.escape(old),new,s)
s="hello world"
print(replace_substring(s,"world","there"))

#remove whitespace from a string 

def remove_whitespace(s): 
     return s.replace(" "," ")
s="hello world"
print(remove_whitespace(s))

# #using join and split methods 

# def remove_witespace(s):
#      return "".join(s.split())
# s="hello world"
# print(remove_whitespace(s))



     

