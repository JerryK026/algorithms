import sys
import math


def turret():
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if d == 0 and r1 == r2:
        return -1
    elif r1 + r2 == d or abs(r1 - r2) == d:
        return 1
    elif r1 + r2 < d or d + min([r1, r2]) < max([r1, r2]):
        return 0
    else:
        return 2


def run():
    for _ in range(int(sys.stdin.readline())):
        print(turret())


if __name__ == "__main__":
    run()
