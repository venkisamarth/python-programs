class student: 
    collage="cote"
    def __init__(self,nm,m): 
        self.name=nm
        self.marks=m
s=student("venki",89)
s1=student("raju",90)
print(s1.marks)
print(s1.name)
print(s.marks)

# class varaible 
# varaibles mode for enter class(all object)
# only one copy created and distributed to all the object 
# modification is class varaible impact on all the object in that class

class Employee: 
    company_name="wipro"
    def __init__(self,nm,sal): 
        self.name=nm
        self.salary=sal
e1=Employee("jay",30000)
e2=Employee("vijay",5000)
e3=Employee("raju",89)
print(e1.name)
print(e2.name) 
print(e1.company_name)
print(e2.company_name)

#How to modify the  
Employee.company_name="TCS"
print(Employee.company_name)
e2.company_name="TCS"
print(Employee.company_name)

# class method 
# class method works on class varaible first arguments is class referce 
# self object referce 
# class class referce 
# made using decorator @classmethod 





