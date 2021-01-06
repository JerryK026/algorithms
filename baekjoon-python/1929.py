import sys


def run():
    M, N = sys.stdin.readline().split()
    M, N = int(M), int(N) + 1

    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    eratos = [True] * N
    eratos[0], eratos[1] = False, False

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if eratos[i] == True:           # i가 소수인 경우
            for j in range(i+i, N, i): # i이후 i의 배수들을 False 판정
                eratos[j] = False

    # 소수 목록 산출
    result = [i for i in range(M, N) if eratos[i] == True]

    for i in result:
        print(i)


if __name__ == '__main__':
    run()
