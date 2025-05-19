def update_energy(i, j, best, d, a, x, y):
    if best[i] == -float('inf'):
        return False

    cost = d * (abs(x[i] - x[j]) + abs(y[i] - y[j]))
    if best[i] < cost:
        return False

    new_energy = best[i] - cost + a[j]
    if new_energy > best[j]:
        best[j] = new_energy
        return True

    return False


def can_reach_end(n, d, a, x, y, mi):
    best = [-float('inf')] * n
    best[0] = mi

    for _ in range(n):
        updated = False
        for i in range(n):
            for j in range(n):
                if i != j and update_energy(i, j, best, d, a, x, y):
                    updated = True

        if not updated:
            break

    return best[-1] >= 0


def solve(n, d, a, x, y):
    lo = 0
    hi = 50000000

    while lo < hi:
        mi = (lo + hi) // 2
        if can_reach_end(n, d, a, x, y, mi):
            hi = mi
        else:
            lo = mi + 1

    return lo


def main():
    n, d = map(int, input().split())
    a = [0] + list(map(int, input().split())) + [0]
    x, y = map(list, zip(*(map(int, line.split()) for line in [input() for _ in range(n)])))

    print(solve(n, d, a, x, y))

if __name__ == "__main__":
    main()
