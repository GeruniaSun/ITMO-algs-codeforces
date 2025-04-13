def is_impossible(n: int, pos: int, neg: int) -> bool:
    return not (pos - n * neg <= n <= n * pos - neg)


def find_x(n: int, balance: int, sgn: int, pos: int, neg: int) -> int:
    ans = -999
    for x in range(1, n + 1):
        min_l = balance + sgn * x + pos - n * neg
        max_l = balance + sgn * x + n * pos - neg
        if min_l <= n <= max_l:
            ans = x
            break
    return ans


def solve_puzzle(s: str) -> str:
    n = int(s.split()[-1])
    pos = s.count('+') + 1
    neg = s.count('-')

    if s.count('?') == 1:
        return f"Possible\n{s.replace('?', str(n))}"

    if is_impossible(n, pos, neg):
        return "Impossible"

    balance = 0
    for c in filter(lambda x: x != '?', ['+'] + s.split()[:-2]):
        sgn = 1 if c == '+' else -1
        if sgn == 1: pos -= 1
        if sgn == -1: neg -= 1

        curr = find_x(n, balance, sgn, pos, neg)
        balance += sgn * curr
        s = s.replace('?', str(curr), 1)

    return f"Possible\n{s}"


def main():
    print(solve_puzzle(input().strip()))


if __name__ == '__main__':
    main()
