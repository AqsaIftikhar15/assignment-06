class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person name is {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) 
        self.subject = subject
        print(f"Teacher's subject is {self.subject}")

teacher1 = Teacher("John", "Math")
