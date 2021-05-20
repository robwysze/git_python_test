from person import Person


def main():
    new_person = Person(name="Ibarbo", age=31)
    quot = new_person.introduce()
    print(quot)


if __name__ == "__main__":
    main()
