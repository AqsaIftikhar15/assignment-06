class counter:
    count = 0

    def __init__(self):
        counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

c1 = counter()
c2 = counter()
c3 = counter()
counter.display_count() 