class Car:
    def __init__(self, name, price, capacity, color, model):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.color = color
        self.model = model

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Capacity: {self.capacity}, Color: {self.color}, Model: {self.model}"

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCapacity(self, capacity):
        self.capacity = capacity

    def getCapacity(self):
        return self.capacity

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModel(self, model):
        self.model = model

    def getModel(self):
        return self.model


class Address:
    def __init__(self, country, city, street):
        self.country = country
        self.city = city
        self.street = street

    def __str__(self):
        return f"Country: {self.country}, City: {self.city}, Street: {self.street}"

    def setCountry(self, country):
        self.country = country

    def getCountry(self):
        return self.country

    def setCity(self, city):
        self.city = city

    def getCity(self):
        return self.city

    def setStreet(self, street):
        self.street = street

    def getStreet(self):
        return self.street


class CarShowroom:
    def __init__(self, address, name):
        self.address = address
        self.cars = []
        self.name = name
        self.rating = []

    def __str__(self):
        avg_rating = self.getAverageRating() if self.rating else "No ratings yet"
        return (f"Showroom Name: {self.name}\n"
                f"Address: {self.address}\n"
                f"Number of Cars: {len(self.cars)}\n"
                f"Average Rating: {avg_rating}")

    def addCar(self, car):
        self.cars.append(car)

    def removeCar(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def getCarsInfo(self):
        for car in self.cars:
            print(car)

    def getAddress(self):
        print(self.address)

    def changeAddress(self, new_address):
        self.address = new_address

    def changeName(self, new_name):
        self.name = new_name

    def getName(self):
        print(self.name)

    def rate(self, rate):
        if 0 < rate <= 5:
            self.rating.append(rate)

    def getAverageRating(self):
        if not self.rating:
            return "No ratings yet"
        return sum(self.rating) / len(self.rating)


# Usage example
address = Address("Uzbekistan", "Tashkent", "Main Street")
showroom = CarShowroom(address, "Best Cars")

car1 = Car("Toyota", 20000, 5, "Red", "Corolla")
car2 = Car("Honda", 22000, 5, "Blue", "Civic")

showroom.addCar(car1)
showroom.addCar(car2)

showroom.getCarsInfo()
showroom.rate(4)
showroom.rate(5)

print(showroom)
