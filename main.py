class Calculator:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y 

    @staticmethod
    def subtract(x: float, y: float) -> float:
        return x - y

    @staticmethod
    def multiply(x: float, y: float) -> float:
        return x * y

    @staticmethod
    def divide(x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y



calc = Calculator(0,0)

print(Calculator.add(5, 2))
print(Calculator.subtract(5, 2))
print(Calculator.multiply(5, 1))
print(Calculator.divide(0, 2))


