class Employee:
    
    def __init__(self, name, salary,hours):
        self.name = name
        self.salary = salary
        self.hours=hours
        
    def display(self):
        print(f"Name: ", self.name, ", Salary: ", self.salary,"he works  {self.hours} per week")

# Create an object of the class
emp = Employee("John", 1000,8)
emp.display()

