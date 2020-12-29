import sys


def run():
    inp = sys.stdin.readline().split()
    row_size, column_size, target = [int(x) for x in inp]

    # src 만들기
    src = list()
    for _ in range(row_size):
        token = sys.stdin.readline().split()
        src.append([int(i) for i in token])

    # integral image (prefix sum)
    integral = [[0 for col in range(column_size)] for row in range(row_size)]

    for r in range(row_size):
        sum_tmp = 0
        for c in range(column_size):
            sum_tmp += src[r][c]
            integral[r][c] = integral[r-1][c] + sum_tmp

    for _ in range(target):
        tar = sys.stdin.readline().split()
        # 1,1부터 세므로 1을 빼서 넣는다.
        r1, c1, r2, c2 = [int(x) - 1 for x in tar]
        A, B, C, D = integral[r1-1][c1-1], integral[r1-1][c2], integral[r2][c1-1], integral[r2][c2]
        if r1 == 0:
            A, B = 0, 0
        if c1 == 0:
            A, C = 0, 0
        val_sum = A + D - B - C
        val_num = (r2 - r1 + 1) * (c2 - c1 + 1)
        output = val_sum // val_num
        print(output)


if __name__ == '__main__':
    run()
