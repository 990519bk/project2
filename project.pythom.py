from project2  import book

b=book()

while True:
  print(b.name)
  v = input("Would you want to add a book ?(yes/find/no):").strip().lower()
  if v == "yes":
    b.Add
  elif v == "find":
    title = input("book title:").strip().upper()
    info = b._book.get(title)       
    if info:
      print(f"\nFound'{title}':\n Author:{info['Author']}\n Price:{info['price']}")     
    else:
      print("Not found:",title) 
  elif v == "show":
    b.show
  elif v == "sell":
    b.sell 
  elif v =="no":
   print("bye.") 
   break
  else:
    print("type:yes/find/no")        
  









  