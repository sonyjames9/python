def adder(value):
    def inner_function(base):
        return base + value

    return inner_function


adder_5 = adder(5)
adder_10 = adder(10)
result = adder_5(10)
result2 = adder_5(7)
result3 = adder_10(9)
print(result, result2, result3)
