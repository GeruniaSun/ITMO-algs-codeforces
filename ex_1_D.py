def update_prime_factors(a, ma):
    while a % 2 == 0:
        ma[2] = ma.get(2, 0) + 1
        a = a // 2

    i = 3
    while i * i <= a:
        while a % i == 0:
            ma[i] = ma.get(i, 0) + 1
            a = a // i
        i += 2

    if a > 1:
        ma[a] = ma.get(a, 0) + 1


def solve_array() -> str:
    n = int(input())
    mp = {}

    for x in list(map(int, input().split())):
        update_prime_factors(x, mp)

    ok = True
    for count in mp.values():
        if count % n != 0:
            ok = False
            break

    return "YES" if ok else "NO"


def main():
    test_count = int(input().strip())
    for _ in range(test_count):
        print(solve_array())


if __name__ == '__main__':
    main()
