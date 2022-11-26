# Write a Python Program to Check String is Palindrome using Stack.



class Stack_structure:
   def __init__(self):
      self.items = []

   def check_empty(self):
      return self.items == []

   def push_val(self, data):
      self.items.append(data)

   def pop_val(self):
      return self.items.pop()

my_instance = Stack_structure()
text_input = input('Enter the string... ')

for character in text_input:
   my_instance.push_val(character)

reversed_text = ''
while not my_instance.check_empty():
   reversed_text = reversed_text + my_instance.pop_val()

if text_input == reversed_text:
   print("The string is a palindrome")
else:
    print("The string isn't a palindrome")