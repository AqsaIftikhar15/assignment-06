class Car:
    brand = "Toyota"
    
    def start(self):
        print(f"The {self.brand} car has started.")

my_car = Car()
print(my_car.brand)  
my_car.start()  
