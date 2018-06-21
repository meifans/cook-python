import heapq


def the_n():

    # 最大最小n个数
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    # 以某个key为标准，最大最小n个数
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    print(expensive)

    # 建造堆
    heapq.heapify(nums)
    print(nums)
    # 顺序弹出最小的三个元素
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))


if __name__ == "__main__":
    the_n()
