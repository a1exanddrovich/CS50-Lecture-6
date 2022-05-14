from cs50 import get_string

s = get_string("Do u agree?").lower()

if s == "y":
    print("U agreed")
elif s == "n":
    print("U disagreed")

