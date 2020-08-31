# Library Management System
import pyttsx3
class Library:
    def __init__(self,list_of_books,Library_name):
        self.lend_bookdata = {}
        self.list_of_books = list_of_books
        self.library_name = Library_name
        # Adding books to dict
        for books in self.list_of_books:
            self.lend_bookdata[books] = None
    def Display_book(self):
        for key,items in enumerate(self.list_of_books):
            print(f"{key} {items}")
    def Lend_book(self,Book,author):
        if Book in self.list_of_books:
            if Book in self.lend_bookdata is None:
                self.lend_bookdata = author
            else:
                print(f"sorry this book is lend by {self.lend_bookdata[Book]}")
        else:
            print("you have written wrong book name \n")
    def Return_book(self,Book,author):
        if Book in self.list_of_books:
            if self.lend_bookdata[Book] is not None:
                self.lend_bookdata.pop(Book)
            else:
                print("Sorry but This book is not Lend")
        else:
            print("You have written wrong book name")
    def add_book(self,book_name):
        self.list_of_books.append(book_name)
        self.lend_bookdata = None
    def del_book(self,book_name):
        self.list_of_books.remove(book_name)
        self.lend_bookdata = None

def Main_func():
    books = ["The Fault in our Stars","Night at a Call Centre",
             "Power of a Subconsious Mind","Rich Dad Poor Dad"]
    Library_name = "Avii"
    Secret_key = 456678
    Avii = Library(books,Library_name)
    pyttsx3.speak("Welcome to Library")
    print(f"Welcome to {Avii.library_name} Library\n")
    print(f" enter '1' for Display \n '2' for Lend book \n '3' for Return book \n '4' for add book \n '5' for del book \n")
    inp = int(input())
    if inp == 1:
        Avii.Display_book()
        Main_func()
    elif inp == 2:
        name = input("Enter your name\n")
        inp1 = input("Enter book which you wanna lend\n")
        Avii.Lend_book(inp1, name)
        Main_func()
    elif inp == 3:
        name = input("Enter your name\n")
        inp1 = input("Enter book which you wanna return\n")
        Avii.Return_book(inp1, name)
        Main_func()
    elif inp == 4:
        book_name = input("Enter book name you wanna add\n")
        Avii.add_book(book_name)
        Main_func()
    elif inp == 5:
        inpp = int(input("Enter Secret key to delete the book\n"))
        if inpp == Secret_key:
            book_name = input("Enter book name you wanna delete\n")
            Avii.del_book(book_name)
            Main_func()
        else:
            pyttsx3.speak("Wrong Secret Key")
            pyttsx3.speak("Sorry we can't delete this book")
            print("Wrong Secret key... Sorry we can't delete this book\n")
            Main_func()
    else:
        pyttsx3.speak("Wrong Input")
        print("Wrong input...")
        Main_func()
if __name__ == '__main__':
    Main_func()