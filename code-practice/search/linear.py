# Linear Search


from typing import Iterator


def linear_search():

    list_to_search = [int(x) for x in input(
        "Enter the list of values").split(',')]
    # list_to_search = map(int, input("Enter the list of values : ").split(','))
    # # list_to_search = list((input("Enter the list")))
    print(id(list_to_search))
    print(type(list_to_search))
    print(list_to_search)

    search_value = int(input("Enter the value to be searched : "))

    for element in list_to_search:
        if element == search_value:
            return f"Value {search_value} found"

    return "Value not in list"


# print(linear_search())


def binary_search_input():
    list_to_search = [int(x) for x in input(
        "Enter the list of values").split(',')]
    print(list_to_search)
    list_to_search.sort()
    print(list_to_search)
    search_value = int(input("Enter the value to be searched : "))
    binary_search(list_to_search, 0, len(list_to_search) - 1, search_value)


def binary_search(list_to_search, left, right, search_value):
    # left = list_to_search[0]
    # right = list_to_search[0]
    print("before right left comparison")
    if right > left:
        print("right greater than left")
        mid = left+(right-1)//2
        if list_to_search[mid] == search_value:
            print("mid value is the value required")
            return f"{search_value} found at {mid}"

        elif list_to_search[mid] > search_value:
            print("mid value greater than search value")
            return binary_search(list_to_search, 1, mid - 1, search_value)

        else:
            print("mid value lesser than search value")
            return binary_search(list_to_search, mid+1, right, search_value)
    else:
        return "Value not in list"


print(binary_search_input())
