def part_1():
    invalid_id_sum = 0
    ids = [
        i
        for j in input().split(",")
        for i in range(int(j.split("-")[0]), int(j.split("-")[1]) + 1)
    ]

    for i in ids:
        if len(str(i)) % 2 == 0:
            s = str(i)
            half = len(s) // 2
            left = s[:half]
            right = s[half:]

            if left == right:
                invalid_id_sum += i
    return invalid_id_sum


def part_2():
    invalid_id_sum = 0
    ids = [
        i
        for j in input().split(",")
        for i in range(int(j.split("-")[0]), int(j.split("-")[1]) + 1)
    ]

    def is_repeated_pattern(s):
        n = len(s)
        for size in range(1, n):
            if n % size == 0:
                chunk = s[:size]
                if chunk * (n // size) == s:
                    return True
        return False

    for i in ids:
        if is_repeated_pattern(str(i)):
            invalid_id_sum += i

    return invalid_id_sum


print(part_1())
print(part_2())
