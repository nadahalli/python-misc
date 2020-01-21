def search(a, origin, point):
    end = len(a)
    while (origin + point < end):
        if a[origin + point] == 1:
            if point == 0:
                return origin
            else:
                origin = origin + int((point - 1) / 2) + 1
                return search(a, origin, 0)
        point = point * 2 + 1

    # Figure out a way to write this if condition as a part of the main else in the while loop
    if (origin + point > end):
        origin = origin + int((point - 1) / 2) + 1
        return search(a, origin, 0)

    return -1


def create(m, n):
    a = [0 for i in range(m)]
    b = [1 for i in range(n)]
    a.extend(b)
    return a


if __name__ == '__main__':
    assert (search(create(10, 20), 0, 0) == 10)
    assert (search(create(16, 32), 0, 0) == 16)
    assert (search(create(0, 20), 0, 0) == 0)  # all 1s
    assert (search(create(20, 0), 0, 0) == -1)  # all 0s
    assert (search(create(0, 0), 0, 0) == -1)  # no elements
