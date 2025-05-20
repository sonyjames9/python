from code_practice.int_prac.aircraft.aeroplane.Aeroplane import Aeroplane


class FighterJet(Aeroplane):
    def __init__(self, name, max_altitude, wing_span, missile_count):
        super().__init__(name, max_altitude, wing_span)
        self.__missile_count = missile_count

    def get_missile_count(self):
        return self.__missile_count

    def purpose(self):
        print(f"{self.name} is a fighter jet with {self.__missile_count} missiles.")
