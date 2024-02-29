class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

if __name__ == "__main__":
    flat1 = Flat(80, 100000)
    flat2 = Flat(90, 120000)

    print("Are the areas of flat1 and flat2 equal?", flat1 == flat2)
    print("Are the areas of flat1 and flat2 not equal?", flat1 != flat2)
    print("Is the price of flat1 less than the price of flat2?", flat1 < flat2)
    print("Is the price of flat1 greater than the price of flat2?", flat1 > flat2)
