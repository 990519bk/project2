class book():
    def __init__(self):
       self.name =""
       self.title=""
       self._book={"duck"}
       self.price=8
       self.author="jason"

    def Add(self):
        self.title = input("What book do you want to see")
        print("You have added",self.title)
    
        self.title=input("enter the name of the book you would like to add: \n").upper
        self.author=input("enter the author of the book you would like to added:\n").upper
        self.price=float(input("enter the listing price of the book:\n"))
       
        self.book[self._name]={'author':self._author,'price':self._price}
    

    def sell(self):
        self.name=input("enter the name of the book you  want to sell")
        try:
            str(self.name)
            if self. name in self.book:
               self.book.pop(self.name)
               print("the reaining books are:",self.book)
        except:
            print("please enter the book title")


    def show(self):
        for x in self.book:
           print[x]
           print(self. book )[x]("self book" )
           print(self. book )[x]
           print(self. book )[x]["authuor price"] 
   
    def find(self):
        self.title = input("What book do you want to find")
   elif