import csv
from cs50 import get_string

with open("phonebook.csv", "a") as file:
    name = get_string("Name: ")
    phone = get_string("Phone: ")

    writer = csv.writer(file)
    writer.writerow([name, phone])

# No need if with used
# file.close()
