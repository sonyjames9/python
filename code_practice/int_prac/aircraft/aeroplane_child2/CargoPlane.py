from code_practice.int_prac.aircraft.aeroplane.Aeroplane import Aeroplane


class CargoPlane(Aeroplane):
    def __init__(self, name, max_altitude, wing_span, cargo_capacity):
        super().__init__(name, max_altitude, wing_span)
        self.__cargo_capacity = cargo_capacity

    def get_cargo_capacity(self):
        return self.__cargo_capacity

    def purpose(self):
        print(f"{self.name} carries cargo upto {self.__cargo_capacity} tons")
