# do not modify this function
def sat(x: float, coeffs=[2.5, 1.3, -0.5]):
    a, b, c = coeffs
    return abs(a * x ** 2 + b * x + c) < 1e-6

def sol(coeffs=[2.5, 1.3, -0.5]):
    """
    Find any (real) solution to:  a x^2 + b x + c where coeffs = [a, b, c].
    For example, since x^2 - 3x + 2 has a root at 1, sat(x = 1., coeffs = [1., -3., 2.]) is True.
    """
    # TODO: your implementation here
    a, b, c = coeffs
    discriminant = (b ** 2 - 4 * a * c) ** 0.5
    return (-b + discriminant) / (2 * a)



print(sat(sol()))
