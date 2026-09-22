# do not modify this function
def sat(prod: int, n=14235764939971075543215213):
    for c in str(n):
        i = int(c)
        if i % 2 == 1:
            assert prod % i == 0
            prod //= i
    return prod == any(int(c) % 2 for c in str(n))

def sol(n=14235764939971075543215213):
    """Return the product of the odd digits in n, or 0 if there aren't any

    12345 => 15
    """
    # TODO: your implementation here
    product = 1
    has_odd_digit = False
    for c in str(n):
        i = int(c)
        if i % 2 == 1:
            product *= i
            has_odd_digit = True    
    if has_odd_digit:
        return product
    else:
        return 0


print(sat(sol()))
