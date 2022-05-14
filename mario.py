def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        try:
            n = int(input("Enter the height: "))
            if n > 0:
                break
        except ValueError:
            print("Not a number")
    return n


if __name__ == '__main__':
    main()