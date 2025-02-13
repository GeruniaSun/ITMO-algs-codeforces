def eratosthenes(n: int) -> list[int]:
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n + 1, number):
                numbers[candidate - 2] = 0

    return list(filter(lambda x: x != 0, numbers))

def solve_array() -> str:
    len_arr = int(input().strip())
    arr = [int(x) for x in input().strip().split()]
    primes = eratosthenes(10 ** 6)
    primes_dict = {key: 0 for key in primes}

    for x in arr:
        num = x
        while num > 1:
            for p in primes:
                if num % p == 0:
                    primes_dict[p] += 1
                    num //= p
                if p > x // 2:
                    break

    return "YES" if all(value == 0 or value % len_arr == 0 for value in primes_dict.values()) else "NO"


def main():
    test_count = int(input().strip())
    for _ in range(test_count):
        print(solve_array())


if __name__ == '__main__':
    main()
