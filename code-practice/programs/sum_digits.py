def sum_of_digits(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    res = 0
    # while n != 0:
    #   res = res + (n % 10)
    #   n = n // 10
    # return res

    if n > 0:
      # res += n%10
      # n = n // 10
        # return sum_of_digits(res)
      return (res + (n % 10)) + sum_of_digits(n//10)

    # for digit in str(n):
    #   res = res + int(digit)
    # return res


print(sum_of_digits(11))
print(sum_of_digits(29))
print(sum_of_digits(99))
print(sum_of_digits(199))
