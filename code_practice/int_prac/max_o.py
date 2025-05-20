
def max_occ(list_num):
    num_occ = {}

    for num in list_num:
        if num in num_occ:
            num_occ[num] += 1
        else:
            num_occ[num] = 1

    print(num_occ)

    max_key = max(num_occ, key=num_occ.get)
    max_val = num_occ[max_key]

    return max_key, max_val


print(max_occ([1,1,1,3,2,1,4,3,2,4,1]))
