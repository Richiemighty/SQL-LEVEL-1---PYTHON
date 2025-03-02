# Library Management System
library = [
    {"Title": "Ghost", "Author": "Richard", "Year of Publication": 2019, "isbn": "BB22", "Available": True},
    {"Title": "Ghost", "Author": "Richard", "Year of Publication": 2019, "isbn": "BB23", "Available": False}
]


def add_book():
    print("Enter the following details of the Book: ")
    title = input("Enter the Book Title: ")
    author = input("Enter the Book Author: ")
    year_of_publication = int(input("What is the year of Publication: "))
    isbn = input("Enter the ISBN number: ")
    available = input("Is this book available (True/False): ").strip().lower() == "true"

    book_dict = {
        "Title": title,
        "Author": author,
        "Year of Publication": year_of_publication,
        "isbn": isbn,
        "Available": available
    }
    library.append(book_dict)
    print(f'Book "{title}" added successfully!')


def view_books():
    if not library:
        print("No books available in the library.")
    else:
        print("\nLibrary Books:")
        for book in library:
            status = "Available" if book["Available"] else "Borrowed"
            print(
                f'Title: {book["Title"]}, Author: {book["Author"]}, Year: {book["Year of Publication"]}, '
                f'ISBN: {book["isbn"]}, Status: {status}'
            )


def update_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            print("\nCurrent Book Details:", book)

            while True:
                print("\nWhat do you want to Update?")
                print("1. Title")
                print("2. Author")
                print("3. Year of Publication")
                print("4. Availability")
                print("5. Exit Update")

                choice = input("Select an option (1-5): ")

                if choice == "5":
                    print("Update Complete!")
                    break
                elif choice == "1":
                    book["Title"] = input("Enter the new Title: ") or book["Title"]
                elif choice == "2":
                    book["Author"] = input("Enter the new Author: ") or book["Author"]
                elif choice == "3":
                    book["Year of Publication"] = int(input("Enter the new Year of Publication: ") or book["Year of Publication"])
                elif choice == "4":
                    book["Available"] = input("Is the book available (True/False): ").strip().lower() == "true"
                else:
                    print("Invalid choice. Try again.")

                print("\nUpdated Book Details:", book)
            return

    print("Book not found. Confirm the ISBN.")


def delete_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            print("\nBook to be deleted:", book)
            confirm = input("Are you sure you want to delete this book? (Y/N): ").strip().upper()
            if confirm == "Y":
                library.remove(book)
                print("Book deleted successfully.")
            else:
                print("Deletion canceled.")
            return

    print("Book not found. Confirm the ISBN.")


def search_book(title):
    found_books = [book for book in library if book["Title"].lower() == title.lower()]
    if found_books:
        print("\nSearch Results:")
        for book in found_books:
            print(book)
    else:
        print("No book found with that title.")


def borrow_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            if book["Available"]:
                book["Available"] = False
                print(f'You borrowed "{book["Title"]}".')
            else:
                print(f'Book "{book["Title"]}" is already borrowed.')
            return

    print("Book not found.")


def return_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            book["Available"] = True
            print(f'You returned "{book["Title"]}".')
            return

    print("Book not found.")


def library_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book(input("Enter ISBN of the book to update: "))
        elif choice == "4":
            delete_book(input("Enter ISBN of the book to delete: "))
        elif choice == "5":
            search_book(input("Enter book title to search: "))
        elif choice == "6":
            borrow_book(input("Enter ISBN to borrow book: "))
        elif choice == "7":
            return_book(input("Enter ISBN to return book: "))
        elif choice == "8":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    library_menu()








