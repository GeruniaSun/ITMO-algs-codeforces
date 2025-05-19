from collections import deque
from array import array

def bfs(n, m, positions):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    fire = array('B', [0]) * (n * m)
    q = deque()
    res = (0, 0)

    for x, y in positions:
        idx = x * m + y
        if not fire[idx]:
            fire[idx] = True
            q.append(idx)

    while q:
        idx = q.popleft()
        x, y = divmod(idx, m)
        res = (x, y)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                nidx = nx * m + ny
                if not fire[nidx]:
                    fire[nidx] = True
                    q.append(nidx)

    return res


def parse_data(data):
    ptr = 0
    n, m = int(data[ptr]), int(data[ptr + 1])
    ptr += 2
    k = int(data[ptr])
    ptr += 1
    numbers = list(map(int, data[ptr:ptr + 2 * k]))

    fires = []
    for i in range(0, 2 * k, 2):
        x = numbers[i] - 1
        y = numbers[i + 1] - 1
        fires.append((x, y))

    return n, m, fires


def main():
    with open("input.txt", "r") as f:
        data = f.read().split()

    n, m, fires = parse_data(data)

    res_x, res_y = bfs(n, m, fires)

    with open("output.txt", "w") as f:
        f.write(f"{res_x + 1} {res_y + 1}")

if __name__ == "__main__":
    main()
