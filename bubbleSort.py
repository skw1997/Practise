def swap(arr, x, y):
    arr[x] = int(arr[x])
    arr[y] = int(arr[y])
    arr[x] = arr[x]^arr[y]
    arr[y] = arr[x]^arr[y]
    arr[x] = arr[y]^arr[x]

def bbsort(arr):
    n = len(arr)

    for i in range(n-1):
        sw = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                swap(arr, j ,j+1)
                sw = True
        if not sw: break
    return arr

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(arr[0])
    print(bbsort(arr))
