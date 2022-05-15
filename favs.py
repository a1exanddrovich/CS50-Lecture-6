import csv

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




