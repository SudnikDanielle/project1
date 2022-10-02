press = int(input())
line = list(map(int, input().split()))
x = int(input())


def nearest(where, who):
    return (where , key=lambda s: min(s - who))


print(nearest(line, x))
