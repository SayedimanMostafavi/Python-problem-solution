def sieve_of_eratosthenes(limit):
    """
    Generate all prime numbers up to the given limit using the Sieve of Eratosthenes algorithm.
    
    Args:
        limit (int): The upper bound to find primes up to
        
    Returns:
        list: List of prime numbers up to the limit
    """
    # Create a boolean array "prime[0..limit]" and initialize all entries as True
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not prime numbers
    
    p = 2
    while p * p <= limit:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = []
    for i in range(2, limit + 1):
        if prime[i]:
            primes.append(i)
    
    return primes


def main():
    """Main function to find and print prime numbers up to 1000."""
    limit = 1000
    print(f"Prime numbers from 1 to {limit}:")
    print("-" * 40)
    
    primes = sieve_of_eratosthenes(limit)
    
    # Print primes in a formatted way (10 per line)
    for i, prime in enumerate(primes):
        print(f"{prime:4d}", end="  ")
        if (i + 1) % 10 == 0:
            print()  # New line after every 10 primes
    
    print(f"\n\nTotal prime numbers found: {len(primes)}")


if __name__ == "__main__":
    main()