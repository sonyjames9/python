# from collections import default_dict

def max_occ(list_num):

 num_occ = {}
 for num in list_num:
   if num in num_occ:
     num_occ[num] += 1
   else:
     num_occ[num] = 1

 max_key = max(num_occ, key=num_occ.get)
 max_val = num_occ[max_key]

 print(max_key, max_val)
 return max_key, max_val

list_num = [1,2,3,4,5,1,2,6,7,1,8,9,1,2,3,4,1,10,11,1]
print(max_occ(list_num))


def transpose_mat(mat):
    rows = len(mat)
    cols = len(mat[0])
    transposed_mat = []

    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(mat[j][i])
        transposed_mat.append(row)

    return transposed_mat


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print(transpose_mat(mat))