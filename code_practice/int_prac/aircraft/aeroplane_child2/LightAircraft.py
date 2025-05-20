from code_practice.int_prac.aircraft.aeroplane.Aeroplane import Aeroplane


class LightAircraft(Aeroplane):
    def __init__(self, name, max_altitude, wing_span, properller_type):
        super().__init__(name, max_altitude, wing_span)
        self.propeller_type = properller_type

    def purpose(self):
        print(f"{self.name} carries cargo upto {self.__cargo_capacity} tons")


