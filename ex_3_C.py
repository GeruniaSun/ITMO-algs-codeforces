def solve(s):
    opening = {'(', '{', '[', '<'}
    closing_map = {')': '(', '}': '{', ']': '[', '>': '<'}
    stack = []
    mismatches = 0

    for ch in s:
        if ch in opening: stack.append(ch)
        else:
            if not stack or ch not in closing_map: return None

            top = stack.pop()
            if closing_map[ch] != top: mismatches += 1

    if stack:
        return None

    return mismatches


def main():
    result = solve(input().strip())

    if result is None:
        print("Impossible")
    else:
        print(result)


if __name__ == "__main__":
    main()
