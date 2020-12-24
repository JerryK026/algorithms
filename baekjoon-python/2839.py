def run():
    sugar = int(input())
    num = 5
    count = 1

    if sugar == 4 or sugar == 7:
        return -1

    while num <= sugar:
        num += 5
        count += 1

    num -= 5
    count -= 1

    if num == sugar:
        return count

    while num >= 0:
        while num <= sugar:
            num += 3
            count += 1

        num -= 3
        count -= 1

        if num == sugar:
            return count
        num -= 5
        count -= 1

    return -1


if __name__ == '__main__':
    print(run())

