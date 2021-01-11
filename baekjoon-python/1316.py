import sys


def group():
    num = int(sys.stdin.readline())
    cnt = 0
    for _ in range(num):
        s = sys.stdin.readline().rstrip()
        cnt += check(s)
    print(cnt)


def check(s):
    for i in range(len(s) - 1):
        check = True
        if s[i] != s[i + 1]:
            check = False
        for j in range(i + 1, len(s)):
            if not check and s[i] == s[j]:
                return 0
    return 1


if __name__ == "__main__":
    group()
