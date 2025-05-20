from code_practice.int_prac.aircraft.base.Aircraft import Aircraft


class UAV(Aircraft):
    def __init__(self, name, max_altitude, autonomous=True):
        super().__init__(name, max_altitude)
        self._autonomous = autonomous

    def purpose(self):
        print(f"{self.name} is a UAV drone. Autonomous: {self._autonomous}")
