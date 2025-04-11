import math
import time


def forward(x: int, y: int) -> int:
    return x * y


def backwards(n: int):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors


def main():
    start = time.monotonic_ns()
    x = forward(769, 953)
    end = time.monotonic_ns()
    first_time = end - start
    print(x, end-start)
    start = time.monotonic_ns()
    y = backwards(x)
    end = time.monotonic_ns()
    second_time = end - start
    print(y, end-start)
    print(second_time/first_time)


if __name__ == '__main__':
    main()
