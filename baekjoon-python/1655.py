import sys
import heapq


def run():
    minheap, maxheap = list(), list()
    num = int(sys.stdin.readline())
    for _ in range(num):
        cur = int(sys.stdin.readline())
        if len(maxheap) == len(minheap):
            heapq.heappush(maxheap, -cur)
        else:
            heapq.heappush(minheap, cur)
        if minheap and -maxheap[0] > minheap[0]:
            tmp1 = -heapq.heappop(maxheap)
            tmp2 = heapq.heappop(minheap)
            heapq.heappush(maxheap, -tmp2)
            heapq.heappush(minheap, tmp1)
        print(-maxheap[0])


if __name__ == '__main__':
    run()
