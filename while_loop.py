# while 1:
#     print(1)


# while a==1:
#     print(a)
#     a=a+1
#
# while not 1:
#     print("In while loop")
# print("End of while loop")
#
# a=1
# while a<10:
#   print(a)
#   a=a+1
# print(a)

# while True:
#     print('What is your name?')
#     name = input()
#     print('What is your age?')
#     age = input()
#     print('What is your favorite color?')
#     color = input()

# a=1
# while a>10:
#   print(a)
#   a=a+1
# else:
#   print(a)
#
# while a<10:print(a);a=a+1

# WAPPT print first 100 natural numbers
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# WAPPT print even numbers upto hundred
# i = 0
# while i <= 100:
#     print(i)
#     i += 2

# WAPPT print addition of first 100 natural numbers
# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i = i + 1
# print(sum)

# WAPPT print table of 5
# i = 1
# while i <= 10:
#     print("5\t*\t",i,"\t=\t",i*5)
#     i += 1

# WAPPT promote the user to input a series of intergers until the user enters zero using while loop.
# Calculate and print the sum of all +ve integers entered
#
# i = 1
# sum = 0
# while i != 0:
#     i = int(input("Enter a number: "))
#     if(i>0):
#         sum = sum + i
# print("Sum = ",sum)

# WAPPT generate a random number between 1 to 20 and asks the users to guess it.
# Use the while loop to give users multiple chances until they guess the correct number
# import random
# num = random.randrange(1,20)
# i=0
# attempts=1
# print("Guess the random number between 1 and 20")
# # print(num)
# while i != num:
#     i = int(input("Enter a number to guess: "))
#     while i != num: # print(num-i)
#         i = int(input("Nah! Enter again: "))
#         attempts = attempts + 1
#         if i == num:
#             print("you won in ",attempts,"tries")

# WAPPT check whether the given number is palindrome or not
# a = int(input("number nhak\n"))
# b = 0
# c = a
# while a > 0:
#     b = (b * 10) + a % 10
#     a = a // 10
# if c == b:
#     print("number is palindrome")
# else:
#     print("number is not palindrome")

# WAPPT check whether the given number is an armstrong number or not
# a = int(input("number nhak\n"))
# b = 0
# c = 0
# d = a
# while a > 0:
#     b = a % 10
#     c = c + b ** 3
#     a = a // 10
# if c == d:
#     print("number is armstrong number")
# else:
#     print("number is not armstrong number")

