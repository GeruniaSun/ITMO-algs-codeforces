import bisect

def insert_into_bst(n, values):
    a = [{'val': 0, 'left': -1, 'right': -1} for _ in range(n)]
    key_map = {}
    arr = []
    parents = []

    a[0]['val'] = values[0]
    arr.append(a[0]['val'])
    key_map[a[0]['val']] = 0

    for i in range(1, n):
        a[i]['val'] = values[i]
        key_map[a[i]['val']] = i

        high = bisect.bisect_right(arr, a[i]['val'])
        if high == 0:
            parents.append(arr[high])
            a[key_map[arr[high]]]['left'] = i
        else:
            low = arr[high - 1]
            if a[key_map[low]]['right'] == -1:
                parents.append(low)
                a[key_map[low]]['right'] = i
            else:
                parents.append(arr[high])
                a[key_map[arr[high]]]['left'] = i
        arr.insert(high, a[i]['val'])

    return parents

def main():
    n = int(input())
    values = list(map(int, input().split()))

    for parent in insert_into_bst(n, values):
        print(parent, end=" ")

if __name__ == "__main__":
    main()
