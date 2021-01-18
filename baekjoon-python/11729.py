import sys


process = []


def run():
    hanoi(int(sys.stdin.readline()), 1, 2, 3)
    print(len(process))
    for a, b in process:
        print(a, b)


def hanoi(num, start, via, dst):
    if num == 1:
        process.append([start, dst])
    else:
        hanoi(num - 1, start, dst, via)     # n-1원반까지 start로 시작해서 dst를 거쳐 via로 가라. 그럼 start에 가장 큰 원반이 남을 것이다.
        process.append([start, dst])        # 가장 큰 원반을 start에서 dst로 원반을 이동시켜라.
        hanoi(num - 1, via, start, dst)     # 나머지 원반을 via에서 시작해서 start를 거쳐 dst로 이동시켜라.


if __name__ == "__main__":
    run()
