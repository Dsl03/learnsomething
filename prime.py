import timeit
import math

def optimized_sieve(n):
    # List to store prime factors
    factors = [list() for _ in range(n + 1)]

    for p in range(2, n + 1):
        if not factors[p]: # If the number is a prime (has no factors yet)
            for multiple in range(p, n + 1, p):
                factors[multiple].append(p)

    return factors

def disasterCode():
    factors = optimized_sieve(2500)

    # This loop is just to "use" the factors to ensure a fair comparison
    for num in range(2, 2500):
        _ = factors[num]

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
