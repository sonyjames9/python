from abc import ABC, abstractmethod


class Aircraft(ABC):
    def __init__(self, name, max_altitude):
        self.name = name
        self._max_altitude = max_altitude
        self.__engine_type = "Jet"

    def get_engine_type(self):
        return self.__engine_type

    def set_engine_type(self, engine_type):
        if engine_type in ["Jet", "Turboprop", "Piston", "Electric"]:
            self.__engine_type = engine_type
        else:
            raise ValueError("Invalid engine type provided")

    def fly(self):
        print(f"{self.name} is flying at altitude {self._max_altitude} feet.")

    @abstractmethod
    def purpose(self):
        pass
