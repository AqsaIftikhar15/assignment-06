class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.book_count()

    @classmethod
    def book_count(cls):
        cls.total_books += 1

for i in range(3):
    title = input(f"Enter title for book {i + 1}: ")
    new_book = Book(title)

print("Total books added:", Book.total_books)
