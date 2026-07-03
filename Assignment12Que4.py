def Display(no):
    for i in range(1, no + 1):
        print(i, end=" ")


def main():
    Value = int(input("Enter a Number: "))
    Display(Value)


if __name__ == "__main__":
    main()