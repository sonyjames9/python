def find_array_pair_sum(array, sum):
  array = sorted(array)
  pair_dict = {}
  atleast_one_pair_found = False
  # print('Pair for sum : {}'.format(sum))
  for ctr, array_elem in enumerate(array):
    # print(ctr, array_elem)

    if sum - array_elem in pair_dict:
      print('Pair found for sum {} : {} {}'.format(
          sum, array[pair_dict.get(sum-array_elem)], array[ctr]))
      atleast_one_pair_found = True
    pair_dict[array_elem] = ctr
    # print(str(pair_dict)+" " + "ctr : " + str(ctr))

  if not atleast_one_pair_found:
    print("Pair not found for sum {}".format(sum))


find_array_pair_sum([1, 3, 3, 5, 7, -1, 2, 4], 90)
find_array_pair_sum([1, 3, 3, 5, 7, -1, 2, 4], 7)
find_array_pair_sum([1, 3, 3, 5, 7, -1, 2, 4], 6)
find_array_pair_sum([1, 3, 3, 5, 7, -1, 2, 4], 2)
find_array_pair_sum([1, 3, 3, 5, 7, -1, 2, 4], 3)
