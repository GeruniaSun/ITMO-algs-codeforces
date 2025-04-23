def delete_common(a, b):
    count_b = {}
    for x in b: count_b[x] = count_b.get(x, 0) + 1

    new_a = []
    for x in a:
        if count_b.get(x, 0) > 0:
            count_b[x] -= 1
        else:
            new_a.append(x)

    new_b = []
    for x, cnt in count_b.items():
        new_b.extend([x] * cnt)

    return new_a, new_b


def replace_multidigit(arr):
    res = []
    cnt = 0

    for x in arr:
        if x > 9:
            res.append(len(str(x)))
            cnt += 1
        else:
            res.append(x)

    return res, cnt


def solve(a, b):
    a, b = delete_common(a, b)

    a, count_a = replace_multidigit(a)
    b, count_b = replace_multidigit(b)
    ans = count_a + count_b

    a, b = delete_common(a, b)
    ans += sum(1 for x in (a + b) if x != 1)

    return ans


def main():
    t = int(input())
    for _ in range(t):
        _ = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(solve(a, b))


if __name__ == "__main__":
    main()
