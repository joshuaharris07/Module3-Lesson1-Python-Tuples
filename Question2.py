# Python Data Structure Challenges in Real-World Scenarios
# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

def add_book(book, author):
    book_to_add = (book, author)
    if book_to_add in library:
        print(f"{book} by {author} is already in the library.")  
    else:
        print(f"Added {book} by {author} to the library.")
        library.append(book_to_add)

library = [
    ("1984", "George Orwell"), 
    ("Brave New World", "Aldous Huxley")
    ]

book = input("What is the book title? ").title()
author = input("What is the author's name? ").title()

add_book(book, author)

print("Here are the books in the library:")
for book in library:
    print(f"{book[0]} by {book[1]}")