import csv #Used to create the formatted output file

value1 = input("Please enter value 1: ")
value2 = input("Please enter value 2: ")

with open('pushup_values.csv', mode='w') as pushup_file:
    employee_writer = csv.writer(pushup_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow([value1, value2])
