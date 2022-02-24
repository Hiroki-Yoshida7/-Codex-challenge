import itertools
from typing import List


def count_arrangements(sizes: List[int]) -> int:
    # Given the sizes of several buckets given in the list named sizes, write a program to find the number of different ways to arrange the buckets such that the first bucket’s size is greater than the second bucket’s size.
    answer = 0

    if len(sizes) <= 1:
        return answer

    remaining_buckets = sizes[:]
    for permutation in itertools.permutations(remaining_buckets):
        if permutation[0] > permutation[1]:
            answer += 1
    return answer

# Examples
print(count_arrangements([1, 3, 1]))    #2
print(count_arrangements([1, 2]))       #1
print(count_arrangements([10]))         #10