class Tree:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name


class Palm(Tree):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color

    def get_color(self):
        return self._color

def main():
    palm1 = Palm("Lucky", 30, "Green")
    print(palm1.get_name())
    print(palm1.get_color())

if __name__ == '__main__':
    main()