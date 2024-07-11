class Shape:
    def __init__(self, shape='*'):
        self.shape = shape

    usr = int(input("Enter a number: "))
    def show(self):
        return self.shape

    def setSymbol(self, new_symbol):
        self.shape = new_symbol
        return self

    def setLength(self, new_length):
        self.shape = new_length
        return self


class Line(Shape):
    def __init__(self, shape='*'):
        super().__init__(shape)

    def show(self):
        return self.shape * self.usr


class Triangle(Shape):
    def __init__(self, shape='*'):
        super().__init__(shape)

    def show(self):
        for i in range(self.usr):
            for j in range(i):
                print("☆", end='')
            print()


class Rectangle(Shape):
    def __init__(self, shape='*'):
        super().__init__(shape)

    def show(self):
        for i in range(self.usr):
            for j in range(self.usr):
                print("☆", end=' ')
            print()


class NullShape(Shape):
    def __init__(self, shape='*'):
        super().__init__(shape)

    def show(self):
        return "Bo'sh Shakil"


# Example usage
shakl = Line('*')

try:
    while True:
        user_input = int(input("""\n0: Exit
1: Line
2: Triangle
3: Rectangle
4: NullShape
Enter command: """))
        if user_input == 1:
            print(shakl.show())
        elif user_input == 0:
            break

        elif user_input == 2:
            Triangle().show()
        elif user_input == 3:
            Rectangle().show()
        elif user_input == 4:
            print(NullShape().show())

        else:
            print("Invalid command")
except ValueError:
    print("Please enter a valid number.")
