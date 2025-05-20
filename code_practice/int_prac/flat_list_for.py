def flat_list(matrix):
    flat_list = []
    for row in matrix:
        for item in row:
            flat_list.append(item)

    return flat_list


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(flat_list(matrix))
