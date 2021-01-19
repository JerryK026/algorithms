import sys


def run():
    arr = list()
    result = list()
    for _ in range(int(sys.stdin.readline())):
        arr.append(sys.stdin.readline().split())

    for w1, h1 in arr:
        count = 1
        for w2, h2 in arr:
            if w2 > w1 and h2 > h1:
                count += 1
        result.append(count)
    print(" ".join(str(x) for x in result))


if __name__ == "__main__":
    run()
