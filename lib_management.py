dictionary = {}
class Library:
    def __init__(self, name , books):
        self.name = name
        self.books = books

    def display_books(self):
        print("We have books given below: ")
        c_b = 0
        for item in self.books:
            print(item)
            c_b +=1
        return f"These are {c_b} books"
    def add_books(self,books):
        for books in books:
            self.books.append(books)

    def lend_books(self,lender,books):
        for book in books:
            if book not in self.books:
                print("Book Not Available")
            else:
                self.books.remove(book)
                if lender in dictionary.keys():
                    dictionary.get(lender).append(book)
                else:
                    dictionary.update({lender:[book]})

    def return_book(self,lender,books):
        for book in books:
            self.books.append(book)
            if  lender in dictionary.keys():
                dictionary.get(lender).remove(book)
    def lender_view(self,lender):
        print("The Books are given Below")
        for item in dictionary.get(lender):
            print(item+",",end="")

    def dict_view(self):
        for user in dictionary:
            print(user+"=> ")
            for books in dictionary.get(user):
                print(books,end=",")


viraj = Library("Viraj",["Hindi","ENglish"])
a=1
if __name__ == '__main__':
    while (a==1):
        print("\n\t*******WELCOME TO LIBRARY********\n")
        print("\tEnter Your Choice\n\t"
              "1 for View Library Books\n\t"
              "2 for Add Books\n\t" 
              "3 for Lend Books\n\t"
              "4 for Return Books\n\t"
              "5 for lender View\n\t"
              "6 for Dictionary View\n\t"
              "7 for Exit\n")
        user_choice = int(input())
        if user_choice == 1:
            print(viraj.display_books())

        elif user_choice == 2:
            print("Enter Books name wan to add seperated by Comma(,) : ",end="")
            books = input()
            list_books = books.split(",")
            viraj.add_books(list_books)
        elif user_choice == 3:
            print("Enter lender name : ",end="")
            lender_name = input()
            print("Enter Books name want to lend seperated by Comma(,) : ",end="")
            lender_books = input()
            list_lender = lender_books.split(",")
            viraj.lend_books(lender_name,list_lender)
        elif user_choice == 4:
            print("Enter lender name : ",end="")
            lender_name = input()
            print("Enter Books name want to return seperated by Comma(,) : ",end="")
            return_books = input()
            list_return = return_books.split(",")
            viraj.return_book(lender_name,list_return)
        elif user_choice == 5:
            print("Enter lender name for books: ", end="")
            lender = input()
            viraj.lender_view(lender)
        elif user_choice == 6:
            viraj.dict_view()
        elif user_choice == 7:
            print("Thank You For using library")
            a=0