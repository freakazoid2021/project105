import csv

chevrolet_dict = {}
chevrolet_set = set()

# 1. MPG - same for all chevrolet
# 2.

# with open("cars.csv", 'r', encoding='utf-8') as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter=';')
#     header = next(csv_reader)
#
#     mpg = float(input("enter mpg: "))
#
#     for line in csv_reader:
#         # print(list(line))
#         if "Chevrolet" in line[0]:
#             # print(line)
#             if  float(line[1]) >= mpg:
#                 chevrolet_set.add(tuple(line))
#
# for car in chevrolet_set:
#     print(car)
#
# with open("chevrolet_file.txt", 'w', encoding='utf-8') as txtfile:
#     txtfile.write(','.join(header) + '\n')
#     for car in chevrolet_set:
#         car = ','.join(car) + "\n"
#         txtfile.write(car)

with open("chevrolet_file.txt", 'r', encoding='utf-8') as txtfile:
    txtreader = txtfile.readlines()

    # header = next(txtreader)
    txtreader.pop(0)

    # print(txtreader)

    for i, line in enumerate(txtreader, 1):
        if 5 <= i <= 10:
            print(i, line)
            
# new line

import json

cars = {}

with open("cars.csv", 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')

    header = next(csv_reader)

    for i, line in enumerate(csv_reader):
        # print(tuple(zip(header, line)))
        cars[i] = dict(zip(header, line))

with open("cars.json", 'w', encoding='utf-8') as jsonfile:
    json.dump(cars,jsonfile, indent=4)
    
    
with open("cars.json", 'r', encoding="utf-8") as jsonfile:
    with open("carsgrate25mpg.json", 'w', encoding="utf-8") as newjson:
        with open("carsfromeurope.json", 'w', encoding="utf-8") as newjsoneurope:
            jsonreader = json.load(jsonfile)

            # print(jsonreader)
            new_cars = {}
            europe_cars = {}

            for key, value in jsonreader.items():
                for k, v in value.items():
                    if k == "MPG" and float(v) > 30:
                        new_cars[key] = value
                        print(key, value)
                    elif k == "Origin" and value == "US":
                        europe_cars[key] = value
                        print(key, value)

            print(europe_cars)

            json.dump(new_cars, newjson, indent=4)
            json.dump(europe_cars, newjsoneurope, indent=4)

fileus = ""
fileeurope = ''
filejapan = ''

formatfile = input("1 - csv, 2 - json, 3 - txt")
fileus + "." + formatfile
