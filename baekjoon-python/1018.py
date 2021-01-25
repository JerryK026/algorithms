import sys


def run():
    m, n = map(int, sys.stdin.readline().split())
    b, w = [[], []]
    # b, w는 왼쯕 상단이 각각 black일 때, white일 때, 다른 색으로 칠해야 하는지. 칠해야 하면 1 필요 없으면 0.
    for c in range(m):
        inp = sys.stdin.readline().replace("\n", "")
        b_tmp, w_tmp = [[], []]
        for i in range(len(inp)):
            if c % 2 == 0:
                if i % 2 == 0:
                    if inp[i] == "B":
                        b_tmp.append(0)
                        w_tmp.append(1)
                    else:
                        b_tmp.append(1)
                        w_tmp.append(0)
                else:
                    if inp[i] == "B":
                        b_tmp.append(1)
                        w_tmp.append(0)
                    else:
                        b_tmp.append(0)
                        w_tmp.append(1)
            else:
                if i % 2 == 0:
                    if inp[i] == "W":
                        b_tmp.append(0)
                        w_tmp.append(1)
                    else:
                        b_tmp.append(1)
                        w_tmp.append(0)
                else:
                    if inp[i] == "W":
                        b_tmp.append(1)
                        w_tmp.append(0)
                    else:
                        b_tmp.append(0)
                        w_tmp.append(1)
        b.append(b_tmp)
        w.append(w_tmp)
    smallest = sys.maxsize
    for m_i in range(m-7):
        for n_i in range(n-7):
            b_sum, w_sum = [0, 0]
            for tmp in range(m_i, m_i+8):
                b_sum += sum(b[tmp][n_i:n_i+8])
                w_sum += sum(w[tmp][n_i:n_i+8])
            count = w_sum if b_sum > w_sum else b_sum
            if count < smallest:
                smallest = count
    print(smallest)


if __name__ == "__main__":
    run()
