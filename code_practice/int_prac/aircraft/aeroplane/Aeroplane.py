from code_practice.int_prac.aircraft.base.Aircraft import Aircraft


class Aeroplane(Aircraft):
    def __init__(self, name, max_altitude, wing_span):
        super().__init__(name, max_altitude)
        self.wing_span = wing_span

    def purpose(self):
        print(f"{self.name} is a general-purpose aeroplane")

