class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name    
        self._salary = salary  
        self.__ssn = ssn          
emp = Employee("Alice", 50000, "123-45-6789")

print("Public (name):", emp.name)

print("Protected (_salary):", emp._salary)

try:
    print("Private (__ssn):", emp.__ssn)
except AttributeError:
    print("Cannot access private variable '__ssn' directly!")

print("Private (__ssn) using name mangling:", emp._Employee__ssn)
