n = int(input())


def func(x, a):
    return int(x/a) + x % a

for _ in range(n):
    a, b, c = list(map(int, input().split()))
    if b == c and b - a > a:
        print(b - 1)
        continue
    res = []
    for i in range(a, b+1):
        res.append(func(i, c))
    # print(res)
    print(max(res))
    # print(x, y, z)
    # print(res)