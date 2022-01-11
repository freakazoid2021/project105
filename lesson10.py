# import sys
# import timeit
#
# lst = [i for i in range(10_000_000)]
# tp = (i for i in range(10_000_000))
#
# # 10.000,00$
# # 10_000_000
# lst2 = [1, 2, 4, 5]
# # lst2.extend(lst)
# tup = ("name", "surname", lst2)
#
# print(sys.getsizeof(lst2))
# print(sys.getsizeof(tup))
#
# print(dir(list))
# print(dir(tuple))
#
# print(timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,0]", number=1_000_000))
# print(timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9,0)", number=1_000_000))

# 1 create tuples
tuple1 = ()
tuple2 = tuple()
tuple3 = 'a',
tuple4 = ('a',)
tuple5 = 'a', 'b', 'c'
tuple6 = ('a', 'b', 'c', 'd')
tuple7 = ('a',)
lst1 = [1, 2, 3, 4]
tuple8 = tuple(lst1)

# 2
tuple9 = ("abc", 1, 4.56, [1, 2, 3, 4], True)
print(tuple9)

# tuple9[3].extend(lst1)
# print(tuple9)

abrakadabra, my_int, it_is_float, a_list, it_is_not_true = tuple9
print(f"{abrakadabra=}, {my_int=}, {it_is_float=}, {a_list=}, {it_is_not_true=}")

user = ("3456", "Follower", "15")
user_id, nickname, age = user
print(f"{user_id=}, {nickname=}, {age=}")
print(id(user))
user = user * 1
print(id(user))
print(user)

new_user = ("Warrior",) + user
print(new_user)

new_user = new_user[:2] + ("Gun",) + new_user[2:]
print(new_user)

str1 = ' '.join(new_user)
print(str1)

str2 = ''
for i in range(len(tuple9)):
    str2 += ' ' + str(tuple9[i])

print(str2)

lst2 = list(str1.split('3456'))
tuple10 = tuple(str1.split())
print(tuple10)
print(lst2)

print(tuple10[::-1])

print(tuple10.index("3456"))
print(tuple10.count("Warrior"))

player1_id = tuple10[tuple10.index("3456")]
print(type(int(player1_id)))
lst5 = ['1', '2', '3', '4', '5']
lst6 = [i * 0.1 for i in range(6)]
lst3 = list(tuple6[::-1])
print(zip(lst1, lst3))
lst4 = list(zip(lst1, lst3, lst5, lst6))
tuple11 = []
print(lst4)
# 1 2 3 4
# a b c d
# 0 9 8 7
# -> (1 a 0)
lst7 = sorted(lst4, key=lambda x: x[1])
print(lst7)

# Books > 15
# id = int(random)
# name_book = str(list1[random] + list2[random])
# author = str(list4[random])
# year = int(random)
# quantity_site = int(random)
# country = str(list3[random])
#
# tuple/ list
# user interface:
# 1. user input id -> book
# 2. user input author 'A...' -> all books where author begin 'A'
# 3. user input country ...
# 4. user input year -> > user year
#
