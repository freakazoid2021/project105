# while loop

# while <expretion>: (True)
#   <statements>
#          i --> -->
# array = [0,1,2,3,4,5,6,7,8,9]
print("for loop")
for index in range(0, 10):
    print(index)

print("----------------------------")

# int i = 0 -> i += 1 --> i += 1 ---> i += 1 / 0, 1, 2...
print("while loop")
index = 0

while index < 10:
    print(index)
    index += 1

print("----------------------------")

array = [i for i in range(10, 20)]

index = 0

print(f"{array=}")

for i in array:
    i -= 10
    print(i, end=" ")

print('\n')

print(f"{array=}")

while index < len(array):
    array[index] -= 10
    index += 1

print(f"{array=}")

print("----------------------------")

# cities = []
# list
cities = ["Minsk", "Gomel", "Vitebsk", "Grodno", "Mogilev", "Brest"]

while cities:
    print(cities.pop(0))
    print(len(cities))

print("----------------------------")
# while - else
# tuple
index = 0

cities = ("Minsk", "Gomel", "Vitebsk", "Grodno", "Mogilev", "Brest")

while index < len(cities):
    print(cities[index])
    index += 1
else:
    print("cities done")

print("----------------------------")

# tuple
# continue break
index = 0

while index < len(cities):
    if 'o' in cities[index]:
        index += 1
        continue
    else:
        print(cities[index])
    index += 1
else:
    print("cities done")

index = 0

while index < len(cities):
    if cities[index] == "Vitebsk":
        break

    print(cities[index])
    index += 1
else:
    print("cities done")

print("----------------------------")

index = 0

while True:
    print(cities[index])
    if cities[index] == "Vitebsk":
        break

    index += 1

print("infinity loop done")

print("----------------------------")
print("welcome to Vitalur!! ")

# number = int(input("enter number: "))
#
# result = 0
# counter = 0
#
# while number != 0:
#     result += number
#     number = int(input("enter number: "))
#     counter += 1
#
# print(f"Total price: {result} blr, items: {counter}")

# print("----------------------------")
#
# user_password = "qwerty1234"
#
# password = input("enter your password: ")
#
# while user_password != password:
#     print("invalid password. try again or write administrator")
#     password = input("enter your password: ")
#
# print("welcome to mail")

print("----------------------------")

login_users = ["Alexey", "Denis", "Dmitry", "Svetlana"]

while True:
    new_login = input("Enter your login: ")

    if new_login in login_users:
        print(f"{new_login} exists. please enter other login ")
        continue
    else:
        login_users.append(new_login)
        print(f"welcome to website, {new_login}")
        break

# qwERty@#12
print("password must be from 6 to 10 symbols, must contain digits, lower and upper cases, !@#$%^/&*-=_")
user_password = input("enter password: ")

while True:
    length, digits, lowers, uppers, symbols = 0, 0, 0, 0, 0

    if 6 < len(user_password) < 10:
        length = 1

    for i in user_password:
        if i.isdigit():
            digits = 1
            continue
        elif i.islower():
            lowers = 1
            continue
        elif i.isupper():
            uppers = 1
            continue
        elif i in "!@#$%^/&*-=_":
            symbols = 1
            continue

    expression = (length, digits, lowers, uppers, symbols)

    if all(expression):
        print("hard password")
        break
    else:
        print("very simple password. try again.")
        print("password must be from 6 to 10 symbols, must contain digits, lower and upper cases, !@#$%^/&*-=_")
        user_password = input("enter password: ")

# welcome message
print(f"Welcome to googlemail, {new_login}!!")
