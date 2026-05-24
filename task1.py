def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0

        if n == 1:
            return 1

        # Return value from cache if already calculated
        if n in cache:
            return cache[n]

        # Calculate and save value to cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


# Get fibonacci function
fib = caching_fibonacci()

# Use fibonacci function
print(fib(10))  # 55
print(fib(15))  # 610