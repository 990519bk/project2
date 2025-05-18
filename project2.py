class book():
    def __init__(self):
       self.name = ""
       self.title= ""
       self._book = {}
       self.price = 8
       self.author = "Jason"

    def Add(self):
       
        self.title=input("enter the name of the book you would like to add: \n").upper
        self.author=input("enter the author of the book you would like to added:\n").upper
        self.price=float(input("enter the listing price of the book:\n"))
       
        self._book[self.name]={'author':self.author,'price':self.price}
        print("You have added",self.title)

    def sell(self):
        self.name=input("enter the name of the book you  want to sell")
        try:
            str(self.name)
            if self. name in self._book:
               self._book.pop(self.name)
               print("the reaining books are:",self._book)
        except:
            print("please enter the book title")


    def show(self):
        for title  in self._book:
           print("title:",title)
           print("author:",self._book[title]["author"])
           print("price:",self._book[title]["price"])
           print("-")
   
    def find(self):
        self.title = input("What book do you want to find")
        if self.title in self._book:
            print("book found")
            print("author:",self._book[self.title]["author"])
            print("price:",self._book[self.title]["price"])
        else:
            print("Sorry the book is not in the collection.")

    def save(self):
        with open("books.txt","w") as f:
            for title in self._book:
                f.write(f"{title}\n")
        print("Book already save")
                