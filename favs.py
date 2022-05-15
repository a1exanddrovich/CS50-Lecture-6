import csv
import re

# see data from csv
titles = set()

with open("favs.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        titles.add(title)

for title in sorted(titles):
    print(title)

# analyze it - keep track of count how many times current title was used
titles = {}

with open("favs.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if title not in titles:
            titles[title] = 0
        titles[title] += 1


# used before introducing lambda
def get_value(title):
    return titles[title]


for title in sorted(titles, key=lambda title: titles[title], reverse=True):
    print(title)


# Cleaning data using simple regular expressions
counter = 0

with open("favs.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if re.search("^(OFFICE|THE.OFFICE)$", title):
            counter += 1

print(f"Number of people who like the office is {counter}")

# ask user for the title

title = input("Title: ").strip().upper()

counter = 0

with open("favs.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["title"].strip().upper() == title:
            counter += 1
