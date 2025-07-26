# Data Abstraction
'''
Data Abstraction refers to providing only essential details to the ouside world
 and hiding the background details . To represent the needed information in 
 program without presenting the details
'''
# Data ENcapsulation
'''
This ia process of wrapping code and data together into a single unit
'''
# Data Absraction AND Data Encapsulation in Python

# Data Absraction

class library():
    def __init__(self,books):
        self.books=books
    def listbooks(self):                   
        for book in self.books:            
            print(book)
    def borrow_books(self,borrow_book):
        if borrow_book in self.books:
            print("Get Your Book Now")
            self.books.remove(borrow_book)
        else:
            print("Book is Not Available")
    def return_book(self,recieve_book):
        print("You have returned the Book")
        self.books.append(recieve_book)        
        
book=['Life of Abdul','Brain of YOU','c','c++','python''java']
o=library(book)
message="""
         1.Display
         2.Borrow
         3.Return
         """ 
while True:
    print(message)
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        print(o.listbooks())
    elif choice==2:
        book=input("Enter the the book to borrow from the library : ")
        o.borrow_books(book)
    elif choice==3:
        book=input("Enter the the book to return to the library : ")
        o.return_book(book)    
    else :
        print("Thank you come again")
        quit()
               
         
         
         
         
         
         
         
         
         
         
         
         