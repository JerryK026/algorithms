import sys

arr = [0, 0]


def run():
    for _ in range(int(sys.stdin.readline())):
        fibonacci(int(sys.stdin.readline()))
        print(arr[0], arr[1], sep=" ")
        arr[0], arr[1] = [0, 0]


def fibonacci(num):
    if num == 0:
        arr[0] += 1
        return 0
    elif num == 1:
        arr[1] += 1
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    run()
