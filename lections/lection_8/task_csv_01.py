import csv

with open("C:/Users/1311103/OneDrive/Рабочий стол/GB/python_2/lections/lection_8/biostats.csv", "r", newline="") as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
    print(type(line))