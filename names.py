import sys

names = ["Ron", "Harry", "Fred", "Ginny"]

if "Ron" in names:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)