from task_1 import Human, SmallHouse

Human.default_info()

human = Human()
human.info()

house = SmallHouse()
human.buy_house(house, 0.1)

human.earn_money(888)
human.buy_house(house, 0.1)

human.info()