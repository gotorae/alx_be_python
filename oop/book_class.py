# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: initializes the book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Readable string representation (for users)."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation (for developers)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: called when an instance is deleted."""
        print(f"Deleting {self.title}")
