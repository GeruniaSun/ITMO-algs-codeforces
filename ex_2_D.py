def find_moves(curr: [int], expect: [int], n: int) -> str:
    moves = []

    for i in range(n):
        j = i
        while j < n and expect[j] != curr[i]:
            j += 1

        while j > i:
            expect[j - 1], expect[j] = expect[j], expect[j - 1]
            moves.append(f'{j} {j + 1}\n')
            j -= 1

    return f'{len(moves)}\n' + ''.join(moves)


def main():
    n = int(input())
    curr = [int(x) for x in input().split()]
    expect = [int(x) for x in input().split()]
    print(find_moves(curr, expect, n))


if __name__ == '__main__':
    main()
