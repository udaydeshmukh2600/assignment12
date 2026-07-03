def ReverseDisplay(no):
    for i in range(no, 0, -1):
        print(i, end=" ")


def main():
    Value = int(input("Enter a Number: "))
    ReverseDisplay(Value)


if __name__ == "__main__":
    main()