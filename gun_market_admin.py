guns = []
ids = []
calibrs = []
authors = []
years = []
countries = []

all_guns = ()
count = 0
count1 = 0

while count < 1:
    with open("guns.txt", "r", encoding="windows-1251") as gunlist:
        for line in gunlist:
            all_guns = list(all_guns)
            all_guns.append(line[0:-1].split("," " "))
            all_guns = tuple(all_guns)
        count = 1

for items in all_guns:
    items[0] = int(items[0])
    items[4] = int(items[4])
    items[5] = float(items[5])
    ids.append(items[0])
    guns.append(items[1])
    authors.append(items[2])
    countries.append(items[3])
    years.append(items[4])
    calibrs.append(items[5])


admin_menu = ("Просмотр всего оружия", "Добавить оружие", "Удалить оружие по id")
log_and_pass = (102103, "Anton")
password = 0

while password < 3:
    try:
        authorize = str(input("Войти в личный кабинет?(yes/no): "))
        if authorize == "yes":
            pass
        elif authorize == "no":
            break
        else:
            print("Вы ввели некорректные данные. попробуйте еще раз.")
            continue
        login_input = str(input("Введите свой логин(Anton): "))
        password_input = int(input("Введите пароль для входа в режим разработчика"
                                   "(102103): "))
        if login_input in log_and_pass:
            if password_input in log_and_pass:
                print("Вы вошли в режим разработчика.")
                print(f"Список доступных полномочий: {admin_menu} \n")
                while True:
                    admin_input = str(input("Хотите что либо изменить?(yes/no): "))
                    if admin_input == "yes":
                        menu_input = str(
                            input("Просмотр всего оружия - 1, Добавить оружие - 2, Удалить оружие по id - 3: "))
                        if menu_input == str("1"):
                            for line in all_guns:
                                print(line)
                        elif menu_input == str("2"):
                            new_gun = ""
                            count1 = 0
                            while count1 < 1:
                                try:
                                    add_id = int(input("Введите id: "))
                                    if add_id in ids:
                                        print("Такой id уже есть в системе. Выберите другой.")
                                        continue
                                    add_gun = str(input("Введите название оружия: "))
                                    if add_gun in guns:
                                        print("Такое оружие уже есть в системе. Выберите другое.")
                                        continue
                                    add_author = str(input("Введите автора: "))
                                    add_country = str(input("Введите страну производителя: "))
                                    add_year = int(input("Введите год выпуска: "))
                                    add_calibr = float(input("Введите калибр оружия: "))
                                except ValueError as verr:
                                    print(f"Тип ошибки {verr}")
                                    new_gun = ""
                                    count1 = 0
                                    continue
                                count1 = 1
                                new_gun = str(add_id) + ", " + str(add_gun) + ", " + str(add_author) + ", " + str(
                                    add_country) + \
                                          ", " + str(add_year) + ", " + str(add_calibr) + "\n"
                                with open("guns.txt", 'a', encoding="windows-1251") as gunstxt:
                                    gunstxt.write(str(new_gun))
                                ids.append(add_id)
                                guns.append(add_gun)
                                authors.append(add_author)
                                countries.append(add_country)
                                years.append(add_year)
                                calibrs.append(add_calibr)
                                count = 0
                                while count < 1:
                                    with open("guns.txt", "r", encoding="windows-1251") as gunlist:
                                        all_guns = list(all_guns)
                                        all_guns.append(new_gun[0:-1].split("," " "))
                                        all_guns = tuple(all_guns)
                                        new_gun = ""
                                    for items in all_guns:
                                        items[0] = int(items[0])
                                        items[4] = int(items[4])
                                        items[5] = float(items[5])
                                    count = 1
                            print("Оружие было добавлено.")
                        elif menu_input == str("3"):
                            for line in all_guns:
                                print(line)
                            print()
                            while True:
                                try:
                                    delete = int(input("Выберите id оружия, которое надо удалить: "))
                                    if delete not in ids:
                                        print("Такого id несуществует. Введите другой id.")
                                        continue
                                    for line in all_guns:
                                        if delete == line[0]:
                                            print(line)
                                    confirm = str(input("Вы действительно хотите удалить это оружие?(yes/no): "))
                                    if confirm == "yes":
                                        for del_gun in all_guns:
                                            if del_gun[0] == delete:
                                                all_guns = list(all_guns)
                                                all_guns.remove(del_gun)
                                                all_guns = tuple(all_guns)
                                                if delete in ids:
                                                    ids.remove(delete)
                                                if del_gun[1] in guns:
                                                    guns.remove(del_gun[1])
                                                if del_gun[2] in authors:
                                                    authors.remove(del_gun[2])
                                                if del_gun[3] in countries:
                                                    countries.remove(del_gun[3])
                                                if del_gun[4] in years:
                                                    years.remove(del_gun[4])
                                                if del_gun[5] in calibrs:
                                                    calibrs.remove(del_gun[5])
                                        with open("guns.txt", "r", encoding="windows-1251") as gunlist:
                                            for line in gunlist:
                                                if str(delete) not in line[0:line.index(",")]:
                                                    new_file = open("newfile.txt", "a", encoding="windows-1251")
                                                    new_file.write(line)
                                                    new_file.close()
                                                    with open("guns.txt", "w", encoding="windows-1251") as gunlist:
                                                        pass
                                        with open("guns.txt", "a", encoding="windows-1251") as gunlist:
                                            new_file = open("newfile.txt", 'r', encoding="windows-1251")
                                            for line in new_file:
                                                gunlist.write(line)
                                            new_file.close()
                                        with open("newfile.txt", "w", encoding="windows-1251") as newfile:
                                            pass
                                        print("Оружие было успешно удалено.")
                                        break
                                    elif confirm == "no":
                                        break
                                    else:
                                        print("Вы ввели некорректные данные. Введите еще раз.")
                                        continue
                                except ValueError as verr:
                                    print(f"Тип ошибки {verr}")
                                    continue
                    elif admin_input == "no":
                        print("До свидания. Был выполнен выход из личного кабинета.")
                        break
                    else:
                        print("Вы ввели некорректные данные. Был выполнен выход из личного кабинета.")
                        break
            else:
                print("Вы ввели неверный пароль.")
                password += 1
        else:
            print("Вы ввели неверный логин.")
            password += 1
    except ValueError as verr:
        print(f"Ошибка типа {verr}")
        password += 1
    if password == 3:
        print("Ваши попытки исчерпаны. Обновите страницу.")
        exit()
