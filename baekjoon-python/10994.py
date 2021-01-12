import sys


def run():
    result = stars(int(sys.stdin.readline()))
    for i in result:
        print(i)


def stars(num):
    if num == 1:
        return "*"
    else:
        s = stars(num-1)
        st = "****" + "*" * len(s[0])
        sp = "* " + " " * len(s[0]) + " *"
        s2 = list()
        for i in range(len(s[0])):
            s2.append("* " + s[i] + " *")
        s2.insert(0, sp)
        s2.insert(0, st)
        s2.append(sp)
        s2.append(st)
        return s2


if __name__ == "__main__":
    run()
