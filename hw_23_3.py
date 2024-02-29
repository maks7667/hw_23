class Airplane:
    def __init__(self, model, max_passengers, current_passengers):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.model == other.model

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __add__(self, other):
        total_passengers = self.current_passengers + other.current_passengers
        return Airplane(self.model, self.max_passengers, total_passengers)

    def __iadd__(self, other):
        self.current_passengers += other.current_passengers
        return self

    def __sub__(self, other):
        total_passengers = self.current_passengers - other.current_passengers
        return Airplane(self.model, self.max_passengers, total_passengers)

    def __isub__(self, other):
        self.current_passengers -= other.current_passengers
        return self

if __name__ == "__main__":
    plane1 = Airplane("Boeing 747", 500, 200)
    plane2 = Airplane("Airbus A380", 600, 300)

    print("Проверьте равенство типов самолетов:", plane1 == plane2)
    print("Проверьте, может ли самолет 1 перевозить больше пассажиров, чем самолет 2:", plane1 > plane2)
    print("Проверьте, может ли самолет 2 перевозить больше пассажиров, чем самолет 1:", plane1 < plane2)

    print("Общее количество пассажиров в обоих самолетах:", (plane1 + plane2).current_passengers)

    plane1 += plane2
    print("Обновлено количество пассажиров в самолете 1 после добавления:", plane1.current_passengers)

    plane1 -= plane2
    print("Обновлено количество пассажиров в самолете 1 после вычитания: ", plane1.current_passengers)
