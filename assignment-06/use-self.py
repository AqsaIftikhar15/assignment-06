class Info:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
s1 = Info("John", 85)
s2 = Info("Jane", 90)

s1.display()
s2.display()