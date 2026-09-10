def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 找出 1 到 100 之间的所有质数
primes = [num for num in range(1, 101) if is_prime(num)]

print("1 到 100 之间的所有质数为：")
print(primes)