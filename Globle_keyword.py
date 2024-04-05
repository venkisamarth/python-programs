num=10 
print(num)
num=num+5 
print(num)

num=10 
def display(): 
    global num
    num=num+5 
    num=20 
    print("Inside ",num)
display()
print("outer",num)
# to Resolve this then we can refer the global keyword 
# How resolve unboundlocalError 
# x=10
# def display():
#     global num 
#     num=num+5 
#     print("Inside ",num)
# display()
# # print('outside',num)

# num =10
# def display():
#     global num 
#     num=num+5 
#     print("inside", num )

# display()
# print("outside",num)

