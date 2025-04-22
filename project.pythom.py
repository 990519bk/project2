from project2  import duck

b=duck()

print(b.name)
v = input("Would you want to add a book ?('Yes' ,'No')")                             
if v == "Yes":
   c = b.add()
