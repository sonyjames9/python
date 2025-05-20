def find_primes(num):
    for prime_ctr in range(2, num+1):
        for div in range(2, prime_ctr):
            if prime_ctr % div == 0:
                break
        else:
            print(prime_ctr, end=" ")


find_primes(11)
