numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is {}".format(numbers[0]))

print("The last number is {}".format(numbers[-1]))

print("The smallest number is {}".format(min(numbers)))

print("The largest number is {}".format(max(numbers)))

print("The average of the numbers is {}".format(sum(numbers) / 5))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup',
             'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Please enter your username: ")
while user_input not in usernames:
    print("Access denied")
    user_input = input("Please enter your username: ")
print("Access granted")
