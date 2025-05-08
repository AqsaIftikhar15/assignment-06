class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee Name: {self.name}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  

    def show_department_info(self):
        print(f"Department: {self.dept_name}")
        print(self.employee.get_details())  
        
emp1 = Employee("Aqsa") 
dept1 = Department("HR", emp1) 

dept1.show_department_info()

