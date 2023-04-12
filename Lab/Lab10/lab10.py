class Vehicle:
    #Class attribute
    special = 'Bus'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

a = Vehicle('Bus', 80, 100000)