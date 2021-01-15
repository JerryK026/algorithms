import sys


def turret():
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if d == 0 and r1 == r2:
        return -1
    elif r1 + r2 > d:
        if d < r1 or d < r2:
            return 0
        elif d == r2 - r1 or d == r1 - r2:
            return 1
        return 2
    elif r1 + r2 == d:
        return 1
    else:
        return 0


def run():
    for _ in range(int(sys.stdin.readline())):
        print(turret())


if __name__ == "__main__":
    run()
