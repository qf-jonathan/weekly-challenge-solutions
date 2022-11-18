def fizz_buzz(n: int) -> str:
    res = []
    if n % 3 == 0:
        res.append("Fizz")
    if n % 5 == 0:
        res.append("Buzz")
    return "".join(res) if res else str(n)


def solution():
    for i in range(1, 101):
        print(fizz_buzz(i))


if __name__ == "__main__":
    solution()
