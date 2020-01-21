def exp_search(a, origin, point):
    end = len(a)
    while (origin + point < end):
        if a[origin + point] == 1:
            if point == 0:
                return origin
            else:
                origin = origin + int((point - 1) / 2) + 1
                return exp_search(a, origin, 0)
        point = point * 2 + 1

    if (origin + point > end):
        origin = origin + int((point - 1) / 2) + 1
        return exp_search(a, origin, 0)

    return -1

def binary_search(a, low, high):
    if low == high == 0:
        return -1
    mid = int((low + high)/2)
    if mid == low:
        if a[mid] == 1: return mid
        if a[mid] == 0: return -1
    else:
        if a[mid-1] == a[mid] == 0: low = mid + 1
        if a[mid-1] == a[mid] == 1: high = mid
        if a[mid-1] == 0 and a[mid] == 1: return mid
        return binary_search(a, low, high)


def search(a, type = 'binary'):
    if type == 'binary':
        return binary_search(a, 0, len(a))
    if type == 'exp':
        return exp_search(a, 0, 0)


def create(m, n):
    a = [0 for i in range(m)]
    b = [1 for i in range(n)]
    a.extend(b)
    return a

if __name__ == '__main__':
    for type in ['exp', 'binary']:
        assert (search(create(8, 8)) == 8)
        assert (search(create(2, 4)) == 2)
        assert (search(create(10, 20)) == 10)
        assert (search(create(16, 32)) == 16)
        assert (search(create(32, 16)) == 32)
        assert (search(create(0, 20)) == 0) # all 1s
        assert (search(create(20, 0)) == -1) # all 0s
        assert (search(create(0, 0)) == -1) # no elements
