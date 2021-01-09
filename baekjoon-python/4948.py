def run():
    ber = bertrand(123456)
    num = int(input())
    while num != 0:
        result = [i for i in range(num + 1, num * 2 + 1) if ber[i] == True]
        print(len(result))
        num = int(input())


def bertrand(num):
    ber = [True] * (2 * num + 1)
    ber[0], ber[1] = False, False

    for i in range(2, len(ber)):
        for j in range(i+i, len(ber), i):
            ber[j] = False
    return ber


if __name__ == "__main__":
    run()
