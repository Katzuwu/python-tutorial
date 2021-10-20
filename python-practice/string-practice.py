# my_string = "Hello World hello"
#
# print(my_string[-7:-2])
#
# print(my_string[-1])
#
# print(my_string.upper(), my_string.capitalize(), my_string.lower(), my_string.replace("o", "0", 2))
#
# print(my_string.rindex('o'))
#
# print(my_string.upper()[3:].startswith('L'))

# name = 'Cookie'
# print("Hello {}.".format(name))
# print("Hello %s." % name)
# print(f"Hello {name}.")

# print("C" in name)
# print("Hello" in name)
# print(len(name))

# print(str(42))
# print(float("42.44"))
# print(int("42"))

# Exercise

# print("Hello!")
# word1 = input("Enter something: ")
# word2 = input("Enter another thing: ")
# word3 = input("Enter a third thing: ")
# word4 = input("And yet another thing: ")
# # Usable everywhere
# print("You entered %s, %s, %s, %s." % (word1, word2, word3, word4))
# print("You entered {}, {}, {}, {}.".format(word1, word2, word3, word4))
# # Only usable in Python 3.6
# print(f"You entered {word1}, {word2}, {word3}, {word4}.")

message = input("What do you want me to say? ")
message = message.upper()
print(message, "!!!")
print(message, "!!!")
print(message, "!!!")

if message[::-1] == message:
    print("It's a palindrome!")
else:
    print("It's not a palindrome")
