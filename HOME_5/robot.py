import math
x = 0
y = 0
command = [0, 0]
while True:
    command = input("\nВвод команды ").split()
    if command == (" ").split():
        break
y = y + command[1]
y = y - command[1]
x = x + command[1]
x = x - command[1]

range = math.sqrt((x ** 2) + (y ** 2))



