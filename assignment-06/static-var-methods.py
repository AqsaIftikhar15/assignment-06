class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = MathUtils.add(num1, num2)
print("Sum:", result)
