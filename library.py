class Library:               # creating class

    def __init__(self, book_id, book_name, author):         #constructor runs 
        self.book_id = book_id                    # stores book_id inside the object
        self.book_name = book_name
        self.author = author

    def book_issue(self):                                #method to  book issue
        print("Book Issued:", self.book_name)

    def returning_book(self):
        print("Book Returned:", self.book_name)

    def book_details(self):
        print("Book ID:", self.book_id)
        print("Book Name:", self.book_name)
        print("Author:", self.author)


#  object   creation  for calling the init 
book1 = Library("101", "the final destination", "j.k rowling ")

book1.book_issue()
book1.returning_book()
book1.book_details()


        