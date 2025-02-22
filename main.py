def greet(name, birth):
   print(f"Hello, My name is {name}.")
   print(f"I was created in {birth}.")

def remind_name():
   print('Please, remind me your name.')
   name = input()
   print('What a great name you have, ' + name + '!')

def guess_age():
   print('Let me guess your age.')
   print('Enter remainders of dividing your age by 3, 5 and 7.')
   reminder3 = int(input())
   reminder5 = int(input())
   reminder7 = int(input())
   age = (reminder3 * 70 + reminder5 * 21 + reminder7 * 15) % 105
   print(f"Your age is {age}; that's a good time to start programming!")

def count():
   print('Now I will prove to you that I can count to any number you want.')
   num = int(input())
   curr = 0
   while curr <= num:
      print(curr, '!')
      curr = curr + 1

def test():
   print("Let's test your programming knowledge.")
   print("""Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
   while True:
      answer = int(input())
      if answer == 2:
         print("Congratulations, have a nice day!")
         break
      else:
         print("Please, try again.")

greet("BuddyBot", 2000)
remind_name()
guess_age()
count()
test()