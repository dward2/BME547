class Person:

    def __init__(self, first_name_arg, last_name_arg):
        self.firstname = first_name_arg
        self.lastname = last_name_arg

    def return_full_name(self):
        return self.firstname + " " + self.lastname


def main():
    x = Person("Robert", "Smith")
    print("First Name = {}".format(x.firstname))
    print("Last Name = {}".format(x.lastname))
    print("")
    print("Full Name = {}".format(x.return_full_name()))
    pass


if __name__ == '__main__':
    main()