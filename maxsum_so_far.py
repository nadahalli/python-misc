from math import inf
import hashlib
import os

def find_middle(cvalues, half):
    leftmax = -inf
    sum = 0
    for i in reversed(cvalues[:half]):
        sum += i
        if sum > leftmax:
            leftmax = sum
    rightmax = -inf
    sum = 0
    for i in cvalues[half:]:
        sum += i
        if sum > rightmax:
            rightmax = sum
    return leftmax + rightmax

def fingerprint_array(array):
    return hashlib.sha256('.'.join(map(str, array)).encode('utf-8')).hexdigest()

def max_sum(cvalues, memoized):
    cvalues_fp = fingerprint_array(cvalues)
    if cvalues_fp in memoized:
        return memoized[cvalues_fp], memoized

    length = len(cvalues)
    if length == 1:
        return cvalues[0], memoized
    half = int(length/2)
    left, memoized = max_sum(cvalues[:half], memoized)
    right, memoized= max_sum(cvalues[half:], memoized)
    middle = find_middle(cvalues, half)

    ret_val = max(left, right, middle)
    memoized[cvalues_fp] = ret_val

    return ret_val, memoized

def max_sum2(cvalues):
    max_so_far = 0
    max_now = 0
    for i in cvalues:
        max_now = max(max_now + i, 0)
        max_so_far = max(max_so_far, max_now)
    return max_so_far

def make_tree(parent, values):
    tree = {}
    for node, parent, value in zip(range(len(parent)), parent, values):
        tree[node] = (parent, value)
    return tree

def find_tree_path_values(tree, node):
    values = []
    for i in range(100000):
        if node not in tree:
            raise RuntimeError('Node not found!')
        parent, value = tree[node]
        values.append(value)
        if parent == -1:
            return values
        else:
            node = parent
    raise RunTimeError('Unrooted Tree!')

def find_leaves(tree):
    parents = set([])
    for _, (parent, _) in tree.items():
        parents.add(parent)
    leaves = []
    for node in tree:
        if node not in parents:
            leaves.append(node)
    return leaves
#
# Complete the 'bestSumDownwardTreePath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY values
#

def bestSumDownwardTreePath(parent, value):
    memoized = {}
    tree = make_tree(parent, values)
    max_so_far = -inf
    for node in find_leaves(tree):
        #max_for_node, memoized = max_sum(find_tree_path_values(tree, node), memoized)
        max_for_node = max_sum2(find_tree_path_values(tree, node))
        max_so_far = max(max_so_far, max_for_node)
    return max_so_far

if __name__ == '__main__':
    parent = [-1, 0, 1, 2, 0]
    values = [-2, 10, 10, -3, 10]
    print(bestSumDownwardTreePath(parent, values))
