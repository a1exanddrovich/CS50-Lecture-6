import csv
from cs50 import SQL

db = SQL("sqlite:///favs.db")

title = input("Title: ").strip()

# ? will substitute with title
rows = db.execute("SELECT COUNT(*) AS counter FROM favs WHERE title LIKE ?", title)

row = rows[0]

print(row["counter"])

rows = db.execute("SELECT title FROM favs WHERE title LIKE ?", title)

for row in rows:
    print(row["title"])

