try:
    x = int(input("x: "))
except:
    print("Not int war passed")
    exit()

x = cs50.get_int("x: ")
y = cs50.get_int("y: ")
z = x / y

print(f"{z:.50}")
