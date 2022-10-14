"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    final_list = []
    prime_list = []
    if number_of_primes <= 0:
        raise ValueError('Number in argument must be positive')
    for num in range(2, 1000):
        div = 0;
        for i in range(2,num):
            if num % i == 0:
                div += 1
            if div == 0 or num == 2:
                prime_list.append(num)
    for x in range(number_of_primes):
        final_list.append(prime_list[x])
    return final_list
