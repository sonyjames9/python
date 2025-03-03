# functional - taking a function and modifying that function, adding some additional
# behavior to that function
# Idea of Decorator is that functional takes a function as input and modifies version
# of that function as output.
# Unlike other programming languages where functions just exist on their own and
# they cant be passed as input/output to other functions
# In Python a function is just a value like any other known as functional programming paradigm,
# where functions are themselves value.

def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")

    return wrapper


@announce
def hello():
    print("Hello World")


hello()
