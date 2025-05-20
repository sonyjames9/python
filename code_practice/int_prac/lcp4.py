def lcp_start_char(list_strs):

    min_len_str = min(len(strs) for strs in list_strs)

    for ctr_f_str in range(min_len_str):
        char_f_str = list_strs[0][ctr_f_str]

        for other_strs in list_strs[1:]:
            if other_strs[ctr_f_str] != char_f_str:
                return list_strs[0][:ctr_f_str]

    return list_strs[0]


print(lcp_start_char(["flower", "flow", "flight"]))
print(lcp_start_char(["flow", "flow", "flow"]))
