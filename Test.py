class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

# Create an object of the class
emp = Employee("John", 1000)
emp.display()

