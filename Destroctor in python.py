import time  
class Employee: 
    def __init__(self,nm,sal): 
        self.name=nm 
        self.salary=sal 

    def display(self): 
        print(f'name is {self.name}/n salary is :{self.salary}')
    def __del__(self): 
        print("Destroctor is called")
e1=Employee("shantanu",50000)
e1.display()
del e1 



