#filter function: 
#This function is used to filter out elments of iterable
numbers=[67,89,91,34,55,45,46,78]
def filter_even(val): 
    if val %2==0: 
        return True
filter_object=list(filter(filter_even,numbers))
print(filter_even)
