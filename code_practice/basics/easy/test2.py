class CargoShip:

    def __init__(self, capacity):
        self.cargo = []
        self.capacity = capacity

    def unload(self, port):
        """
        :param port: (String)
        :returns: [(String, Int)]
        """
        carg = self.cargo[0]
        for ctr in carg:
          if port in self.cargo:
            print(ctr[0])
        #   if port in ctr[0]:
        #     print(port)
        #     self.cargo.remove(ctr)
          for ctr2 in ctr:
            print(ctr2)
        #   if port in ctr2:
        #     print(ctr)
        #   self.cargo.remove(ctr2)
        #   print(ctr2)
        #   if port in ctr[]:
        #     print(port)

        # self.cargo.append(new_cargo)

    def can_depart(self):
        """
        :returns: (Bool)
        """
        return None

    def load(self, new_cargo):
        """
         :param new_cargo: [(String, Int)]
         """
        self.cargo.append(new_cargo)


if __name__ == "__main__":
    ship = CargoShip(10)
    ship.load([("New York", 1), ("London", 20)])
    print(ship.cargo)  # should print [("New York", 1)]
    print(ship.unload("New York"))  # should print [("New York", 1)]

    # print(ship.cargo)  # should print [("London", 20)]
    # print(ship.can_depart())  # should print False """
