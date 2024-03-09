class Human:
    default_name = "Ramil"
    default_age = 0

    def __init__(self,name: str = default_name, age: int = default_age):
        self.default_name = name
        self.default_age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.name, self.age, self.__money, self.__house)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, wages):
        self.__money += wages

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money > price:
            print(self.make_deal)
        else:
            print("У вас не хватает денег")

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount: int):
        return round(self._price*(100-discount)/100)

class SmallHouse (House):
    defaulr_area = 40
    def __init__(self, price):
        super().__init__(SmallHouse.defaulr_area, price)

Human.default_info()
human = Human()
human

smallhouse = SmallHouse(600)
Human.buy_house(self="", house=40,discount=5)




