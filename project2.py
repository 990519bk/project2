class book():
    def __init__(self, storage_path="books.txt"):
        self.storage_path = storage_path

        self._books = []
        self.name = ""
        self.title= ""
        self._book = {}
        self.price = 8
        self.author = "Jason"
 

    def Add(self):
       
        self.title=input("enter the name of the book you would like to add: \n")
        self.author=input("enter the author of the book you would like to added:\n")
        self.price=float(input("enter the listing price of the book:\n"))
       
        self._book[self.title]={'author':self.author,'price':self.price}
        print("You have added",self._book)

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
        for x   in self._book:
           print (x)
           print(self._book[x]('price'))
           print(self._book[x]("self_book"))
           print(self._book[x]("author"))


    def save(self):
     
        try:
            with open(self.storage_path, "w", encoding="utf-8") as f:
                for t, a, p in self._books:
                    f.write(f"{t}|{a}|{p}\n")
            print(f"Saved to {self.storage_path}")
        except Exception as e:
            print("Failed to save:", e)

   
       
   
    def find(self):
        self.title = input("What book do you want to find")
        if self.title in self._book:
            print("book found")
            print("author:",self._book[self.title]["author"])
            print("price:",self._book[self.title]["price"])
        else:
            print("Sorry the book is not in the collection.")

    