import sys


def part_1():
    curr = 50
    password = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        direction = line[0]
        amount = int(line[1::])

        if direction == "R":
            curr = (curr + amount) % 100

        else:
            curr = (curr - amount) % 100

        if curr == 0:
            password += 1

    return password


def part_2():
    curr = 50
    password = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        direction = line[0]
        amount = int(line[1:])

        if direction == "R":
            password += (curr + amount) // 100
            curr = (curr + amount) % 100
        else:
            if curr == 0:
                password += amount // 100
            elif amount >= curr:
                password += (amount - curr) // 100 + 1
            curr = (curr - amount) % 100

    return password


print(part_1())
print(part_2())
