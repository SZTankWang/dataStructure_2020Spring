class Student:
    def __init__(self, name, age, GPA):
        self.name = name
        self.age = age
        self.GPA = GPA

    def get_GPA(self):
        return self.GPA

    def set_GPA(self, GPA):
        self.GPA = GPA


def main():
    bob = Student("Bob", 15, 3.0)
    print(bob.get_GPA())

    bob.set_GPA(4.0)
    print(bob.get_GPA())

if __name__ == '__main__':
    main()





