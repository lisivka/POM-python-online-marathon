# TODO: task_4 +
"""
Given two permutations p and q of length n. Find a permutation r, such that for every 1 <= i <= n, q[i] = p[r[i]].
Permutation of length n is an array consisting of distinct numbers from 1 to n in some order.

Example
Input:
p = [5, 1, 3],  q = [3, 1, 5]

Output:
r = [3, 2, 1]
[input] array.integer p
[input] array.integer q
[output] array.integer
permutation r
"""

def findPermutation(p:list, q:list):
    # result = []
    # for i in q:
    #     result.append(p.index(i)+1)
    result = [p.index(i)+1 for i in q]
    return result

p = [3, 4, 1, 2, 5]
q = [4, 5, 2, 3, 1]
print(findPermutation(p, q))

# [2, 5, 4, 1, 3]

