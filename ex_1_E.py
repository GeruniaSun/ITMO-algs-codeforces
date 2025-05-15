from itertools import permutations

def solve(k, matrix):
    return min(
        max(int(''.join(str(row[i]) for i in perm)) for row in matrix) -
        min(int(''.join(str(row[i]) for i in perm)) for row in matrix)
        for perm in permutations(range(k))
    )

def main():
    n, k = map(int, input().split())
    matrix = [[int(d) for d in input()[::-1]] for _ in range(n)]
    print(solve(k, matrix))

if __name__ == "__main__":
    main()
