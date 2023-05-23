class Human:
    default_name = "John"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._money = 666
        self._house = None

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("House:", self._house)
        print("Money:", self._money)

    @staticmethod
    def default_info():
        print("Default Name:", Human.default_name)
        print("Default Age:", Human.default_age)

    def make_deal(self, house, price):
        if self._money >= price:
            self._money -= price
            self._house = house
            print("Deal successful!")
        else:
            print("Not enough money to make the deal.")

    def earn_money(self, amount):
        self._money += amount

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self._money >= final_price:
            self.make_deal(house, final_price)
        else:
            print("Not enough money to buy the house.")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount)


class SmallHouse(House):
    def __init__(self):
        super().__init__(area=40, price=100000)

