def minimize_removals(n, I, arr):
    k = (8 * I) // n
    if k > 25: return 0
    K = 2 ** k

    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    counts = [freq[x] for x in sorted(freq)]
    m = len(counts)
    if m <= K: return 0

    prefix = [0]
    for c in counts:
        prefix.append(prefix[-1] + c)

    best = max(prefix[i] - prefix[i - K] for i in range(K, m + 1))

    return n - best


def main():
    n, I = map(int, input().split())
    arr = map(int, input().split())
    print(minimize_removals(n, I, arr))

if __name__ == "__main__":
    main()
