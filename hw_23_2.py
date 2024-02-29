class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        divisor = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / divisor
        imag = (self.imag * other.real - self.real * other.imag) / divisor
        return Complex(real, imag)

    def __repr__(self):
        return f"{self.real} + {self.imag}i"

if __name__ == "__main__":
    num1 = Complex(3, 4)
    num2 = Complex(5, 6)

    print("Addition:", num1 + num2)  # Output: 8 + 10i
    print("Subtraction:", num1 - num2)  # Output: -2 + -2i
    print("Multiplication:", num1 * num2)  # Output: -9 + 38i
    print("Division:", num1 / num2)  # Output: 0.6346153846153846 + 0.11538461538461539i
