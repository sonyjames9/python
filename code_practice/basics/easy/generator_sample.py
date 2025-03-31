def generator_func():
    for i in range(3):
        yield i


# for value in generator_func():
#     print(value)


def simple_generator():
    print("Step 1: Start execution")
    yield 1  # Pauses here
    print("Step 2: Resuming execution")
    yield 2  # Pauses again
    print("Step 3: Resuming execution and finishing")
    return "Done"

gen = simple_generator()  # Creates generator object


while True:
    try:
        print(next(gen))  # Step 1 executes, pauses at yield 1
        print(next(gen))  # Step 2 executes, pauses at yield 2
        # print(next(gen))  # Step 3 executes, function ends
        value = next(gen)
        print("Received:", value)
    except StopIteration as e:
        print("Generator has stopped: ", e.value)
        break
# print(next(gen))  # Raises StopIteration
