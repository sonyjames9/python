
def transpose_matrix(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    transposed_mat = []

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        transposed_mat.append(new_row)

    return transposed_mat


print(transpose_matrix([[1,2,3],[4,5,6]]))
