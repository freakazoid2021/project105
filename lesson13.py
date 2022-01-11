# def input_data():
#     while True:
#         try:
#             user_input = int(input("Enter digit: "))
#             print("'Hello")
#             a = 5
#             b = 0
#             try:
#                 c = a / b
#             # except BaseException:
#             #     print("base exception")
#
#             # except ArithmeticError:
#             #     print("Arithmetic error")
#
#             except ZeroDivisionError:
#                 print("zero except")
#
#             print("end block try")
#
#             list1 = []
#             list2 = ["1", "2", "3.4", "6", "word"]
#             error_list = []
#
#             for i in range(len(list2)):
#                 try:
#                     list1.append(int(list2[i]))
#                 except ValueError as errval:
#                     list1.append(list2[i])
#                     error_list.append(errval)
#             else:
#                 print("ok")
#             print(list1)
#             print(error_list)
#             print(dir(BaseException))
#
#         except BaseException:
#             user_input = 0
#
#         print(user_input)
#
#
# # input_data()
#
# try:
#     user_input = int(input("Enter digit: "))
#     file = open("lesson13.py", 'r')
#
# except ValueError as verr:
#     print(verr)
#
# else:
#     print("it was without error")
#
# finally:
#     print("do always this block")
#     try:
#         file.close()
#     except NameError as name_err:
#         print(name_err)
#

