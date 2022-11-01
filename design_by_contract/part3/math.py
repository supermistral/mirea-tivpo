import deal, math


@deal.pre(lambda n: n >= 0)
@deal.post(lambda res: res >= 0)
def sqrt(x: float) -> float:
    return x ** 0.5


@deal.post(lambda res: 0 <= res <= 1)
def sin(x: float) -> float:
    return math.sin(x)


@deal.pre(lambda n: isinstance(n, int) and n >= 0)
@deal.post(lambda res: isinstance(res, int) and res >= 1)
def factorial(x: int) -> int:
    res = 1
    for i in range(2, x + 1):
        res *= i
    return res


if __name__ == '__main__':
    print(sqrt(0), sqrt(2), sqrt(-2))
