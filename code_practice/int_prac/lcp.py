def lcp(list_strs):
    if not list_strs:
        return ""

    for ctr in range(len(list_strs[0])):
        char = list_strs[0][ctr]
        for ch in list_strs[1:]:
            print(f"ch {ch}")
            print(f"ctr {ctr}")
            print(f"len(ch) {len(ch)}")
            print(f"ch[ctr] {ch[ctr]}")
            print(f"char {char}")
            if ctr >= len(ch) or ch[ctr] != char:
                print (f" list_strs[0][:ctr] {list_strs[0][:ctr]}")
                return list_strs[0][:ctr]

    print (f" list_strs[0] {list_strs[0]}")
    return list_strs[0]


print(lcp(["flower", "flow", "flight"]))

print(lcp(["flow", "flow", "flow"]))
