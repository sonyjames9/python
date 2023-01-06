# fizz buzz
# print numbers from 1 - 100
# if the number is multiple of 3, print fizz
# if the number is multiple of 5, print buzz
# if the number is multiple of both print fizzbuzz

def fizzbuzz():

    # Loop
    for num in range(1, 100):

        # Print fizzbuzz when number is divisible by 15
        if num % 15 == 0:
            print(f"number {num} fizzbuzz")

        # Print fizz when number is divisible by 3
        elif num % 3 == 0:
            print(f"number {num} fizz")

        # Print buzz when number is divisible by 5
        elif num % 5 == 0:
            print(f"number {num} buzz")


fizzbuzz()
