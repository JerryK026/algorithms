import sys


def run():
    line = sys.stdin.readline().split()
    M, N = [int(x) for x in line]
    eratos, result = list(), list()

    for i in range(2, N + 1):
        eratos.append(i)

    for i in eratos:
        if i >= M:
            result.append(i)
        tmp = N // i
        tmp2 = i
        for j in range(1, tmp):
            tmp2 += i
            if tmp2 in eratos:
                eratos.remove(tmp2)

    for i in result:
        print(i)


if __name__ == '__main__':
    run()
