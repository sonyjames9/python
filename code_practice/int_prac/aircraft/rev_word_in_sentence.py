# ip = today is interview
# op = inter vi ewistoday

# reverese the statement keeping space as constraint
# today
# inter

def rev_stmt_with_space(input_str):
    words = input_str.split()
    words = words[::-1]
    words_str = ''.join(words)
                 # .replace(" ","")
    # words_str = words_str
    print(input_str)

    # for ctr in range(0, len(words_str)):
    #     print(words_str[ctr], end="")
    #
    # print()
    ctr1 = 0
    ctr2 = 0
    while ctr1 < len(input_str):

        if input_str[ctr1] != " ":
            print(words_str[ctr2], end="")
            ctr2 += 1
        elif input_str[ctr1] == " ":
            print(" ", end="")
        ctr1 += 1


input_str = "today is interview"
rev_stmt_with_space(input_str)
