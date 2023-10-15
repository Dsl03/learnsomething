import timeit
import math

def sieve_eratosthenes(n):
    is_prime = [True] * (n + 1)
    # 0 and 1 are not prime numbers
    is_prime[0] = False
    is_prime[1] = False

    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    return [i for i, prime in enumerate(is_prime) if prime]

def disasterCode():
    primes = sieve_eratosthenes(1000)

    # Create a dictionary of prime factors
    primes_table = {i: set() for i in range(2, 1000)}

    # Fill the dictionary
    for num in range(2, 1000):
        n = num
        # Iterate over the list of prime numbers
        for p in primes:
            while n % p == 0:
                # Add the prime factor to the set
                primes_table[num].add(p)
                # Divide the number by the prime factor
                n //= p
            # If the number is 1, stop the loop
            if n == 1:
                break

# Benchmark the code
if __name__ == "__main__":
    benchmark_code = "disasterCode()"
    setup_code = "from __main__ import disasterCode"

    # Measure the execution time of disasterCode function
    times = []
    for i in range(5):
        times.append(timeit.timeit(benchmark_code, setup=setup_code, number=1))

    res = sum(times) / 5
    print(f"Average execution time after 5 runs: {res:.6f} seconds")
