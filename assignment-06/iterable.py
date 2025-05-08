class Countdown:
    def __init__(self, start):
        self.start = start + 1  
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.start -= 1
        if self.start < 0:
            raise StopIteration
        return self.start

# Example usage
print("Countdown from 5:")
for num in Countdown(5):
    print(num)

print("\n Countdown from 3:")
for num in Countdown(3):
    print(num)