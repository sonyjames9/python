# def hello():  # type: ignore
#   print("Hello")

def hello(func):
  def inner():
    print("Hello1")
    func()
    print("Hello2")
  return inner

@hello
def name():
  print("Alice")

print("\n\nImplementing the decorator without the usual decorator @declaration above the function")
# without decorator and commenting the decorator @hello above the function name()
obj = hello(name)
obj()

print("\n\nUsing decorator with @ implementation")
# using decorator implementation and uncommenting the decorator @hello above the function name()
name()
