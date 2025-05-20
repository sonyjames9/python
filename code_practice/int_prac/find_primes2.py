def find_primes(num_range):
    primes = []
    for ctr in range(2, num_range+1):
        for div in range(2, int(ctr/2)):
            if ctr % div == 0:
                break
        else:
            primes.append(ctr)
    return primes


print(find_primes(17))
