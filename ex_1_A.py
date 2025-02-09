def solve_sequence():
    _ = int(input().strip())
    sequence = input().strip()
    balance = 0
    moves = 0

    for ch in sequence:
        balance += 1 if ch == '(' else -1
        if balance < 0:
            moves += 1
            balance = 0

    return moves


def main():
    test_count = int(input().strip())
    for _ in range(test_count):
        print(solve_sequence())


if __name__ == '__main__':
    main()
