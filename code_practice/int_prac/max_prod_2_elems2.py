def max_product(list_of_nums):
    if len(list_of_nums) < 2:
        return 0

    max_product = float('-inf')


    for f_ptr in range(len(list_of_nums)):
        for s_ptr in range(f_ptr):
            max_product = max(max_product, list_of_nums[f_ptr] * list_of_nums[s_ptr])

    # for s1 in list_of_nums:
    #     for s2 in list_of_nums[s1:]:
    #         if s1 != s2:
    #             print(f"s1, s2 {s1, s2}")
    #             print(f"s1*s2 {s1*s2}")
    #             max_product = max(max_product, s1 * s2)

    return max_product

print(max_product([-5, -10, 1, 2, 3, 4]))

