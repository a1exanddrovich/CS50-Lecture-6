from cs50 import get_int


points = get_int("How many points did you lose?")

if points < 2:
    print("Fewer than me")
elif points > 2:
    print("More than me")
else:
    print("The same")
