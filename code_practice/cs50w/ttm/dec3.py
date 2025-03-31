class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


print(Math.add(6, 8))
print(Math.multiply(6, 8))



class Person:
    species = "monkeys"

    @classmethod
    def get_species(cls):
        print(cls)
        return cls.species


print(Person.get_species())
