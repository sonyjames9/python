def Longest_Common_Prefix(lists_of_str):
  """
  Input: ["flower", "flow", "flight"]
  Output: "fl"
  """

  if not lists_of_str:
    return ""

  # Step 1: Find length of the shortest word
  min_length = min(len(list) for list in lists_of_str)

  # Step 2: Compare character by character
  for i in range(min_length):
    # Use first word's character as a reference
    char = lists_of_str[0][i]

    print(f"char 1: {char}")
    print(f"list {lists_of_str[i]}")
    for single_str in lists_of_str:
      print(f"single_str : {single_str}")
      if single_str[i] != char:
        
        print(f"single_str[i] : {single_str[i]}")
        print(f"char 2: {char}")
        # Return everything up to the mismatch
        return lists_of_str[0][:i]

  # If we made it through the loop, all prefixes match
  return lists_of_str[0][:min_length]


print(Longest_Common_Prefix(["flower", "flow", "flight"]))
print(Longest_Common_Prefix(["flower", "flow", "flowd"]))
print(Longest_Common_Prefix(["toy", "flow", "fliowd"]))
