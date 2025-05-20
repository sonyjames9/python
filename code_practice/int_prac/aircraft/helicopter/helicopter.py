from code_practice.int_prac.aircraft.base.Aircraft import Aircraft


class Helicopter(Aircraft):
    def __init__(self, name, max_altitude, rotor_blades):
        super().__init__(name, max_altitude)
        self.__rotor_blades = rotor_blades

    def get_rotor_blades(self):
        return self.__rotor_blades

    def purpose(self):
        print(f"{self.name} is used for rescue or transport with {self.__rotor_blades} blades.")
