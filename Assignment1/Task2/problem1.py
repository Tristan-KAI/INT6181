from typing import List

# do not modify this function
def sat(li: List[int]):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

def sol():
    """Find a list of one hundred integers between 0 and 999 which all differ by at least ten from one another."""
    # TODO: your implementation here
    return list(range(0, 1000, 10))



print(sat(sol()))
