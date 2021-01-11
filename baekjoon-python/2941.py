import sys


def croatia():
    s = sys.stdin.readline().rstrip()
    cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for c in cro:
        s = s.replace(c, "a")
    print(len(s))


if __name__ == "__main__":
    croatia()