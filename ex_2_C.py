from itertools import accumulate


def check(m: int, arr: [], k: int, n: int):
    indices = [1 if elem >= m else -1 for elem in arr]
    sums = list(accumulate(indices, initial=0))
    min_sum = sums[0]
    max_diff = 0
    for i in range(k, n + 1):
        min_sum = min(min_sum, sums[i - k])
        max_diff = max(max_diff, sums[i] - min_sum)

    return max_diff > 0


def max_median(arr: [], k: int, n: int) -> int:
    left = 0
    right = n + 1
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, arr, k, n):
            left = mid
        else:
            right = mid - 1

    return left


def main():
    n, k = map(int, input().split())
    array = [int(x) for x in input().split()]
    print(max_median(array, k, n))


if __name__ == '__main__':
    main()
