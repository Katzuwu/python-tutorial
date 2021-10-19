
# BASICS
# a = 1
# a = a + 1
# b = a
# print(a)
#
# print("hello" * 3)
#
# print(a == 2)
#
# empty = None
# print(empty)
#
# # None()
#
# print(not a)
#
# print(1 == 1 and 2 == 2)

# FUNCTIONS
# user_number = input("Enter a number: ")
# print(user_number)

# print("Hello", "World")

# IF ELSE AND ELIF

# its_raining = True
# if its_raining:
#     print("It's raining!")

# its_raining = False
# if its_raining:
#     print("It's raining!")

# if its_raining:
#     print("It's raining!")
# else:
#     print("It's not raining.")
#
# print("Hello!")
# password = input("Enter the correct password: ")
#
# if password == "password":
#     print("Welcome, Sir.")
# else:
#     print("Wrong password.")
#
# print("Hello!")
# word = input("Enter something: ")
#
# if word == "hi":
#     print("Hi to you too!")
# elif word == "hello":
#     print("Hello hello!")

# Exercise
# print("Hello!")
# something = input('Enter something: ')
# print('You entered:', something)
#
# print('Hello!')
# something = input("Enter something: ")
# if something == 'hello':
#     print("Hello for you too!")
#
# elif something == 'hi':
#     print('Hi there!')
# else:
#     print("I don't know what,", something, "means.")

# user_input = input("Enter a word and I'll repeat it 1000 times: ")
# user_input += " "
# print(user_input * 1000)
#
# two_words = input("Enter two words: ")
# two_words += " "
# print(two_words * 1000)

password_checker = input("Please enter the correct password: ")
if password_checker == "Password":
    print("Welcome!")
elif password_checker == "":
    print("You didn't enter anything")
else:
    print("Access denied")
