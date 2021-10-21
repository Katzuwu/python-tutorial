# its_raining = True
# while its_raining:
#     print("It's raining!")
#     answer = input("Or is it? (y=yes, n=no) ")
#     if answer == 'y':
#         print("Oh well...")
#     elif answer == 'n':
#         its_raining = False     # end the while loop
#     else:
#         print("Enter y or n next time.")
# print("It's not raining anymore.")

# raining = False
# while not raining:
#     print("It's not raining.")
#     if input("Is it raining? (y/n) ") == 'y':
#         raining = True
# print("It's raining!")

# stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
# length_of_stuff = len(stuff)
# index = 0
# while index < length_of_stuff:
#     print(stuff[index])
#     index += 1

# for item in stuff:
#     print(item)

# for letter in "abcdefghijklmnop":
#     print(letter)

# for number in (1, 2, 3, 4, 5, 6):
#     print(number)

# Exercises
# things = [1, 2, 3, 4, 5]
# for thing in things:
#     print(thing)
#
# before = [[1, 2], [3, 4], [5, 6]]
# after = []
# for sublist in before:
#     after.extend(sublist)
# print(after)
#
# string_numbers = ['1', '2', '3']
# numbers = []
# for string in string_numbers:
#     numbers += [int(string)]
# result = 0
# for n in numbers:
#     result += n
# print("their sum is", result)

# numbers = ['1', '2', '3']
# actual_numbers = []
# for number in numbers:
#     actual_numbers.append(int(number))
# print(actual_numbers)

# row_count = int(input("Type the number of rows needed:"))
# for column_count in range(1, row_count+1):
#     for number in range(1, column_count+1):
#         print(number, end=" ")
#     print()

row_count = int(input("Type the number of rows needed:"))

for line_number in range(1, row_count+1):
    for number in range(line_number, row_count+1):
        print(number, end=' ')
    print()
