data=[]
for num in range(1,10):
    if num%2==0:
        data.append("even")
print(data)

print(["even" for num in range(1,10) if num %2 ==0])


data=[]
for num in range(1,10):
    if num%2 ==0:
        data.append("even")
    else:
        data.append('odd')
print(data)
print("*"*5)
print(["even" if num%2==0 else 'odd' for num in range (1,10)])



result=[]
marks=[89,91,56,34,70,81,12]
for m in marks:
    if m>=80 and m<=100:
        result.append("A")
    elif m>=60 and m<80:
        result.append("B")
    elif m>=35 and m<60:
        result.append("append")
    elif m>=35 and m<60:
        result.append("c")
else:
    result.append("faild or invalid marks")

print(result)


