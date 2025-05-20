def lcp_start_char(list_strs):
    if not list_strs:
        return ""

    min_str_length = min(len(s_list) for s_list in list_strs)

    for ctr_first_str in range(min_str_length):
        char_first_str = list_strs[0][ctr_first_str]

        for other_string in list_strs[1:]:
            if other_string[ctr_first_str] != char_first_str:

                return list_strs[0][:ctr_first_str]

    return list_strs[0]


print(lcp_start_char(["flower", "flow", "flight"]))
print(lcp_start_char(["flow", "flow", "flow"]))


def lcp_prefix_while(list_strs):
    if not list_strs:
        return ""

    prefix_first_str = list_strs[0]

    for other_str in list_strs[1:]:

        while not other_str.startswith(prefix_first_str):
            prefix_first_str =  prefix_first_str[:-1]
            if not prefix_first_str:
                return ""

    return prefix_first_str

print(lcp_prefix_while(["flower", "flow", "flight"]))
print(lcp_prefix_while(["flow", "flow", "flow"]))
