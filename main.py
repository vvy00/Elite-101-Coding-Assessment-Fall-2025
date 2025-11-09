from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def view_available_books(books):
    print ("Available Books:")
    for book in library_books:
        if book["available"]:
            print(f"{book['id']}: {book['title']}: by {book['author']}")
# print the books that are available
# view_available_books(library_books)

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books(books, term):
    term = term.lower()
    results = []
    for book in books:
        if term in book["author"].lower() or term in book["genre"].lower():
            results.append(book)
    if results:
        print("Search Research:")
        for book in results:
            print(f"{book['id']}: {book['title']}: by {book['author']} ({book['genre']})")
    else:
        print("No books found")
# print the search results
# search_books(library_books, "fantasy")

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout_book(books, book_id):
    for book in books:
        if book['id'] == book_id:
            if book["available"]:
                book["available"] = False
                book["due_date"] = (datetime.now() + timedelta(weeks=2)).strftime("%Y-%m-%d")
                book["checkouts"] += 1
                print(f"You have checked out '{book["title"]}'. It is due on {book["due_date"]}.")
            else:
                print(f"Sorry, '{book["title"]}' is already checked out.")
            return
    print("Book ID not found.")
# print the checkout result
# checkout_book(library_books, "B1")

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                book["due_date"] = None
                print(f"'{book['title']}' has been returned.")
            else:
                print(f"'{book['title']}' was not checked out.")
            return
    print("Book ID not found") 

def list_overdue_books(books):
    today = datetime.now()
    overdue = [
        b for b in books
        if not b["available"] and b["due_date"] and datetime.strptime(b["due_date"], "%Y-%m-%d") < today
        ]
    if overdue:
        print("Overdue Books:")
        for book in overdue:
            print(f"{book['id']}: {book['title']} by {book['author']} (Due {book['due_date']})")
    else:
        print("No overdue books")

# return_book(library_books, "B2")
# list_overdue_books(library_books)

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!
# create a Book class
class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title 
        self.author = author 
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    def checkout(self):
        if self.available:
            self.available = False
            self.due_date = (datetime.now() + timedelta(weeks=2)).strftime("%Y-%m-%d")
            self.checkouts += 1
            print(f"Checked out '{self.title}', due {self.due_date}.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if not self.available:
            self.available = True
            self.due_date = None
            print(f"Returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not checked out.")

    def is_overdue(self):
        if self.due_date:
            return datetime.strptime(self.due_date, "%Y-%m-%d") < datetime.now()
        return False
    
# convert dictionary to objects    
book_objects = [Book(**b) for b in library_books]

# 
# level 1: View available books
def view_available_books(books):
    print("\nAvailable Books:")
    for book in books:
        if book.available:
            print(f"{book.id}: {book.title} by {book.author}")

# level 2: Search books
def search_books(books):
    term = input("Enter author or genre to search: ").lower()
    results = [b for b in books if term in b.author.lower() or term in b.genre.lower()]
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"{book.id}: {book.title} by {book.author} ({book.genre})")
    else:
        print("No books found.")

# level 4: Overdue books
def list_overdue_books(books):
    overdue = [b for b in books if b.is_overdue()]
    if overdue:
        print("\nOverdue Books:")
        for book in overdue:
            print(f"{book.id}: {book.title} by {book.author} (Due {book.due_date})")
    else:
        print("No overdue books.")

# level 5: Top 3 most book checkouts
def top_checked_out_books(books):
    top_books = sorted(books, key=lambda b: b.checkouts, reverse=True)[:3]
    print("\nTop 3 Most Checked-Out Books:")
    for book in top_books:
        print(f"{book.id}: {book.title} (Checkouts: {book.checkouts})")

# menu
def menu(books):
    while True:
        print("\nLibrary Menu:")
        print("1. View Available Books")       # calls level 1
        print("2. Search by Author or Genre")  # calls level 2
        print("3. Checkout a Book")            # calls level 3 (Book.checkout())
        print("4. Return a Book")              # calls level 4 (Book.return_book())
        print("5. View Overdue Books")         # calls level 4
        print("6. Top 3 Most Check-Out Books") # calls level 5
        print("0. Exit")

        choice = input("Enter you choices: ")

        if choice == "1":
            view_available_books(books)
        elif choice == "2":
            search_books(books)
        elif choice == "3":
            book_id = input("Enter book ID to checkout: ")
            for book in books:
                if book.id == book_id:
                    book.checkout()
                    break
            else:
                print("Book ID not found.")
        elif choice == "4":
            book_id = input("Enter book ID to return: ")
            for book in books:
                if book.id == book_id:
                    book.return_book()
                    break
            else:
                print("Book ID not found")
        elif choice == "5":
            list_overdue_books(books)
        elif choice == "6":
            top_checked_out_books(books)
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again.")

# run the menu                                                                                                                                              
if __name__ == "__main__":
    menu(book_objects)
    # You can use this space to test your functions
