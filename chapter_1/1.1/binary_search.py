import sys

def rank(key, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as w:
        whitelist = w.read().split()

    with open(sys.argv[2], 'r') as c:
        check = c.read().split()

    whitelist = sorted(whitelist)

    for key in check:
        if rank(key, whitelist) < 0:
            print(key)
