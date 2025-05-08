class Dog:
    def __init__(self, name, breed):
        self.name = name        
        self.breed = breed      

    def bark(self):
        print(f"{self.name} which is a {self.breed} says: Woof woof!")


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Poodle")


dog1.bark()
dog2.bark()
