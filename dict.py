from cs50 import get_string

people = {
    "Carter": "+234234234",
    "Jam": "+795379424"
}

name = get_string("Name: ")

if name in people:
    print(people[name])
