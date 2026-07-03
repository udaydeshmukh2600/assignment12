def Check(ch):
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
       ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        print("Vowel")
    else:
        print("Consonant")


def main():
    Value = input("Enter a Character: ")
    Check(Value)


if __name__ == "__main__":
    main()