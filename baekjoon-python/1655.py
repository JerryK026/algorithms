from bisect import bisect_left


def run():
    size = int(input())
    arr = list()

    for _ in range(size):
        num = int(input())
        arr_length = len(arr)
        pointer = bisect_left(arr, num)
        arr.insert(pointer, num)
        arr_length += 1

        if arr_length % 2 == 1:
            index = arr_length // 2 + 1
        else:
            if arr_length / 2 < (arr_length / 2) + 1:
                index = arr_length // 2
            else:
                index = arr_length // 2 + 1
        index = index - 1
        print(arr[index])


if __name__ == '__main__':
    run()
