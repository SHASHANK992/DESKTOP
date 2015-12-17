class library:
    book_count=0

    def __init__(self, name, author, isbn, price):
        self.name = " "
        self.author = " "
        self.isbn = " "
        self.price = 0

    def bookcount(self):
        self.book_count +=1

    def enter_details(self):
        self.name = input("ENTER THE BOOK NAME:")
        self.author = input("ENTER THE BOOK AUTHOR:")
        self.isbn = input("ENTER THE BOOK ISBN:")
        self.price = input("ENTER THE BOOK PRICE:")

    def display(self):
        print("BOOKNAME:", self.name)
        print("AUTHOR:", self.author)
        print("ISBN:", self.isbn)
        print("MRP:", self.price)



f1 = library (" ", " ", " ", 0)
f1.enter_details()
f1.bookcount()
f1.display()

