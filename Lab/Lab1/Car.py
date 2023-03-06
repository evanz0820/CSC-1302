class Car:
    def __init__(self, maker, year, price):
        self.maker = maker
        self.year = year
        self.price = price

    def printCar(self):
        print("Car's information:")
        print(" Car maker: ", self.maker)
        print(" Model year: ", self.year)
        print(" Purchase price: $", self.price)

c = Car('Toyota', 2023, 47000)
c.printCar()