names = ['Bob', 'John', 'Steve', 'Dave']
# print(len(names))
# names += ['Robert']
# print(names)
# print(names[:3])
# print('Bob' in names)
# names.remove('Bob')
# names.remove('John')
# print(names)
# names.append('Don')
# print(names)
# names.extend(['Bob', 'John'])
# print(names)
# print(names)
# names[1] = 'Don'
# print(names)

# numbers = [1, 2, 3, 4, 5]
# numbers_squared = [number ** 2 for number in numbers]
# print(numbers_squared)

# numbers_two = numbers.copy()
# numbers_two.append(6)
# print(numbers, numbers_two)

# Exercise
namelist = ['wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
namelist.append('pb122')
if 'pb122' in namelist:
    print("Now I know pb122!")

# print("Hello!")
# name = input("Enter your name: ")
# print("Your name is %s." % name)

namelist = ['wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
namelist.extend('theelous3')
if input("Enter your name: ") in namelist:
    print("I know you!")
else:
    print("I don't know you.")
