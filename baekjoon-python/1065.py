import sys


def run():
    num = int(sys.stdin.readline())
    if num < 100:
        cnt = num
    elif num == 1000:
        cnt = 144
    else:
        cnt = 99
        for i in range(100, num + 1):
            a, b, c = map(int, str(i))
            if a - b == b - c:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    run()
