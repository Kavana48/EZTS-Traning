def is_prime(n):
     if n <= 1:
         return False
     if n <= 3:
        return True
     if n % 2 == 0 or n % 3 == 0:
         return False
     i = 5
     while i * i <= n:
         if n % i == 0 or n % (i + 2) == 0:
             return False
         i += 6
     return True
def next_prime(n):
    prime_candidate = n + 1
    while not is_prime(prime_candidate):
        prime_candidate += 1
    return prime_candidate
num=int(input())
print(f"The smallest prime number larger than {num} is {next_prime(num)}")