def find_all_shovels_pairs(n: int) -> int:
    max_sum = 2 * n - 1
    max_sum_length = len(str(max_sum))

    # скип неинтересных случаев
    if n < 5:
        return sum(range(n))
    if str(max_sum) == '9' * max_sum_length:
        return 1

    pairs = 0
    for digit in range(9):
        candidate = int(f"{digit}{'9' * (max_sum_length - 1)}")

        if candidate <= n + 1:
            pairs += candidate // 2
        elif candidate > max_sum:
            break
        else:
            pairs += (n - (candidate - n) + 1) // 2

    return pairs


def main():
    n = int(input().strip())
    print(find_all_shovels_pairs(n))


if __name__ == '__main__':
    main()
