books = ["Harry Potter","The Secret Garden","The wind on haunted Halls","The Jungle Book"]

print("1. Add new book")
print("2. Remove books")
print("3. Search books")
print("4. Show all books")

choice = input("enter your choice [1 - 4] :")


if choice == "1":
    book = input("Enter book name: ")
    books.append(book)
    print("Book added successfully : ",books)
    

elif choice == "2":
    book = input("Enter book name to remove: ")
    if book in books:
        books.remove(book)
        print("Book removed successfully :",books)
       
    else:
        print("Book not found:",books)

elif choice == "3":
    book = input("Enter name of book to search: ")
    if book in books:
        print("Book is available:",books)
    else:
        print("Book not available:",books)

elif choice == "4":
    if len(books) == 0:
        print("No books in library:")

    else:
        print("Books in library:")
        for b in books:
            print("-", b)

else:
    print("Invalid choice.")