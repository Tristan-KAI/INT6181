from typing import List

# do not modify this function
def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    """Find a list integers such that the integer i occurs i times, for i = 0, 1, 2, ..., 9."""
    result = []
    for i in range(10):
        result = result + [i] * i
    return  result



print(sat(sol()))
