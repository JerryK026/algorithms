def run():
    inform = input().split()
    row_size, column_size, target = inform[:]
    arr = list()
    tar = list()

    for _ in range(int(row_size)):
        token = input().split()
        arr.append([int(x) for x in token])

    for _ in range(int(target)):
        target_token = input().split()
        tar = [int(x) - 1 for x in target_token]
        sum_list = 0

        for i in range(tar[0], tar[2]+1):
            sum_list += sum(arr[i][tar[1]:tar[3] + 1])

        print(sum_list // ((tar[2] - tar[0] + 1) * (tar[3] - tar[1] + 1)))


if __name__ == '__main__':
    run()
