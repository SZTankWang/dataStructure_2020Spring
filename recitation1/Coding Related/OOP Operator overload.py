class Pizza:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        new_pizza = Pizza(self.price)
        new_pizza += other
        return new_pizza

    def __iadd__(self, other):
        self.price += other.price
        return self

    def __str__(self):
        return "the price is, " + str(self.price)



def main():
    pizza1 = Pizza(5)
    pizza2 = Pizza(6)
    pizza1 + pizza2
    pizza1 += pizza2
    print(pizza1)

if __name__ == '__main__':
    main()

