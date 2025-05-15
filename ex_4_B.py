def volume(n, m, visited, grid, stack):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    s = 0

    while stack:
        r, c = stack.pop()
        s += grid[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    stack.append((nr, nc))

    return s


def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    max_vol = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 or visited[i][j]:
                continue

            stack = [(i, j)]
            visited[i][j] = True

            max_vol = max(max_vol, volume(n, m, visited, grid, stack))

    return max_vol


def main():
    t = int(input())
    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    main()