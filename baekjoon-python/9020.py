import sys
import bisect


def run():
    era = eratos(10000)
    for _ in range(int(sys.stdin.readline())):
        num = int(sys.stdin.readline())
        # 현재 입력된 짝수보다 작은 최대의 소수.
        bp = bisect.bisect_left(era, num)
        result = list()

        for i in range(bp):
            for j in range(bp, i - 1, -1):
                if era[i] + era[j] == num:
                    result = [era[i], era[j]]
                    break
        a, b = result
        print(a, b)



def eratos(num):
    arr = [True] * (num + 1)
    arr[0], arr[1] = False, False

    m = int((num + 1) ** 0.5)
    for i in range(2, m):
        if arr[i] == True:
            for j in range(i + i, num, i):
                arr[j] = False

    return [i for i in range(num + 1) if arr[i] == True]


if __name__ == '__main__':
    run()
