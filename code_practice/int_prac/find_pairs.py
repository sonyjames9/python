def find_pairs(list_num, total_sum):

    pairs = []
    seen = []
    for sum1 in list_num:
        sum2 = total_sum-sum1
        if sum2 in list_num:
            if sum1 not in seen or sum2 not in seen:
                pairs.append((sum1, sum2))
                seen.append(sum1)
                seen.append(sum2)
    return pairs


print(find_pairs([1, 4, 3, 3, 2, 5, 6], 7))
