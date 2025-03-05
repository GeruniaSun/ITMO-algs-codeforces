from collections import namedtuple

dot = namedtuple('dot', ['id', 'coord', 'weight'])

def read_dots(m: int) -> [dot]:
    dots = []

    for i in range(m):
        x, w = map(int, input().split())
        dots.append(dot(i + 1, x, w))

    return dots

def print_answer(weight: int, n: int, dots: [dot]):
    print(weight)

    for i in range(n):
        print(dots[i].id, dots[2 * n - i - 1].id)

def find_min_weight() -> None:
    n, m = map(int, input().split())
    dots = read_dots(m)

    dots = sorted(dots, key=lambda d: d.weight)[:2 * n]
    min_weight = sum([d.weight for d in dots])
    dots.sort(key=lambda d: d.coord)

    print_answer(min_weight, n, dots)



def main():
    test_count = int(input().strip())
    for _ in range(test_count):
        _ = input()
        find_min_weight()


if __name__ == '__main__':
    main()