def generate_login(user: str) -> str:
    name, surname = user.split()

    for i in range(1, len(name)):
        if name[i] >= surname[0]: return name[:i] + surname[0]

    return name + surname[0]


def main():
    print(generate_login(input().strip()))


if __name__ == '__main__':
    main()