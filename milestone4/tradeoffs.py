from typing import List, Tuple


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    for i, e in enumerate(li):
        for m, j in enumerate(li[i+1:]):
            if e + j == target:
                return (i, m+1)


assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
# The complexity is O(n^2)


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    num_index = {}
    for i, e in enumerate(li):
        diff = target - e
        if diff in num_index:
            return (i, num_index[diff])
        num_index[e] = i
    return 'None sum up to target'


assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}  
# The time complexity is O(n)
