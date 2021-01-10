import sys
import bisect

def run():
    era = eratos(10000)
    for _ in range(int(sys.stdin.readline())):
        num = int(sys.stdin.readline())

        # 어차피 입력되는 건 짝수인데, 짝수는 2개의 홀수로 나뉘어질 수 있다. 그 홀수는 최대의 소수가 될 수 있을 것.
        # bp는 반으로 나눴을 때 그것보다 작은 가장 큰 소수(최대 딱 절반)의 index. b2는 num보다 작은 가장 큰 소수
        bp = bisect.bisect_right(era, num // 2) - 1
        bp2 = bisect.bisect_right(era, num) - 1
        check = False
        for i in range(bp, -1, -1):
            for j in range(bp, bp2, 1):
                if era[i] + era[j] == num:
                    print(era[i], era[j], sep=" ")
                    check = True
                    break
            if check:
                break


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
