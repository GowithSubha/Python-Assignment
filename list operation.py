# Write a Python Program to Append, Delete and Display Elements of a List using Classes.
class list_class():
   def __init__(self):
      self.n=[]
   def add_val(self,a):
      return self.n.append(a)
   def remove_val(self,b):
      self.n.remove(b)
   def display_val(self):
      return (self.n)
my_instance = list_class()
choice_val = 1
while choice_val!=0:
   print("0. Exit")
   print("1. Add elements")
   print("2. Delete element")
   print("3. Display list")
   choice_val=int(input("Enter your choice: "))
   if choice_val==1:
      n=int(input("Enter element to add to the list... "))
      my_instance.add_val(n)
      print("List: ",my_instance.display_val())
   elif choice_val==2:
      n=int(input("Enter number to delete.."))
      my_instance.remove_val(n)
      print("List: ",my_instance.display_val())
   elif choice_val==3:
      print("List: ",my_instance.display_val())
   elif choice_val==0:
      print("Exit")
   else:
      print("Invalid choice!")
print()