n = int(input())


for _ in range(n):
    a, b, c = list(map(int, input().split()))
    for x in range(5_000):
        for y in range(5_000):
            for z in range(5_000):
                if x % y == a and y % z == b and z % x == c:
                    print(x, y, z)
                    break
                    break
                    break
                