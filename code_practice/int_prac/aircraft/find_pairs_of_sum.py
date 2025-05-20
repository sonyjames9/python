
def find_pairs(list_num, total_sum):
    pair = []
    seen = []
    for num in list_num:
        num2 = total_sum - num
        if num not in seen:
            if num2 in list_num:
                pair.append((num, num2))
                seen.append(num)
                seen.append(num2)

    return pair


print(find_pairs([1, 4, 3, 3, 2, 5, 6], 7))
