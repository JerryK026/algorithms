import sys


def run():
    arr = [[1, 0], [0, 1]]
    for _ in range(2, 41):
        arr.append([arr[-1][i] + arr[-2][i] for i in range(2)])

    for _ in range(int(sys.stdin.readline())):
        a, b = arr[int(sys.stdin.readline())]
        print(a, b)


if __name__ == "__main__":
    run()
