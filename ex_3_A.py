def registration_status(names: list[str]) -> list[str]:
    registered = dict.fromkeys(names, 0)
    responses = []
    for name in names:
        responses.append('OK' if registered[name] == 0 else f'{name}{registered[name]}')
        registered[name] += 1

    return responses


def main():
    n = int(input())
    names = [input() for _ in range(n)]
    print(*registration_status(names), sep='\n')


if __name__ == '__main__':
    main()
