class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find_set(self, v):
        if self.parent[v] == v:
            return v

        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def make_set(self, v):
        self.parent[v] = v
        self.size[v] = 1

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.parent[b] = a
            self.size[a] += self.size[b]


def process_input(n, input_data):
    c = [0] * (n + 1)
    d = DSU()
    for i in range(1, n + 1):
        d.make_set(i)

    for i in range(1, n + 1):
        t = input_data[i - 1]
        c[t] += 1
        c[i] += 1
        d.union_sets(t, i)

    return c, d


def count_cycles_and_chains(n, c, d):
    groups = {}
    for i in range(1, n + 1):
        root = d.find_set(i)
        if root not in groups:
            groups[root] = set()
        groups[root].add(i)

    n_cycles = 0
    n_chains = 0
    for g in groups.values():
        if len(g) == 2:
            n_chains += 1
            continue

        chain = False
        for i in g:
            if c[i] != 2:
                chain = True
                break

        if chain:
            n_chains += 1
        else:
            n_cycles += 1

    return n_cycles, n_chains


def solve(n, c, d):
    n_cycles, n_chains = count_cycles_and_chains(n, c, d)
    return n_cycles + (1 if n_chains > 0 else 0), n_cycles + n_chains


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        c, d = process_input(n, list(map(int, input().split())))
        print(*solve(n, c, d))

if __name__ == "__main__":
    main()
