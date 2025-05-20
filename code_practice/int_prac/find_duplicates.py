def find_duplicates(numbers):

    duplicates = []
    seen = set()

    for number in numbers:
        if number in seen:
            duplicates.append(number)
        else:
            seen.add(number)

    return duplicates


print(find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]))
